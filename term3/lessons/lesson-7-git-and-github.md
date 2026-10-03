# Lesson 7 – Version Control with Git and GitHub

**Term:** 3 · Holiday self-study (week 3)  
**Time:** About 2–3 hours, split into shorter sessions  
**Audience:** Grade 10 students, Alliance Girls High School  
**Tools:** [Visual Studio Code](https://code.visualstudio.com/), Git, and GitHub (all free)

> 🏠 **Take-home lesson:** Work through these steps on your own during the holiday. Read the
> [Holiday Self-Study Pack](../holiday-self-study.md) first.
>
> 🖥️ **Slides:** [Open the Lesson 7 slide deck](../week-7-git-slides.html) to click through the key ideas.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Explain the difference between Git and GitHub.
2. Create a repository and record changes in commits.
3. Read repository history and restore an earlier file version with guidance.
4. Keep your account and repository safe without sharing passwords or private data.

## Materials

- [ ] Your capstone downloaded from NitroIDE (options menu → **Download ZIP**)
- [ ] [Visual Studio Code](https://code.visualstudio.com/) and [Git](https://git-scm.com/downloads) installed, or a browser to use
  GitHub's upload page and VS Code for the Web (github.dev)
- [ ] Your own free GitHub account, created with permission from a parent or guardian
- [ ] If you cannot create an account, ask your facilitator about another way to submit your files

---

## Self-Study Steps

### Step 1 | Connect: A Save Point for Code

A commit is like a labelled save point in a game. Copy these definitions into your journal:

- **Git** records versions of your files on a computer.
- **GitHub** hosts Git repositories online so you can share, review, and publish work.
- A repository is not a place for passwords or private information.

### Step 2 | Set Up Your Repository

1. Sign in to [GitHub](https://github.com/) and turn on two-factor authentication if you can.
2. Create a new **Public** repository for your capstone, for example `cybersmart-quest`. Do **not**
   tick "Add a README" — leave it empty so your first push works.
3. Unzip your NitroIDE download into a new folder and open that folder in VS Code
   (**File → Open Folder**). It contains `index.html`, `style.css`, and `script.js`.
4. In `index.html`, check that the `<head>` links `style.css`, the end of `<body>` loads
   `script.js`, and the page starts with `<html lang="en">`. Change
   `<title>Exported Project</title>` to your project name, add
   `<meta name="viewport" content="width=device-width, initial-scale=1">`, and put any permitted
   image files in an `images` folder.

If Git is installed, open the VS Code terminal (**Terminal → New Terminal**). Tell Git who you are
(once per computer). To keep your email private, use the "noreply" address from GitHub
**Settings → Emails**:

```bash
git config --global user.name "Your First Name"
git config --global user.email "you@example.com"
```

Then save your first version and push it to **your own** repository (replace `YOUR-NAME` and the
repository name):

```bash
git init
git add .
git commit -m "Create capstone website"
git branch -M main
git remote add origin https://github.com/YOUR-NAME/cybersmart-quest.git
git push -u origin main
```

If a sign-in window opens, choose **Sign in with your browser**. Never copy another person's
access token or password. If Git is not installed, use the
[Browser-Only Alternative](#browser-only-alternative) below.

### Step 3 | Make a Useful Commit

Make one small improvement to your page, then run:

```bash
git status
git diff
git add index.html
git commit -m "Improve project introduction"
git push
git log --oneline
```

A good commit message describes the completed change, such as "Add empty state to search", not
"update" or "stuff".

### Step 4 | Good Habits for Working Alone

1. Check `git status` and `git diff` before every commit.
2. Work on one task at a time.
3. Make small commits with clear messages.
4. Push at the end of every study session so your work is backed up.
5. Never commit passwords, private data, or API keys.

### Step 5 | Capstone Checkpoint

Your capstone repository must contain your current project and **at least three** meaningful
commits. For the Opportunities Hub or CyberSmart Quest, move your data into `opportunities.json` or
`questions.json` now and update your Lesson 6 code to fetch it.

> `fetch` cannot load a JSON file opened directly from your computer (`file://`). Test it in
> Lesson 8 on GitHub Pages, or keep your sample-data fallback working until then.

### Step 6 | Learning Journal

Explain repository, commit, and history in your own words. Write down where on GitHub you would
look to see which files changed in a commit.

✅ **Done when:** your capstone is in your own GitHub repository with at least three clear commits,
and your journal entry is complete.

## Browser-Only Alternative

If VS Code or Git cannot be installed, create the repository on GitHub and use **Add file → Upload
files**. Then press `.` on the repository page to open it in VS Code for the Web (github.dev). Edit
your files there and commit from the **Source Control** panel with a clear message. Open the commit
history and compare two versions.

## Free Practice

- [GitHub Skills: Introduction to GitHub](https://github.com/skills/introduction-to-github)
- [GitHub Docs: Getting started with Git](https://docs.github.com/en/get-started/getting-started-with-git)
- [Learn Git Branching](https://learngitbranching.js.org/)

## Facilitator Notes

- Before the holiday, demonstrate opening a NitroIDE ZIP in VS Code, account creation, and a first
  commit with a practice repository.
- Agree a submission route for students who cannot create GitHub accounts, such as sharing a
  downloaded project folder when school reopens.
- Use GitHub organisations or classroom tooling only if the school has approved them.
- Keep repository visibility aligned with school policy and remove personal student data before
  making a project public.
