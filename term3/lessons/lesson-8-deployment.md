# Lesson 8 – Deploy Your Web Application

**Term:** 3 · Holiday self-study (week 4)  
**Time:** About 2–3 hours, split into shorter sessions  
**Audience:** Grade 10 students, Alliance Girls High School  
**Tools:** Browser, GitHub, and GitHub Pages (free)

> 🏠 **Take-home lesson:** Work through these steps on your own during the holiday. Read the
> [Holiday Self-Study Pack](../holiday-self-study.md) first.
>
> 🖥️ **Slides:** [Open the Lesson 8 slide deck](../week-8-deployment-slides.html) to click through the key ideas.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Explain the difference between local files, a repository, and a deployed site.
2. Prepare a web project for deployment.
3. Publish a site with GitHub Pages.
4. Test the public site and document a release.

## Self-Study Steps

### Step 1 | Connect: From Your Computer to the World

Copy the release journey into your journal:

```text
Edit → Test → Commit → Push → Deploy → Test again
```

Deployment is how Cloud and DevOps engineers make software available to users.

### Step 2 | Pre-Deployment Check

Check that:

- [ ] The home page is named `index.html`.
- [ ] File names match links exactly, including capital letters.
- [ ] Links and images use relative paths.
- [ ] There are no passwords, keys, private details, or unlicensed images.
- [ ] The main task works with a keyboard and at phone width.
- [ ] Loading, empty, and error states are understandable.

### Step 3 | Publish with GitHub Pages

In your capstone repository:

1. Open **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select the `main` branch and `/ (root)` folder, then save.
4. Wait a few minutes for GitHub to provide the public URL.
5. Open the URL in a new private/incognito window.

> GitHub's interface can change. If these labels differ, use the current
> [GitHub Pages quickstart](https://docs.github.com/en/pages/quickstart).

### Step 4 | Deployment Debugging

If the site fails, check:

1. Is Pages enabled for the correct branch and folder?
2. Is `index.html` at that location?
3. Do the browser console and Network panel show errors?
4. Do file-name capital letters match?
5. Has the latest change been committed and pushed?

### Step 5 | Capstone Release Check

Send your public URL to a family member or friend and ask them to try it on their phone. Together,
complete this release checklist:

- [ ] The page loads without a sign-in.
- [ ] The purpose and main action are clear.
- [ ] Navigation and interactions work.
- [ ] The layout works on a phone.
- [ ] API failure does not break the whole page.
- [ ] No private information is visible.
- [ ] The footer credits you and any permitted external content.

Fix one issue they found, commit it, and check that the update appears online.

### Step 6 | Learning Journal and Showcase Form

Write down:

- One feature you are proud of
- One deployment problem you solved
- One final improvement before the showcase

Then add a short `README.md` to your repository that explains your project and credits any data,
learning resources, and images.

Finally, take at least two screenshots (phone width and computer width) and submit the
[Capstone Showcase Form](../../showcase/README.md). This form **is** your showcase: there is no live
presentation.

✅ **Done when:** your capstone is live (or saved locally), tested by someone else, and submitted with
the Capstone Showcase Form, including screenshots.

## Free Practice

- [GitHub Pages quickstart](https://docs.github.com/en/pages/quickstart)
- [MDN: Publishing your website](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Publishing_your_website)

## Facilitator Notes

- Confirm public repositories and public student work comply with school policy.
- If publishing is not approved, a student can submit screenshots of the site running locally;
  completing the release checklist still meets the lesson goal.
- Review each Capstone Showcase Form for personal information before adding the
  `showcase-approved` label (see the [showcase guide](../../showcase/README.md#for-facilitators)).

