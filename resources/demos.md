# Cool Demos for Sessions

This document provides step-by-step instructions for live demos that facilitators can run during sessions. Each demo is designed to **spark curiosity**, make software feel tangible, and show students that building is learnable.

---

## Quick Reference

| Demo | Session | Time | Tools | Wow Factor |
|---|---|---|---|---|
| 1. Hello World in 3 Languages | Session 1 | 5 min | CodePen | See the same idea in different web languages |
| 2. Add a Button | Session 1 | 5 min | CodePen | Turn a click into a response |
| 3. Update Page Colours | Session 1 | 5 min | CodePen | See styles change with JavaScript |
| 4. Show and Hide a Message | Session 1 | 5 min | CodePen | Build a simple interactive control |
| 5. Scratch Interactive Story | Session 1 | 8–10 min | Scratch | Build something playable in minutes |
| 6. Build a Webpage in 5 Minutes | Session 3 | 10–15 min | Browser (any) | See code → real webpage instantly |
| 7. Colour-Changing Button (JS) | Session 3 | 5 min | CodePen | Show interactivity |
| 8. Make the Computer Speak | Any | 5 min | CodePen | Computer says your name aloud |
| 9. Draw with Code | Any | 8 min | CodePen / Scratch | Art from code |
| 10. Simple Survey Form | Session 3 | 10 min | Google Forms or HTML | Show how data is collected |
| 11. Figma Wireframe Live | Term 3 kickoff | 10 min | Figma (free) | Show design before building |
| 12. A Real App's Source Code | Any | 5 min | Browser DevTools | Demystify every website |

---

## Demo 1 – Hello World in 3 Languages

**Best session:** Session 1  
**Time:** 5 minutes  
**Tools needed:** CodePen (codepen.io, open in the browser without creating an account)

**What it shows:** The same idea can be expressed in different programming "languages" — just like you can say "hello" in Swahili, English, or French.

**Steps:**
1. Open `codepen.io/pen` and use the HTML, CSS, and JS panels.
2. Type and run:
   ```html
   <h1>Hello, Alliance Girls!</h1>
   ```
3. In the CSS panel, type:
   ```css
   h1 { color: darkblue; }
   ```
4. In the JS panel, type and run:
   ```javascript
   console.log("Hello, Alliance Girls!");
   ```

**What to say:**
> *"Three different languages, same result. Learning one makes learning others much easier — the logic is the same, only the spelling changes."*

---

## Demo 2 – Add a Button

**Best session:** Session 1  
**Time:** 5 minutes  
**Tools needed:** CodePen (codepen.io, open in the browser without creating an account)

**What it builds:** A button that updates a message when someone clicks it.

Add this to the HTML panel:
```html
<h2>Make something happen</h2>
<button id="welcome-button" type="button">Say hello</button>
<p id="welcome-message" aria-live="polite"></p>
```

Add this to the JavaScript panel:
```javascript
const button = document.querySelector("#welcome-button");
const message = document.querySelector("#welcome-message");

button.addEventListener("click", () => {
  message.textContent = "You made the page respond!";
});
```

**What to say:**
> *"The button is the control, the click is the event, and the message is the result. Interfaces are built from small interactions like this."*

---

## Demo 3 – Update Page Colours

**Best session:** Session 1  
**Time:** 5 minutes  
**Tools needed:** CodePen (codepen.io, open in the browser without creating an account)

**What it builds:** A colour picker that updates the page without reloading it.

Add this to the HTML panel:
```html
<label for="theme">Choose a page colour:</label>
<select id="theme">
  <option value="#f7f3ea">Cream</option>
  <option value="#dce6ff">Blue</option>
  <option value="#f9d6e3">Pink</option>
</select>
<p id="colour-message">The page can change while it is running.</p>
```

Add this to the JavaScript panel:
```javascript
const themePicker = document.querySelector("#theme");
const colourMessage = document.querySelector("#colour-message");

themePicker.addEventListener("change", () => {
  document.body.style.backgroundColor = themePicker.value;
  colourMessage.textContent = `The page is now ${themePicker.value}.`;
});
```

**What to say:**
> *"CSS gives the page its starting style. JavaScript can update that style when a person makes a choice."*

---

## Demo 4 – Show and Hide a Message

**Best session:** Session 1  
**Time:** 5 minutes  
**Tools needed:** CodePen (codepen.io, open in the browser without creating an account)

**What it builds:** A toggle button that reveals or hides extra information.

Add this to the HTML panel:
```html
<button id="details-button" type="button" aria-expanded="false">
  Show details
</button>
<p id="details" hidden>Well done — you built a reusable interface pattern!</p>
```

Add this to the JavaScript panel:
```javascript
const detailsButton = document.querySelector("#details-button");
const details = document.querySelector("#details");

detailsButton.addEventListener("click", () => {
  const isHidden = details.hidden;
  details.hidden = !isHidden;
  detailsButton.setAttribute("aria-expanded", String(isHidden));
  detailsButton.textContent = isHidden ? "Hide details" : "Show details";
});
```

**What to say:**
> *"Good interfaces give people control over what they see. The same show-and-hide pattern appears in menus, FAQs, and settings screens."*

---

## Demo 5 – Scratch Interactive Story / Mini Game

**Best session:** Session 1 (for a visual, beginner-friendly wow moment)  
**Time:** 8–10 minutes  
**Tools needed:** scratch.mit.edu (or Scratch offline editor)

**What it builds:** A character that responds when you click it — moves, changes costume, plays sound, says a message.

**Steps:**
1. Open Scratch, start a new project.
2. Click the cat sprite → go to "Events" → drag `when this sprite clicked` onto the canvas.
3. Add `say [Hello! I'm a software engineer!] for [2] seconds`.
4. Add `change x by [50]` (makes the cat move right).
5. Add `play sound [meow]`.
6. Click the cat on stage — it responds!

**Extend it (if time allows):**
- Add a second sprite (backdrop character) that responds differently.
- Add a score counter.
- Let a student come up and add their own block!

**What to say:**
> *"This is drag-and-drop, but the logic is identical to what professional developers write. Events → Actions. That's all programming is."*

---

## Demo 6 – Build a "Hello, Me!" Webpage in 5 Minutes

**Best session:** Session 3 (students follow along on their own devices)  
**Time:** 10–15 minutes  
**Tools needed:** CodePen (codepen.io, open in the browser without creating an account)

**What it builds:** A personal mini-webpage with a heading, a paragraph, and a background colour.

**Code to type together:**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
    <style>
      body {
        background-color: lightblue;
        font-family: Arial, sans-serif;
        text-align: center;
      }
      h1 {
        color: darkblue;
      }
    </style>
  </head>
  <body>
    <h1>Hi, I'm [Your Name]!</h1>
    <p>I am a student at Alliance Girls High School.</p>
    <p>One day I want to build: [your dream project].</p>
  </body>
</html>
```

**Interactive moment:** Ask students to change:
- The background colour to their favourite colour
- The `<h1>` text to their own name
- The `<p>` text to something true about them

**What to say:**
> *"You just built a webpage. Right now. This is exactly how every website on the internet started — someone typed code like this."*

---

## Demo 7 – Colour-Changing Button (JavaScript)

**Best session:** Session 3 (to show interactivity)  
**Time:** 5 minutes  
**Tools needed:** CodePen (codepen.io, open in the browser without creating an account)

**What it builds:** A button that changes the page's background colour when clicked.

```html
<!DOCTYPE html>
<html>
<body>
  <h2>Click the button!</h2>
  <button onclick="changeColor()">Change Colour</button>

  <script>
    function changeColor() {
      const colors = ["lightpink", "lightyellow", "lightgreen", "lavender", "peachpuff"];
      const random = Math.floor(Math.random() * colors.length);
      document.body.style.backgroundColor = colors[random];
    }
  </script>
</body>
</html>
```

**What to say:**
> *"Three languages working together: HTML is the structure, CSS is the style, JavaScript is the behaviour. That's how every website works."*

---

## Demo 8 – Make the Computer Speak Your Name

**Best session:** Any (very quick crowd-pleaser)  
**Time:** 5 minutes  
**Tools needed:** CodePen (codepen.io, open in the browser without creating an account)

**CodePen JavaScript (no install needed):**
Add a button to the HTML panel:
```html
<button onclick="speak()">Make the computer speak</button>
```
Then add this to the JS panel:
```javascript
function speak() {
  if (!("speechSynthesis" in window)) {
    alert("Speech is not supported in this browser.");
    return;
  }
  speechSynthesis.speak(
    new SpeechSynthesisUtterance("Hello Alliance Girls!")
  );
}
```

**What to say:**
> *"Every smart assistant — Siri, Google Assistant, Alexa — runs code like this. You just made a computer speak. In one line."*

---

## Demo 9 – Draw with Code (JavaScript Canvas)

**Best session:** Any (visually satisfying, great for creative students)  
**Time:** 8 minutes  
**Tools needed:** CodePen (codepen.io, open in the browser without creating an account)

**What it builds:** A colourful spiral drawn by code.

```html
<canvas id="canvas" width="500" height="400"></canvas>
```
```javascript
const canvas = document.querySelector("#canvas");
const context = canvas.getContext("2d");
const colors = ["red", "orange", "yellow", "green", "blue", "purple"];
let x = 250;
let y = 200;
// A larger spacing spreads the spiral out; a smaller one makes it tighter.
const spiralSpacing = 10;

// 360 steps make one full turn while the radius grows.
for (let i = 0; i < 360; i++) {
  context.strokeStyle = colors[i % colors.length];
  context.lineWidth = i / 100 + 1;
  context.beginPath();
  context.moveTo(x, y);
  // Increasing each step while changing the angle (in radians) creates a spiral.
  const angle = i * Math.PI / 180;
  x += Math.cos(angle) * i / spiralSpacing;
  y += Math.sin(angle) * i / spiralSpacing;
  context.lineTo(x, y);
  context.stroke();
}
```

**What to say:**
> *"Math + code = art. This spiral comes entirely from a loop and some geometry. Technology and creativity are not opposites."*

---

## Demo 10 – Simple Survey Form (HTML or Google Forms)

**Best session:** Session 3 (links well to project building)  
**Time:** 10 minutes  
**Tools needed:** Browser (Google Forms OR basic HTML)

**What it shows:** How data is collected from users — a key part of most software.

**Option A – Google Forms:** Create a 3-question form live in front of the class. Fill it in. Show the Responses tab updating in real time.

**Option B – HTML form:**
```html
<form>
  <label>What is your name?</label><br>
  <input type="text" name="name"><br><br>

  <label>What subject do you love most?</label><br>
  <select name="subject">
    <option>Mathematics</option>
    <option>English</option>
    <option>Biology</option>
    <option>Computer Studies</option>
  </select><br><br>

  <input type="submit" value="Submit">
</form>
```

**What to say:**
> *"Every time you fill in a form on the internet, this is what's happening behind the scenes. Your project might need a form like this."*

---

## Demo 11 – Figma Wireframe Live

**Best session:** Term 3 kickoff / Session 3  
**Time:** 10 minutes  
**Tools needed:** Figma (figma.com — free account)

**What it shows:** You can design an app without writing a single line of code first. Always design before you build.

**Steps:**
1. Create a new Figma frame (Phone — iPhone 14 size).
2. Draw a rectangle as the background.
3. Add a heading text: "MyApp".
4. Add two buttons (rectangles with text): "Sign Up" and "Log In".
5. Show the "Prototype" tab → connect buttons to new screens → click "Play" to run the prototype.

**What to say:**
> *"Designers do this before developers write a single line of code. It lets you test your idea cheaply — and saves weeks of wasted work."*

---

## Demo 12 – Peek Behind Any Website (Browser DevTools)

**Best session:** Any (great as a "magic trick" moment)  
**Time:** 5 minutes  
**Tools needed:** Any browser with any website open

**What it shows:** Every website's code is visible — nothing is a black box.

**Steps:**
1. Open any website (try google.com or the school's website if one exists).
2. Right-click → "Inspect" (or press F12).
3. Show the HTML panel — hover over elements to see them highlight on the page.
4. Double-click a heading text and type something else — show it change on screen.
5. Close DevTools and refresh — show it goes back to normal.

**What to say:**
> *"This is how developers explore and learn — by looking at what others have built. Everything you see on the internet was built by a person, and you can look at how they did it."*

---

## General Demo Tips for Facilitators

- **Test every demo before the session.** Networks fail; libraries don't install; websites block things.
- **Narrate as you type.** Don't just show — explain what you're doing and why.
- **Make deliberate mistakes.** When something breaks, say: *"Ah — this is debugging. It happens to every developer, every day."*
- **Let students drive.** Ask: *"What should I change here?"* or invite a student to the keyboard.
- **Keep it short.** A 5-minute demo that works is better than a 15-minute demo that falls apart.
- **Have a fallback.** If live code fails, have a screen recording or screenshot as backup.
