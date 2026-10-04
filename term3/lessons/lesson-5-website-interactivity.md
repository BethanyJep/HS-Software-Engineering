# Lesson 5 – Add Interactivity to Your Website

**Term:** 3 · Holiday self-study (week 1)  
**Time:** About 2–3 hours, split into shorter sessions  
**Audience:** Grade 10 students, Alliance Girls High School  
**Tools:** Browser and [NitroIDE](https://nitroide.com/tools/codebox.html)

> 🏠 **Take-home lesson:** Work through these steps on your own during the holiday. Read the
> [Holiday Self-Study Pack](../holiday-self-study.md) first.
>
> 🖥️ **Slides:** [Open the Lesson 5 slide deck](https://bethanyjep.github.io/HS-Software-Engineering/term3/week-5-interactivity-slides.html) to click through the key ideas.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Select and update HTML elements with the DOM.
2. Respond to clicks, form submissions, and input changes.
3. Render an array of data on a page.
4. Provide clear feedback after a user action.

## Self-Study Steps

### Step 1 | Connect: Event → Action → Feedback

Think about the feedback a lift button, M-Pesa prompt, or school portal gives after you act. Write
down one example. Interfaces listen for **events**, do some **work**, and show the **result**.

### Step 2 | Learn: DOM and Events

Open [NitroIDE](https://nitroide.com/tools/codebox.html) and start a **New Project** for practice, so your capstone stays safe. Paste this
into `index.html`:

```html
<label for="search">Find a resource</label>
<input id="search" type="search">
<button id="search-button" type="button">Search</button>
<p id="status" aria-live="polite"></p>
<ul id="results"></ul>
```

Paste this into `script.js`:

```javascript
const resources = [
  { title: "Revision group" },
  { title: "Science fair" },
  { title: "Coding club" }
];
const searchInput = document.querySelector("#search");
const searchButton = document.querySelector("#search-button");
const status = document.querySelector("#status");
const results = document.querySelector("#results");

function showResults(items) {
  results.replaceChildren();

  for (const item of items) {
    const listItem = document.createElement("li");
    listItem.textContent = item.title;
    results.append(listItem);
  }

  status.textContent = `${items.length} result(s) found.`;
}

searchButton.addEventListener("click", () => {
  const query = searchInput.value.trim().toLowerCase();
  showResults(resources.filter((item) => item.title.toLowerCase().includes(query)));
});
```

Type a word and click **Search**. Then read the code line by line and find the event, the action,
and the feedback. Notice that the code uses `textContent`: it is safer for ordinary text than
inserting HTML that came from a user or another website.

### Step 3 | Practise

In the same practice project, add:

- An empty-state message such as "No resources match your search."
- A **Reset** button that clears the search box and shows every resource again
- A fourth resource in the array, to check the loop still works
- Keyboard testing: use only **Tab**, **Enter**, and **Space** to search and reset

### Step 4 | Capstone Checkpoint

Open your own capstone and connect your Lesson 4 data to the page. Build **one** core interaction:

| Capstone | Suggested interaction |
|---|---|
| School Opportunities Hub | A category filter or keyword search |
| Kenya Weather Dashboard | A location selector |
| CyberSmart Quest | Answer buttons that show an explanation |

The interaction must work with both mouse and keyboard, show a visible status message, and handle
the "nothing found" case.

### Step 5 | Home User Test

Ask a family member or friend to complete one task on your page **without** explaining how. Write
down where they hesitate, succeed, or expect different feedback. Improve one thing based on what you
saw.

### Step 6 | Learning Journal

Answer in your journal:

1. What are the event, action, and feedback in your capstone feature?
2. What did your tester find confusing, and what did you change?

✅ **Done when:** your capstone has one working interaction that gives clear feedback, and your
journal entry is complete.

## Free Practice

- [MDN: DOM scripting](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting)
- [MDN: Introduction to events](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events)

## Facilitator Notes

- Before the holiday, check that each student has a saved copy of their Lessons 1–4 capstone work.
- Keep JavaScript in `script.js` rather than inline `onclick` attributes.
- Prefer `textContent` and DOM methods for displaying user or API data.
- A smaller interaction that is clear and reliable is better than many unfinished controls.
