# Lesson 7 – Version Control with Git and GitHub

**Term:** 3  
**Duration:** 90 minutes  
**Audience:** Grade 10 students, Alliance Girls High School  
**Tools:** Git, a text editor, and GitHub (free)

---

## Learning Objectives

Students will be able to:

1. Explain the difference between Git and GitHub.
2. Create a repository and record changes in commits.
3. Read repository history and restore an earlier file version with guidance.
4. Collaborate without sharing passwords or overwriting teammates' work.

## Materials

- [ ] Team HTML, CSS, and JavaScript files downloaded from CodePen
- [ ] Git installed, or access to GitHub's browser file editor
- [ ] An individual GitHub account for each student, if school policy permits
- [ ] A facilitator-owned repository as an alternative when students cannot create accounts

---

## Lesson Plan

### ⏱ 0–15 min | Connect: A Save Point for Code

Compare a commit to a labelled save point. Clarify:

- **Git** records versions on a computer.
- **GitHub** hosts Git repositories online so teams can share and review work.
- A repository is not a backup for passwords or private information.

### ⏱ 15–35 min | Guided Setup

Create a repository containing `index.html`, `styles.css`, and `script.js`. If Git is available:

```bash
git init
git add index.html styles.css script.js
git commit -m "Create capstone website"
git branch -M main
```

Connect the repository using the instructions GitHub shows for the team's own repository. Never copy
another person's access token or password.

### ⏱ 35–55 min | Make a Useful Commit

Students make one small page improvement and run:

```bash
git status
git diff
git add index.html
git commit -m "Improve project introduction"
git log --oneline
```

Discuss why commit messages should describe the completed change.

### ⏱ 55–65 min | Team Workflow

Agree on these beginner rules:

1. Pull the newest work before editing.
2. Work on one agreed task at a time.
3. Review `git diff` before committing.
4. Make small commits with clear messages.
5. Never commit passwords, private data, or API keys.
6. Ask before resolving a teammate's merge conflict.
7. Add teammates as repository collaborators; never share an account or password.

### ⏱ 65–80 min | Capstone Checkpoint

Each team creates its repository, adds the current project, and records at least two meaningful
commits. Every member locates the files and commit history on GitHub.

### ⏱ 80–90 min | Exit Ticket

Students explain repository, commit, and history, then show where they would check changed files.

## Browser-Only Alternative

If Git cannot be installed, create the repository on GitHub, use **Add file → Upload files**, and use
GitHub's editor for one small change. Show the commit history and compare two versions.

## Free Practice

- [GitHub Skills: Introduction to GitHub](https://github.com/skills/introduction-to-github)
- [GitHub Docs: Getting started with Git](https://docs.github.com/en/get-started/getting-started-with-git)
- [Learn Git Branching](https://learngitbranching.js.org/)

## Facilitator Notes

- Demonstrate with a practice repository before touching capstone work.
- Use GitHub organisations or classroom tooling only if the school has approved them.
- Keep repository visibility aligned with school policy and remove personal student data before
  making a project public.
