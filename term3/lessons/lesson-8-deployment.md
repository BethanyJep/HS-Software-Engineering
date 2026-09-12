# Lesson 8 – Deploy Your Web Application

**Term:** 3  
**Duration:** 90 minutes  
**Audience:** Grade 10 students, Alliance Girls High School  
**Tools:** Browser, GitHub, and GitHub Pages (free)

---

## Learning Objectives

Students will be able to:

1. Explain the difference between local files, a repository, and a deployed site.
2. Prepare a web project for deployment.
3. Publish a site with GitHub Pages.
4. Test the public site and document a release.

## Lesson Plan

### ⏱ 0–15 min | Connect: From Your Computer to the World

Draw the release journey:

```text
Edit → Test → Commit → Push → Deploy → Test again
```

Explain that deployment is how Cloud and DevOps teams make software available to users.

### ⏱ 15–30 min | Pre-Deployment Check

Teams verify:

- The home page is named `index.html`.
- File names match links exactly, including capital letters.
- Links and images use relative paths.
- There are no passwords, keys, private details, or unlicensed images.
- The main task works with a keyboard and at phone width.
- Loading, empty, and error states are understandable.

### ⏱ 30–50 min | Publish with GitHub Pages

In the project repository:

1. Open **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select the `main` branch and `/ (root)` folder, then save.
4. Wait for GitHub to provide the public URL.
5. Open the URL in a new private/incognito window.

> GitHub's interface can change. If these labels differ, use the current
> [GitHub Pages quickstart](https://docs.github.com/en/pages/quickstart).

### ⏱ 50–65 min | Deployment Debugging

If the site fails, teams check:

1. Is Pages enabled for the correct branch and folder?
2. Is `index.html` at that location?
3. Do the browser console and Network panel show errors?
4. Do file-name capital letters match?
5. Has the latest change been committed and pushed?

### ⏱ 65–80 min | Capstone Release Check

Another team tests the public URL using this release checklist:

- [ ] The page loads without a sign-in.
- [ ] The purpose and main action are clear.
- [ ] Navigation and interactions work.
- [ ] The layout works on a phone.
- [ ] API failure does not break the whole page.
- [ ] No private information is visible.
- [ ] The footer credits the team and any permitted external content.

The project team fixes one issue, commits it, and verifies the update online.

### ⏱ 80–90 min | Celebrate and Reflect

Each team shares its URL and completes:

- One feature we are proud of
- One deployment problem we solved
- One final improvement before the showcase

## Free Practice

- [GitHub Pages quickstart](https://docs.github.com/en/pages/quickstart)
- [MDN: Publishing your website](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Publishing_your_website)

## Facilitator Notes

- Confirm public repositories and public student work comply with school policy.
- A team may demonstrate locally if publishing is not approved; learning the release checklist still
  meets the lesson goal.
- Keep screenshots or a short recording as a showcase backup.

