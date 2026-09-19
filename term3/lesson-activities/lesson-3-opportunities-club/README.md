# Opportunities Finder: sample code for Lessons 3 and 4

A small "Opportunities Club" website that ends in a working finder: students pick a topic and the cards for that topic appear. It uses the same example content as the lesson plans (Revision group, Science fair, Coding club, Design challenge). All content is fictional and no personal information is collected or stored.

```
leson-3-opportunities-club/
├── v1-simple/          cards written in HTML, advanced CSS, very small JavaScript
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   ├── debug-challenge.js     student handout for the Lesson 4 debugging block
│   ├── images/                8 card illustrations (SVG)
│   └── fonts/                 optional offline copy of the font (regular + bold) and its licence
└── v2-extended/        same HTML/CSS foundation; cards are built from a JavaScript data array
    ├── index.html
    ├── style.css              identical to v1 with a labelled block of additions at the end
    ├── app.js
    ├── images/
    └── fonts/
```

Open `index.html` in a browser to run either version (internet needed for the font). Keep the `images` folder next to it. CodePen can't see local image files, so run the project from a folder; the Google Font link would work in CodePen as is.

## What changed from the first draft

- **v1 cards are plain HTML.** JavaScript only shows or hides them. The JavaScript is now four short steps: find elements, one function with a parameter and a return value, one loop with an `if`, and one event listener. No arrays of objects, `.filter()` or arrow functions.
- **Font:** Josefin Slab, loaded with a Google Fonts `<link>` in each `index.html` (needs internet). To use a different font, pick it on fonts.google.com, paste its `<link>` lines over the existing ones, and change the name in `font-family`. For offline use, the `fonts` folder and a commented-out `@font-face` block in `style.css` are included; swap to them by deleting the `<link>` lines and un-commenting the block.
- **Images:** every card has an `<img>` with meaningful alt text and `width`/`height` attributes. The SVGs were made for this project; edit or replace them freely.

## Where each file fits in the lessons

| Lesson block | Use this |
|---|---|
| L3 Connect (0-10) | Open v1 in the browser and resize it. Ask what moves, wraps or shrinks. |
| L3 Learn: flexible layouts (10-30) | `style.css` sections 5 (Flexbox nav), 7 (Flexbox form), 8 (Grid `auto-fit` cards), and the two `@media` blocks |
| L3 Guided build (30-50) | `index.html`: landmarks, the labelled `<select>` form, one `<article class="card">` with its `<img>` and alt text. Keyboard, focus, heading order |
| L3 DevTools (50-60) | Toggle `.card-grid` columns, inspect `.card-body` padding, use the device toolbar at 320px |
| L4 Learn (10-30) | v1 `app.js` steps 1 to 3: variables, `cardMatches` (parameters and return), `showTopic` (loop and `if`). Do the lesson's array-of-objects console exercise alongside it |
| L4 Guided practice (30-50) | v1 step 4 and the "Try it yourself" list at the bottom of `app.js` |
| L4 Debugging (50-60) | `debug-challenge.js` |
| Capstone checkpoint | Teams copy a card, change the words, images and `data-category`. Stretch: move their content into an array of objects, as in v2 |
| Stretch or later week | v2, one feature at a time |

## Version 1 vs Version 2

**v1:** one dropdown and a submit button. Concepts: variables, functions with parameters and return values, `if`/`else`, `for...of`, one event listener, `data-*` attributes.

**v2:** the cards now come from an array of objects (with `image` and `imageAlt` properties), and it adds a `state` object with a single `render()` function, search plus topic plus checkboxes plus sort working together, dropdown options built from the data, saved favourites that survive a refresh (`localStorage`), event delegation, and focus management. This is where the lesson's "turn capstone information into structured data" objective lives.

## Adapting it for capstone projects

**In v1:** copy an `<article class="card">` block, change the text, image and `data-category`, and add a matching `<option value="...">` to the dropdown. Add a `.card[data-category="..."]` colour rule in `style.css` for any new category.

**In v2:** change the `resources` array and `categoryLabels`. The dropdown builds itself.

Weather (towns and sample forecasts) and CyberSmart (questions with a safer answer) both fit the same pattern.

## Debug challenge answer key (facilitators only)

| Bug | What students see | Fix |
|---|---|---|
| Missing `];` closing the array | `SyntaxError: Unexpected token 'function'` (the error points at the line *after* the real problem) | Add `];` after the last object |
| `opportunites` misspelled | `ReferenceError: opportunites is not defined` | Rename to `opportunities` |
| `item.type` should be `item.category` | **No error**, but nothing prints | Change to `item.category` |

The third bug is the useful one to discuss: not every bug announces itself. Students have to check the data with `console.log`.

## Facilitator notes

- Common typos: `event` vs `events` between the dropdown and `data-category`, and capital letters in category names.
- The "Volunteering" option in v1 has no cards on purpose, so students see the empty-state message. Adding one card fixes it.
- Ask students to write their own alt text. A good test is "if the picture vanished, would this sentence tell you what was there?"
- Try the page with keyboard only (Tab, Space, Enter) and at 200% zoom.
- Fonts are under the SIL Open Font License (licence file included in each `fonts` folder).
