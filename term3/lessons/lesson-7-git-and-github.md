# Lesson 7 – Version Control with Git and GitHub

**Term:** 3 · Holiday self-study (week 3)  
**Time:** About 2–3 hours, split into shorter sessions  
**Audience:** Grade 10 students, Alliance Girls High School  
**Tools:** Git, a text editor, and GitHub (free)

> 🏠 **Take-home lesson:** Work through these steps on your own during the holiday. Read the
> [Holiday Self-Study Pack](../holiday-self-study.md) first.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Explain the difference between Git and GitHub.
2. Create a repository and record changes in commits.
3. Read repository history and restore an earlier file version with guidance.
4. Keep your account and repository safe without sharing passwords or private data.

## Materials

- [ ] Your capstone HTML, CSS, and JavaScript files downloaded from CodePen (**Export → Export .zip**)
- [ ] Git installed, or a browser to use GitHub's file upload and editor
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
2. Create a new repository for your capstone, for example `cybersmart-quest`.
3. Unzip your CodePen export and rename the files `index.html`, `styles.css`, and `script.js`.
   Check that `index.html` links to the CSS and JavaScript files.

If Git is installed on your computer, run these commands in your project folder:

```bash
git init
git add index.html styles.css script.js
git commit -m "Create capstone website"
git branch -M main
```

Then follow the instructions GitHub shows for **your own** repository to connect and push. Never
copy another person's access token or password. If Git is not installed, use the
[Browser-Only Alternative](#browser-only-alternative) below.

### Step 3 | Make a Useful Commit

Make one small improvement to your page, then run:

```bash
git status
git diff
git add index.html
git commit -m "Improve project introduction"
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

If Git cannot be installed, create the repository on GitHub, use **Add file → Upload files**, and use
GitHub's editor for each small change. Open the commit history and compare two versions.

## Free Practice

- [GitHub Skills: Introduction to GitHub](https://github.com/skills/introduction-to-github)
- [GitHub Docs: Getting started with Git](https://docs.github.com/en/get-started/getting-started-with-git)
- [Learn Git Branching](https://learngitbranching.js.org/)

## Facilitator Notes

- Before the holiday, demonstrate account creation and a first commit with a practice repository.
- Agree a submission route for students who cannot create GitHub accounts, such as sharing a
  downloaded project folder when school reopens.
- Use GitHub organisations or classroom tooling only if the school has approved them.
- Keep repository visibility aligned with school policy and remove personal student data before
  making a project public.
