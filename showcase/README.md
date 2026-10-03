# Term 3 – Capstone Showcase 🎉

**Audience:** Grade 10 students, Alliance Girls High School  
**Format:** An online form submitted by each student. There is no live presentation.  
**When:** By the end of the holiday, after you finish [Lessons 5–8](../term3/lessons/README.md)

---

## How the Showcase Works

1. You build your **individual** capstone over the holiday using the
   [Holiday Self-Study Pack](../term3/holiday-self-study.md).
2. You fill in the **[Capstone Showcase Form](https://github.com/BethanyJep/HS-Software-Engineering/issues/new?template=capstone-showcase.yml)**,
   including screenshots of what you built.
3. A facilitator checks the form for personal information and approves it.
4. Your answers and screenshots are saved in this folder under `submissions/`, and your project
   appears in the gallery below.
5. Judges review every saved submission using the
   [judging criteria](../term3/project-guidelines.md#judging-criteria), and winners are announced
   when school reopens.

## Before You Fill In the Form

Have these ready:

- [ ] **Screenshot 1:** your project at **phone width**
- [ ] **Screenshot 2:** your project at **computer width**
- [ ] *(Optional)* **Screenshot 3:** your main feature in action
- [ ] Your GitHub Pages link and repository link, if you have them
- [ ] Your [learning journal](../term3/holiday-self-study.md#learning-journal) answers for Lessons 5–8
- [ ] One piece of feedback you received and the change you made

> ⚠️ This repository is **public**. Use your first name or a nickname only. Check that your
> screenshots do not show your surname, phone number, email, passwords, or photos of people.

### How to Take a Screenshot

| Device | Shortcut |
|---|---|
| Windows | **Windows + Shift + S**, then select the area |
| Mac | **Cmd + Shift + 4**, then select the area |
| Chromebook | **Ctrl + Shift + Show windows** |
| Android or iPhone | Press **Power + Volume down** (Android) or **Side button + Volume up** (iPhone) |

**Phone-width view on a computer:** open your site in Chrome or Edge, press **F12** (or
**Ctrl + Shift + I**), then click the phone-and-tablet icon (**Ctrl + Shift + M**) and choose a phone.

## Submit Your Form

1. Sign in to GitHub with the account you created in [Lesson 7](../term3/lessons/lesson-7-git-and-github.md).
2. Open the **[Capstone Showcase Form](https://github.com/BethanyJep/HS-Software-Engineering/issues/new?template=capstone-showcase.yml)**.
3. Answer every question in your own words.
4. Drag and drop your screenshot files into the **Screenshots** box and wait for them to finish uploading.
5. Tick the three checkboxes and select **Create**.

You can edit your form until a facilitator approves it. When it has been saved, you will get a
comment with a link to your gallery page.

**No GitHub account?** Write your answers using the same questions, and send them with your
screenshots to your facilitator. They can submit the form for you.

---

## Showcase Gallery

<!-- gallery:start -->

_No submissions have been saved yet._

<!-- gallery:end -->

---

## For Facilitators

### One-Time Setup

1. Create two labels in **Issues → Labels**: `showcase` (applied by the form automatically) and
   `showcase-approved`.
2. Make sure GitHub Actions is enabled for the repository. The
   [save workflow](../.github/workflows/save-showcase-submission.yml) commits to the default branch,
   so branch protection must allow `github-actions[bot]` to push.

### Reviewing a Submission

1. Open the issue and check the text **and every screenshot** for personal information.
2. Ask the student to edit the form if anything needs to change.
3. Add the `showcase-approved` label. The workflow downloads the screenshots, saves the submission to
   `showcase/submissions/<issue-number>-<project-name>/`, updates the gallery, comments, and closes
   the issue.
4. If saving fails, the workflow comments with what to fix. Remove and re-add the label to retry.

To remove a submission, delete its folder in `showcase/submissions/` and remove its row from the
gallery above.
