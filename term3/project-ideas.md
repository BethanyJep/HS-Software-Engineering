# Term 3 – Capstone Project Options

**Audience:** Grade 10 students, Alliance Girls High School  
**Format:** Teams of 3–5 students choose one of the three projects below  
**Cost:** Each option can be completed with free tools

---

## Choose One Capstone

Instead of inventing a project idea, each team selects one of these three shared briefs. Teams can
choose their own name, content, colours, and features, but they should solve the stated problem and
complete the common requirements.

| Option | Main career paths | Suggested free tools |
|---|---|---|
| [1. School Opportunities Hub](#option-1--school-opportunities-hub) | Web Development, UI/UX Design, Quality Assurance | CodePen, Figma or paper, GitHub Pages |
| [2. Kenya Climate & Water Dashboard](#option-2--kenya-climate--water-dashboard) | Data Analysis, Web Development, Cloud & DevOps | CodePen, Open-Meteo, GitHub Pages |
| [3. CyberSmart Quest](#option-3--cybersmart-quest) | Cybersecurity, Game Development, Quality Assurance | CodePen, MDN, GitHub Pages |

> Every project needs developers, designers, testers, and presenters. Rotate roles so each team member
> tries more than one career skill.

## Requirements for Every Project

By the showcase, every capstone must include:

- [ ] A semantic HTML landing page with clear headings, navigation, and a footer
- [ ] Consistent CSS and a layout that works on phones and computers
- [ ] Readable colour contrast, image alternative text, labelled controls, and keyboard access
- [ ] JavaScript data, at least one reusable function, a condition, and a loop
- [ ] One meaningful interaction with clear user feedback
- [ ] Data loaded with `fetch`, from a suitable public API or a team-created JSON file
- [ ] Loading, empty, and error states for fetched data
- [ ] A GitHub repository with clear commits from the team
- [ ] A tested GitHub Pages deployment, or a local demonstration if school policy prevents publishing
- [ ] A short `README` crediting data, learning resources, and permitted images

---

## Option 1 – School Opportunities Hub

### The Brief

Students often hear about clubs, competitions, scholarships, events, and study opportunities too
late or through scattered messages. Build one accessible place where a student can discover and
filter useful opportunities.

### Target User

A secondary-school student who wants to find a relevant opportunity quickly on a phone or shared
computer.

### Minimum Viable Product

- A welcoming landing section explaining the hub
- At least eight fictional or facilitator-approved opportunity cards
- A category filter or keyword search
- A details view or show/hide section for each opportunity
- A clear empty state when no opportunities match
- Opportunity data fetched from a team-created `opportunities.json` file

### Career Connections

- **Web Developer:** builds the page, data rendering, and filters
- **UI/UX Designer:** organises information and tests whether students can find an opportunity
- **QA Tester:** checks links, filters, keyboard use, and different screen sizes

### Safe Data Rules

Use fictional entries or public information approved by a facilitator. Do not publish student names,
phone numbers, personal email addresses, private schedules, or application details without permission.

### Stretch Goals

- Add bookmarks stored only in the user's browser
- Sort by date or category
- Add a "closing soon" label
- Include a print-friendly view

### Success Looks Like

A first-time visitor can find one relevant opportunity, understand its next step, and use the page
on a phone without asking the team for help.

---

## Option 2 – Kenya Climate & Water Dashboard

### The Brief

Weather and climate information can be difficult to interpret. Build a simple dashboard that helps
students compare current conditions in selected Kenyan locations and explains one practical action,
such as preparing for heat or conserving water.

### Target User

A student, teacher, or community member who wants a clear summary rather than a page of raw numbers.

### Minimum Viable Product

- A landing section explaining what the dashboard can and cannot tell users
- A selector with at least three facilitator-approved locations and their coordinates
- Current temperature fetched from the free, no-key
  [Open-Meteo API](https://open-meteo.com/en/docs)
- A clear loading state, last-updated value, and friendly error state
- A visual comparison using accessible HTML/CSS bars, cards, or a table
- A short plain-language explanation of the displayed data

### Career Connections

- **Data Analyst:** checks units, compares values, and writes an accurate data story
- **Web Developer:** fetches and displays the API response
- **UI/UX Designer:** makes the dashboard understandable and accessible
- **Cloud/DevOps Engineer:** deploys the site and checks that its live data remains reliable

### Responsible Data Rules

Credit Open-Meteo, show units, and never present a classroom project as an emergency warning service.
Do not collect a visitor's precise location; use the team's fixed list of approximate city coordinates.

### Stretch Goals

- Show one additional weather measurement
- Compare today's reading with a short forecast
- Add Celsius explanations or a simple legend
- Cache the last successful result as a fallback

### Success Looks Like

A visitor can choose a location, understand the result and its units, and still receives a useful
message if the API or internet is unavailable.

---

## Option 3 – CyberSmart Quest

### The Brief

Phishing, weak passwords, and unsafe sharing put students at risk online. Build a short, game-like
learning experience that lets students practise making safer choices without using any real private
information.

### Target User

A secondary-school student learning how to recognise common online risks and respond safely.

### Minimum Viable Product

- A landing section explaining the quest and its safety purpose
- At least eight original scenario questions stored as structured data
- Answer buttons with immediate explanations, not only "right" or "wrong"
- A score or progress indicator created with functions and loops
- A restart action and a final screen with three practical safety habits
- Questions fetched from a team-created `questions.json` file

### Career Connections

- **Cybersecurity Specialist:** researches accurate, defensive safety guidance
- **Game Developer:** creates rules, progress, feedback, and a satisfying finish
- **Web Developer:** builds the interface and JavaScript logic
- **QA Tester:** tries unexpected actions and checks scoring, accessibility, and explanations

### Safety Rules

Use invented examples and placeholder passwords only. Never collect real passwords, private messages,
account details, or names. Do not test attacks on any account, device, website, or network.

### Stretch Goals

- Add difficulty levels or topic categories
- Let the player review missed questions
- Save only a high score in the browser
- Add a timer that can be paused or disabled

### Success Looks Like

A player can finish the quest, understand why each answer is safe or unsafe, and name three actions
they can take to protect an account.

---

## Team Selection Activity

1. Read all three briefs.
2. Each team member privately ranks the options from 1 to 3.
3. Discuss the rankings and select one option the whole team can support.
4. Write one sentence explaining why that option matters to your target user.
5. Complete the [Project Kickoff Form](project-guidelines.md#appendix-a--project-kickoff-form).

Do not add stretch goals until the minimum viable product works.

