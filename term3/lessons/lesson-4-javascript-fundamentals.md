# Lesson 4 – JavaScript Functions, Loops, and More

**Term:** 3  
**Duration:** 90 minutes  
**Audience:** Grade 10 students, Alliance Girls High School  
**Tools:** Browser, CodePen, and browser console

---

## Learning Objectives

Students will be able to:

1. Store values in variables and arrays.
2. Write and call a function with a parameter and return value.
3. Use conditions and loops to make decisions and repeat work.
4. Turn capstone information into structured JavaScript data.

## Lesson Plan

### ⏱ 0–10 min | Connect: Give the Computer a Recipe

Ask students to write instructions for making tea. Use missing or vague steps to show that a function
needs clear inputs, actions, and an output.

### ⏱ 10–30 min | Learn: Data, Decisions, and Functions

Build this in the console:

```javascript
const resources = [
  { title: "Revision group", category: "study", featured: true },
  { title: "Science fair", category: "event", featured: false },
  { title: "Coding club", category: "event", featured: true }
];

function getFeatured(items) {
  return items.filter((item) => item.featured);
}

for (const resource of getFeatured(resources)) {
  console.log(resource.title);
}
```

Trace each line together. Explain strings, booleans, objects, arrays, parameters, return values,
conditions, and loops.

### ⏱ 30–50 min | Guided Practice

Students:

1. Add two objects to the array.
2. Write a function that returns items in a chosen category.
3. Loop through the results and print each title.
4. Add an `if` statement that prints a helpful message when no items match.
5. Predict each output before running the code.

### ⏱ 50–60 min | Debugging Challenge

Give pairs code with a misspelled variable, missing bracket, and incorrect property name. Students
read the console error, find the line, make one change, and rerun.

### ⏱ 60–80 min | Capstone Checkpoint

Teams create an array of at least six objects for their project. Each object should use the same
properties. They then write one reusable function that selects, scores, or transforms that data.

### ⏱ 80–90 min | Exit Ticket

Students explain, in their own words, when they would use an array, a function, and a loop.

## Free Practice

- [MDN: JavaScript first steps](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/A_first_splash)
- [freeCodeCamp: JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/)
- [JavaScript.info fundamentals](https://javascript.info/first-steps)

## Facilitator Notes

- Ask students to predict output before pressing Run.
- Keep data fictional and avoid storing student names or other personal information.
- Use console errors as clues; do not solve every bug for the class immediately.

