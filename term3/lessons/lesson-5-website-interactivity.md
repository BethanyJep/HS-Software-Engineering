# Lesson 5 – Add Interactivity to Your Website

**Term:** 3  
**Duration:** 90 minutes  
**Audience:** Grade 10 students, Alliance Girls High School  
**Tools:** Browser and CodePen

---

## Learning Objectives

Students will be able to:

1. Select and update HTML elements with the DOM.
2. Respond to clicks, form submissions, and input changes.
3. Render an array of data on a page.
4. Provide clear feedback after a user action.

## Lesson Plan

### ⏱ 0–10 min | Connect: Event → Action → Feedback

Ask students what feedback a lift button, M-Pesa prompt, or school portal gives after an action.
Explain that interfaces listen for events, do work, and show the result.

### ⏱ 10–30 min | Learn: DOM and Events

```html
<label for="search">Find a resource</label>
<input id="search" type="search">
<button id="search-button" type="button">Search</button>
<p id="status" aria-live="polite"></p>
<ul id="results"></ul>
```

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

Discuss why `textContent` is safer for ordinary text than inserting untrusted HTML.

### ⏱ 30–55 min | Guided Build

Students connect Lesson 4's data to their page, then add:

- A working search, filter, quiz answer, or reveal button
- An empty-state message
- A reset action
- A visible status message
- Keyboard testing

### ⏱ 55–65 min | User Test

One teammate gives another a task without explaining the interface. The observer records where the
tester hesitates, succeeds, or expects different feedback.

### ⏱ 65–80 min | Capstone Checkpoint

Teams complete one core interaction for their chosen capstone and improve it using the test notes.
The interaction must work with both mouse and keyboard.

### ⏱ 80–90 min | Exit Ticket

Students identify the event, action, and feedback in their capstone feature.

## Free Practice

- [MDN: DOM scripting](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting)
- [MDN: Introduction to events](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events)

## Facilitator Notes

- Keep JavaScript in the JavaScript panel or a separate file rather than inline `onclick` attributes.
- Prefer `textContent` and DOM methods for displaying user or API data.
- A smaller interaction that is clear and reliable is better than many unfinished controls.
