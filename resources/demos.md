# Cool Demos for Sessions

This document provides step-by-step instructions for live demos that facilitators can run during sessions. Each demo is designed to **spark curiosity**, make software feel tangible, and show students that building is learnable.

---

## Quick Reference

| Demo | Session | Time | Tools | Wow Factor |
|---|---|---|---|---|
| 1. Hello World in 3 Languages | Session 1 | 5 min | CodePen | See the same idea in different web languages |
| 2. Live Chatbot / AI Response | Session 1 | 5–8 min | ChatGPT or CodePen | AI is not magic — it responds to instructions |
| 3. Scratch Interactive Story | Session 1 | 8–10 min | Scratch | Build something playable in minutes |
| 4. Build a Webpage in 5 Minutes | Session 3 | 10–15 min | Browser (any) | See code → real webpage instantly |
| 5. Colour-Changing Button (JS) | Session 3 | 5 min | CodePen | Show interactivity |
| 6. Make the Computer Speak | Any | 5 min | CodePen | Computer says your name aloud |
| 7. Draw with Code | Any | 8 min | CodePen / Scratch | Art from code |
| 8. Simple Survey Form | Session 3 | 10 min | Google Forms or HTML | Show how data is collected |
| 9. Figma Wireframe Live | Term 3 kickoff | 10 min | Figma (free) | Show design before building |
| 10. A Real App's Source Code | Any | 5 min | Browser DevTools | Demystify every website |

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

## Demo 2 – Live AI / Chatbot Response

**Best session:** Session 1  
**Time:** 5–8 minutes  
**Tools needed:** Internet browser + ChatGPT (chat.openai.com) OR a simple JavaScript chatbot on CodePen

**What it shows:** AI responds to instructions; it's not magic — it's patterns and data.

**Option A – Using ChatGPT:**
1. Open ChatGPT in the browser.
2. Type: *"Write a poem about Alliance Girls High School."*
3. Watch it respond. Then ask: *"Now write it in Kiswahili."*
4. Ask the students: *"What do you notice? What could you ask it?"*

**Option B – Simple JavaScript chatbot in CodePen:**
```html
<label for="message">Message</label>
<input id="message" placeholder="Type hi, help, or bye">
<button onclick="reply()">Send</button>
<p id="response"></p>
```
```javascript
function reply() {
  const input = document.querySelector("#message").value.toLowerCase();
  const responses = {
    hi: "Hi there! Nice to meet you.",
    help: "I can say hi and say goodbye. That's about it for now!",
    bye: "Goodbye! Have a great day."
  };
  document.querySelector("#response").textContent =
    responses[input] || "I don't understand that yet. I'm still learning!";
  document.querySelector("#message").value = "";
}
```

**What to say:**
> *"This chatbot only knows a few words. ChatGPT knows billions — but the idea is the same: it's following rules we wrote. YOU could write those rules."*

---

## Demo 3 – Scratch Interactive Story / Mini Game

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

## Demo 4 – Build a "Hello, Me!" Webpage in 5 Minutes

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

## Demo 5 – Colour-Changing Button (JavaScript)

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

## Demo 6 – Make the Computer Speak Your Name

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
  speechSynthesis.speak(
    new SpeechSynthesisUtterance("Hello Alliance Girls!")
  );
}
```

**What to say:**
> *"Every smart assistant — Siri, Google Assistant, Alexa — runs code like this. You just made a computer speak. In one line."*

---

## Demo 7 – Draw with Code (JavaScript Canvas)

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

for (let i = 0; i < 360; i++) {
  context.strokeStyle = colors[i % colors.length];
  context.lineWidth = i / 100 + 1;
  context.beginPath();
  context.moveTo(x, y);
  x += Math.cos(i) * i / 10;
  y += Math.sin(i) * i / 10;
  context.lineTo(x, y);
  context.stroke();
}
```

**What to say:**
> *"Math + code = art. This spiral comes entirely from a loop and some geometry. Technology and creativity are not opposites."*

---

## Demo 8 – Simple Survey Form (HTML or Google Forms)

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

## Demo 9 – Figma Wireframe Live

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

## Demo 10 – Peek Behind Any Website (Browser DevTools)

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
