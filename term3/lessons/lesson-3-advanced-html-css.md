# Lesson 3 – Advanced HTML/CSS Concepts

**Term:** 3  
**Duration:** 90 minutes  
**Audience:** Grade 10 students, Alliance Girls High School  
**Tools:** Browser, CodePen, and browser developer tools

---

## Learning Objectives

Students will be able to:

1. Build layouts with Flexbox and Grid.
2. Make a page adapt to small and large screens.
3. create accessible forms with labels and helpful input types.
4. Use browser developer tools to inspect and debug a layout.

## Lesson Plan

### ⏱ 0–10 min | Connect: One Web, Many Screens

Resize a website from desktop width to phone width. Ask students to identify what moves, wraps,
shrinks, or becomes difficult to use.

### ⏱ 10–30 min | Learn: Flexible Layouts

Compare Flexbox for a row or column with Grid for a group of cards:

```css
nav ul {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  list-style: none;
  padding: 0;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
  gap: 1rem;
}

@media (max-width: 40rem) {
  header {
    text-align: center;
  }
}
```

### ⏱ 30–50 min | Guided Build: Responsive Cards and a Form

Students add a responsive card grid and a small form:

```html
<form>
  <label for="topic">Choose a topic</label>
  <select id="topic" name="topic">
    <option value="">Select one</option>
    <option value="events">Events</option>
    <option value="study">Study</option>
  </select>
  <button type="submit">Show results</button>
</form>
```

Students check keyboard navigation, visible focus, form labels, heading order, and phone layout.

### ⏱ 50–60 min | Debug with Developer Tools

Use the element inspector to:

- Toggle one CSS declaration
- Find an element's margin and padding
- Simulate a phone screen
- Fix an overflowing card or image

### ⏱ 60–80 min | Capstone Checkpoint

Teams make their page work at approximately 320 px and desktop width, then add the form or controls
their project will need. A teammate must complete the main task using only the keyboard.

### ⏱ 80–90 min | Exit Ticket

Students record one responsive change, one accessibility improvement, and one remaining layout bug.

## Free Practice

- [Flexbox Froggy](https://flexboxfroggy.com/)
- [CSS Grid Garden](https://cssgridgarden.com/)
- [MDN: Responsive design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design)
- [W3C Easy Checks](https://www.w3.org/WAI/test-evaluate/preliminary/)

## Facilitator Notes

- Treat accessibility as part of building correctly, not an optional polish step.
- Avoid fixed widths for main content and never disable browser zoom.
- Let students diagnose layout problems before showing the fix.

