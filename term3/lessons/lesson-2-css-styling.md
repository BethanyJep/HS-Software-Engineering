# Lesson 2 – Add CSS to Beautify Your Page

**Term:** 3  
**Duration:** 90 minutes  
**Audience:** Grade 10 students, Alliance Girls High School  
**Tools:** Browser and CodePen

---

## Learning Objectives

Students will be able to:

1. Explain how CSS selectors, properties, and values work.
2. Apply colour, typography, spacing, borders, and reusable classes.
3. Use contrast and consistency to improve readability.
4. Create a simple visual system for their capstone.

## Materials

- [ ] Lesson 1 page
- [ ] Projector and colour-contrast checker
- [ ] Paper or shared document for a mini style guide

---

## Lesson Plan

### ⏱ 0–10 min | Connect: Same Content, Different Feeling

Show the same HTML with and without CSS. Ask what changed and which version is easier to use.
Introduce the idea that UI designers make deliberate choices rather than adding decoration at random.

### ⏱ 10–25 min | Learn: Selectors and the Box Model

Add these styles one group at a time:

```css
:root {
  --primary: #243b7b;
  --accent: #f4b400;
  --surface: #f7f8fc;
  --text: #172033;
}

body {
  margin: 0;
  color: var(--text);
  background: var(--surface);
  font-family: Arial, sans-serif;
  line-height: 1.6;
}

header,
main,
footer {
  max-width: 64rem;
  margin-inline: auto;
  padding: 1.5rem;
}

.action {
  display: inline-block;
  padding: 0.75rem 1rem;
  color: white;
  background: var(--primary);
  border-radius: 0.5rem;
}
```

Explain element and class selectors, custom properties, margin, padding, and the box model.

### ⏱ 25–50 min | Guided Build: Style a Plain Page

Students:

1. Choose a palette with one primary colour, one accent, one surface, and one text colour.
2. Set a readable font, line height, and page width.
3. Add spacing between sections.
4. Style one link as an action button.
5. Add a card class and apply it to two related pieces of content.
6. Check that text and background colours have enough contrast.

### ⏱ 50–60 min | Design Review

Pairs use the "CRAP" checklist: **Contrast, Repetition, Alignment, Proximity**. Each student gives
one specific compliment and one suggestion.

### ⏱ 60–80 min | Capstone Checkpoint

Teams create a mini style guide and apply it consistently to the capstone:

| Choice | Team decision |
|---|---|
| Primary and accent colours | |
| Heading and body fonts | |
| Button style | |
| Card style | |
| Spacing rule | |

### ⏱ 80–90 min | Exit Ticket

Students identify one selector, one CSS property, and one design decision that improved usability.

## Free Practice

- [MDN: CSS getting started](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Getting_started)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Coolors Contrast Checker](https://coolors.co/contrast-checker)

## Facilitator Notes

- Demonstrate invalid CSS and use the browser inspector to find the problem.
- Encourage a small, consistent palette rather than many competing colours.
- Do not require a paid font, template, or design tool.

