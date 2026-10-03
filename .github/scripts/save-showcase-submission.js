// Saves an approved Capstone Showcase Form issue into showcase/submissions/
// and rebuilds the gallery table in showcase/README.md.
// Used by .github/workflows/save-showcase-submission.yml via actions/github-script.

const fs = require("fs");
const path = require("path");

const SHOWCASE_DIR = "showcase";
const SUBMISSIONS_DIR = path.join(SHOWCASE_DIR, "submissions");
const GALLERY_FILE = path.join(SHOWCASE_DIR, "README.md");
const GALLERY_START = "<!-- gallery:start -->";
const GALLERY_END = "<!-- gallery:end -->";

const MAX_IMAGES = 6;
const MAX_IMAGE_BYTES = 10 * 1024 * 1024;
const IMAGE_TYPES = {
  "image/png": "png",
  "image/jpeg": "jpg",
  "image/gif": "gif",
  "image/webp": "webp",
};
const ALLOWED_IMAGE_HOSTS = [
  "github.com",
  "user-images.githubusercontent.com",
  "private-user-images.githubusercontent.com",
];

const FIELDS = {
  displayName: "Display name",
  capstone: "Capstone option",
  projectName: "Project name",
  liveUrl: "Live site link",
  repoUrl: "Repository link",
  screenshots: "Screenshots",
  problem: "The problem and your user",
  features: "What your project does",
  howBuilt: "How you built it",
  challenge: "Hardest part and what you learned",
  feedback: "Feedback and improvement",
  nextSteps: "What you would add next",
  credits: "Credits",
};
const REQUIRED = ["displayName", "capstone", "projectName", "screenshots"];
const CAPSTONES = ["School Opportunities Hub", "Kenya Weather Dashboard", "CyberSmart Quest"];

function parseIssueForm(body) {
  const sections = {};
  const parts = (body || "").replace(/\r\n/g, "\n").split(/^### +(.+)$/m);
  for (let i = 1; i < parts.length; i += 2) {
    const value = parts[i + 1].trim();
    sections[parts[i].trim()] = value === "_No response_" ? "" : value;
  }
  const result = {};
  for (const [key, label] of Object.entries(FIELDS)) {
    result[key] = sections[label] || "";
  }
  return result;
}

function oneLine(text, maxLength = 120) {
  return text.replace(/\s+/g, " ").trim().slice(0, maxLength);
}

function escapeCell(text) {
  return oneLine(text).replace(/[\\|<>[\]*_`]/g, (c) => `\\${c}`);
}

function escapeHtml(text) {
  return oneLine(text).replace(/[&<>"'|]/g, (c) => `&#${c.charCodeAt(0)};`);
}

function safeHttpsUrl(text) {
  try {
    const url = new URL(oneLine(text, 300));
    if (url.protocol !== "https:") return "";
    return url.href.replace(/[()|]/g, (c) => `%${c.charCodeAt(0).toString(16).toUpperCase()}`);
  } catch {
    return "";
  }
}

function slugify(text) {
  return (
    text
      .toLowerCase()
      .normalize("NFKD")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "")
      .slice(0, 40)
      .replace(/-+$/g, "") || "project"
  );
}

function findImageUrls(markdown) {
  const urls = [];
  const pattern = /!\[[^\]]*\]\(\s*<?([^)\s>]+)>?[^)]*\)|<img\b[^>]*\bsrc=["']([^"']+)["']/gi;
  for (const match of markdown.matchAll(pattern)) {
    const url = safeHttpsUrl(match[1] || match[2]);
    if (!url || urls.includes(url)) continue;
    const { hostname, pathname } = new URL(url);
    const allowed =
      ALLOWED_IMAGE_HOSTS.includes(hostname) &&
      (hostname !== "github.com" || pathname.startsWith("/user-attachments/assets/"));
    if (allowed) urls.push(url);
  }
  return urls.slice(0, MAX_IMAGES);
}

async function downloadImage(url, destinationWithoutExt) {
  const response = await fetch(url, { redirect: "follow" });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const type = (response.headers.get("content-type") || "").split(";")[0].trim();
  const ext = IMAGE_TYPES[type];
  if (!ext) throw new Error(`unsupported content type "${type}"`);
  const declared = Number(response.headers.get("content-length") || 0);
  if (declared > MAX_IMAGE_BYTES) throw new Error("image is larger than 10 MB");
  const bytes = Buffer.from(await response.arrayBuffer());
  if (bytes.length > MAX_IMAGE_BYTES) throw new Error("image is larger than 10 MB");
  const file = `${destinationWithoutExt}.${ext}`;
  fs.writeFileSync(file, bytes);
  return path.basename(file);
}

function section(title, text) {
  return text ? `## ${title}\n\n${text}\n` : "";
}

function renderSubmission(meta, form, screenshots) {
  const links = [
    meta.liveUrl ? `**Live site:** <${meta.liveUrl}>` : "**Live site:** not published",
    meta.repoUrl ? `**Repository:** <${meta.repoUrl}>` : "",
  ].filter(Boolean);
  const images = screenshots
    .map((shot, index) => `![Screenshot ${index + 1} of ${escapeCell(meta.projectName)}](${shot})`)
    .join("\n\n");
  return [
    `# ${escapeCell(meta.projectName)}`,
    "",
    `**Built by:** ${escapeCell(meta.displayName)}  `,
    `**Capstone:** ${meta.capstone}  `,
    links.join("  \n"),
    "",
    `> Submitted with the Capstone Showcase Form (issue #${meta.issueNumber}).`,
    "",
    "## Screenshots",
    "",
    images || "_No screenshots could be saved._",
    "",
    section("The problem and the user", form.problem),
    section("What the project does", form.features),
    section("How it was built", form.howBuilt),
    section("Hardest part and what was learned", form.challenge),
    section("Feedback and improvement", form.feedback),
    section("What would come next", form.nextSteps),
    section("Credits", form.credits),
    "[← Back to the showcase gallery](../../README.md)",
    "",
  ]
    .join("\n")
    .replace(/\n{3,}/g, "\n\n");
}

function rebuildGallery() {
  const rows = fs
    .readdirSync(SUBMISSIONS_DIR, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => {
      const file = path.join(SUBMISSIONS_DIR, entry.name, "submission.json");
      if (!fs.existsSync(file)) return null;
      return { folder: entry.name, ...JSON.parse(fs.readFileSync(file, "utf8")) };
    })
    .filter(Boolean)
    .sort((a, b) => a.issueNumber - b.issueNumber);

  const table = rows.length
    ? [
        "| Preview | Project | Built by | Capstone | Live site |",
        "|---|---|---|---|---|",
        ...rows.map((row) => {
          const base = `submissions/${row.folder}`;
          const preview = row.cover
            ? `<img src="${base}/${row.cover}" alt="${escapeHtml(row.projectName)} screenshot" width="160">`
            : "";
          const live = row.liveUrl ? `[Open](${row.liveUrl})` : "—";
          return `| ${preview} | [${escapeCell(row.projectName)}](${base}/README.md) | ${escapeCell(
            row.displayName
          )} | ${row.capstone} | ${live} |`;
        }),
      ].join("\n")
    : "_No submissions have been saved yet._";

  const gallery = fs.readFileSync(GALLERY_FILE, "utf8");
  const start = gallery.indexOf(GALLERY_START);
  const end = gallery.indexOf(GALLERY_END);
  if (start === -1 || end === -1 || end < start) {
    throw new Error(`Gallery markers are missing from ${GALLERY_FILE}`);
  }
  const updated = `${gallery.slice(0, start + GALLERY_START.length)}\n\n${table}\n\n${gallery.slice(end)}`;
  fs.writeFileSync(GALLERY_FILE, updated);
}

module.exports = async function saveShowcaseSubmission({ context, core }) {
  const issue = context.payload.issue;
  const form = parseIssueForm(issue.body);

  const missing = REQUIRED.filter((key) => !form[key]).map((key) => FIELDS[key]);
  if (missing.length) {
    throw new Error(`The form is missing: ${missing.join(", ")}`);
  }
  if (!CAPSTONES.includes(form.capstone)) {
    throw new Error(`Unknown capstone option "${form.capstone}"`);
  }

  const meta = {
    issueNumber: issue.number,
    displayName: oneLine(form.displayName, 40),
    projectName: oneLine(form.projectName, 80),
    capstone: form.capstone,
    liveUrl: safeHttpsUrl(form.liveUrl),
    repoUrl: safeHttpsUrl(form.repoUrl),
    cover: "",
  };

  fs.mkdirSync(SUBMISSIONS_DIR, { recursive: true });
  for (const entry of fs.readdirSync(SUBMISSIONS_DIR)) {
    if (entry.startsWith(`${issue.number}-`)) {
      fs.rmSync(path.join(SUBMISSIONS_DIR, entry), { recursive: true, force: true });
    }
  }
  const folder = `${issue.number}-${slugify(meta.projectName)}`;
  const folderPath = path.join(SUBMISSIONS_DIR, folder);
  fs.mkdirSync(folderPath, { recursive: true });

  const imageUrls = findImageUrls(form.screenshots);
  if (!imageUrls.length) {
    throw new Error("No uploaded screenshots were found in the Screenshots field");
  }
  const screenshots = [];
  for (const url of imageUrls) {
    try {
      const name = `screenshot-${screenshots.length + 1}`;
      screenshots.push(await downloadImage(url, path.join(folderPath, name)));
    } catch (error) {
      core.warning(`Could not save screenshot ${url}: ${error.message}`);
    }
  }
  if (!screenshots.length) {
    throw new Error("None of the screenshots could be downloaded");
  }
  meta.cover = screenshots[0];

  fs.writeFileSync(path.join(folderPath, "README.md"), renderSubmission(meta, form, screenshots));
  fs.writeFileSync(path.join(folderPath, "submission.json"), `${JSON.stringify(meta, null, 2)}\n`);
  rebuildGallery();

  core.setOutput("folder", `${SUBMISSIONS_DIR}/${folder}`);
  core.setOutput("screenshots", String(screenshots.length));
  core.setOutput("expected_screenshots", String(imageUrls.length));
};

module.exports.parseIssueForm = parseIssueForm;
module.exports.findImageUrls = findImageUrls;
module.exports.rebuildGallery = rebuildGallery;
module.exports.renderSubmission = renderSubmission;
