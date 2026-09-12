# Lesson 1 – Create a Landing Page with HTML

**Term:** 3  
**Duration:** 90 minutes  
**Audience:** Grade 10 students, Alliance Girls High School  
**Tools:** Browser and [CodePen](https://codepen.io/pen) (free; no account required)

---

## Learning Objectives

By the end of this lesson, students will be able to:

1. Explain how HTML gives a web page structure.
2. Use headings, paragraphs, links, images, lists, and sections.
3. Add useful alternative text to an image.
4. Build the first version of their capstone landing page.

## Materials

- [ ] One computer per student or pair
- [ ] Projector and facilitator example
- [ ] Capstone option selected from [Project Ideas](../project-ideas.md)
- [ ] Offline text editor as a backup

---

## Lesson Plan

### ⏱ 0–10 min | Connect: What Is a Landing Page?

Open a familiar website and ask students to identify its title, navigation, main message, sections,
images, and action button. Explain that HTML describes each part's meaning.

### ⏱ 10–25 min | Learn: HTML Building Blocks

Introduce the document structure and semantic elements:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Project name</title>
  </head>
  <body>
    <header>
      <h1>Project name</h1>
      <p>A short explanation of who this project helps.</p>
    </header>
    <main>
      <section>
        <h2>How it helps</h2>
        <p>Describe the project's main benefit.</p>
      </section>
    </main>
    <footer>Built by Team Name</footer>
  </body>
</html>
```

Discuss nesting, opening and closing tags, indentation, and why there should be one clear `h1`.

### ⏱ 25–50 min | Guided Build

Students create a small school club landing page containing:

- A header with a title and introduction
- Navigation links to two page sections
- A main section with a heading, paragraph, and list
- An image with meaningful `alt` text
- A link or button inviting the visitor to act
- A footer

Pause after each element so pairs can compare their output and fix missing closing tags.

### ⏱ 50–60 min | Check and Improve

Students exchange seats and answer:

1. Can I tell what this page is for in five seconds?
2. Are the headings in a logical order?
3. Does every image have useful alternative text?
4. Do all links work?

### ⏱ 60–80 min | Capstone Checkpoint

Teams replace the practice content with their capstone content. By the end, each project should
have a header, navigation, at least three meaningful sections, and a footer.

### ⏱ 80–90 min | Share and Exit Ticket

Invite two teams to show their page. Students submit:

- One HTML element they can now explain
- One improvement they made after peer feedback
- One question for the next lesson

## Free Practice

- [MDN: Getting started with HTML](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax)
- [freeCodeCamp: Responsive Web Design](https://www.freecodecamp.org/learn/2022/responsive-web-design/)
- [W3Schools HTML Tutorial](https://www.w3schools.com/html/)

## Facilitator Notes

- Focus on meaningful structure rather than memorising every tag.
- Use only images students created or have permission to reuse.
- If internet access fails, students can write the same HTML in a text editor and open it locally.

