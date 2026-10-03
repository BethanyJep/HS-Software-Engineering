"""Generate the one-page end-of-program student feedback form (PDF).

Usage (from the repository root):

    pip install reportlab
    python resources/feedback/generate_feedback_form.py

The PDF is written next to this script as ``student-feedback-form.pdf``.

The form is designed to be printed and filled in by hand: every answer box and
writing line is drawn on the page itself. Invisible form fields sit on top of
them so the same PDF can also be completed on screen.

Edit the question lists below and re-run the script to update the form. The
script stops with an error if the content no longer fits on a single page.
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

OUTPUT = Path(__file__).with_name("student-feedback-form.pdf")

PAGE_W, PAGE_H = A4
MARGIN = 32
GUTTER = 16
BOTTOM = 34
CONTENT_W = PAGE_W - 2 * MARGIN
HALF_W = (CONTENT_W - GUTTER) / 2

NAVY = colors.HexColor("#0b1022")
BLUE = colors.HexColor("#315ee7")
PINK = colors.HexColor("#ed6a9a")
GOLD = colors.HexColor("#f5c95f")
GREEN = colors.HexColor("#72c4a7")
CREAM = colors.HexColor("#f8f4ea")
GREY = colors.HexColor("#5b6275")
LINE = colors.HexColor("#b8bdcc")

BOX = 9
ROW_H = 14.5
COL_STEP = 19

SESSIONS_LEFT = [
    ("t2_s1", "T2 · Intro to Software Engineering"),
    ("t2_s2", "T2 · Career Conversations"),
    ("t2_s3", "T2 · Resource Session"),
    ("t2_panel", "T2 · Tech Careers Panel"),
    ("t3_l1", "L1 · HTML landing page"),
    ("t3_l2", "L2 · CSS styling"),
]
SESSIONS_RIGHT = [
    ("t3_l3", "L3 · Advanced HTML/CSS"),
    ("t3_l4", "L4 · JavaScript fundamentals"),
    ("t3_l5", "L5 · Website interactivity"),
    ("t3_l6", "L6 · APIs and fetching data"),
    ("t3_l7", "L7 · Git and GitHub"),
    ("t3_l8", "L8 · Deploying your site"),
]

SKILLS = [
    ("html", "Structuring a page with HTML"),
    ("css", "Styling & responsive layouts (CSS)"),
    ("js", "JavaScript functions, loops, events"),
    ("api", "Fetching data from an API"),
    ("git", "Using Git and GitHub with a team"),
    ("deploy", "Deploying with GitHub Pages"),
]

STATEMENTS = [
    ("pace", "The lessons moved at a good pace"),
    ("explain", "Concepts were explained clearly"),
    ("help", "I could get help when I was stuck"),
    ("tools", "I had enough device/internet access"),
    ("capstone", "The capstone helped me apply skills"),
    ("team", "My team worked well together"),
    ("career", "I can picture myself in a tech career"),
]

CAREER_PATHS = [
    ("web", "Web Development"),
    ("mobile", "Mobile Development"),
    ("security", "Cybersecurity"),
    ("ai", "AI & Machine Learning"),
    ("data", "Data Analysis"),
    ("cloud", "Cloud & DevOps"),
    ("uiux", "UI/UX Design"),
    ("games", "Game Development"),
    ("qa", "QA & Testing"),
    ("unsure", "Not sure yet"),
]

OPEN_QUESTIONS = [
    ("enjoyed_most", "What did you enjoy most, and why?"),
    ("hardest", "What was hardest? What would have helped?"),
    ("change", "What should we change or add for the next group?"),
    ("message", "A message for the facilitators and volunteers"),
]

# Form widgets are invisible: the printed boxes and lines are drawn on the page.
HIDDEN = dict(borderWidth=0, borderColor=colors.transparent, fillColor=colors.transparent)


class OnePageForm:
    def __init__(self, path):
        self.c = canvas.Canvas(str(path), pagesize=A4)
        self.c.setTitle("Student Feedback Form – Software Engineering Program")
        self.c.setAuthor("TOFA & Alliance Girls Alumni")
        self.c.setSubject("End-of-program student feedback")
        self.form = self.c.acroForm
        self.y = PAGE_H

    # ----- drawing primitives ---------------------------------------------
    def text(self, x, y, value, size=8, bold=False, color=NAVY, align="left"):
        self.c.setFillColor(color)
        self.c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
        draw = {"left": self.c.drawString, "centre": self.c.drawCentredString,
                "right": self.c.drawRightString}[align]
        draw(x, y, value)

    def box(self, x, y):
        """Printed tick box with its lower-left corner at (x, y)."""
        self.c.setStrokeColor(NAVY)
        self.c.setLineWidth(0.7)
        self.c.setFillColor(colors.white)
        self.c.rect(x, y, BOX, BOX, stroke=1, fill=1)

    def radio(self, group, value, tooltip, x, y):
        self.box(x, y)
        self.form.radio(name=group, value=value, tooltip=tooltip, selected=False, x=x, y=y,
                        size=BOX, buttonStyle="circle", shape="square", textColor=BLUE,
                        **HIDDEN)

    def checkbox(self, name, tooltip, x, y):
        self.box(x, y)
        self.form.checkbox(name=name, tooltip=tooltip, x=x, y=y, size=BOX,
                           buttonStyle="check", textColor=BLUE, **HIDDEN)

    def bar(self, x, width, title):
        self.c.setFillColor(BLUE)
        self.c.roundRect(x, self.y - 14, width, 16, 3, stroke=0, fill=1)
        self.text(x + 7, self.y - 9, title, size=9.5, bold=True, color=colors.white)

    # ----- page sections ----------------------------------------------------
    def header(self):
        band_h = 58
        self.c.setFillColor(NAVY)
        self.c.rect(0, PAGE_H - band_h, PAGE_W, band_h, stroke=0, fill=1)
        stripe_w = PAGE_W / 4
        for i, col in enumerate((BLUE, PINK, GOLD, GREEN)):
            self.c.setFillColor(col)
            self.c.rect(i * stripe_w, PAGE_H - band_h - 4, stripe_w, 4, stroke=0, fill=1)
        self.text(MARGIN, PAGE_H - 20,
                  "ALLIANCE GIRLS HIGH SCHOOL · SOFTWARE ENGINEERING PROGRAM",
                  size=7.5, bold=True, color=GOLD)
        self.text(MARGIN, PAGE_H - 44, "Student Feedback Form", size=19, bold=True,
                  color=colors.white)
        self.text(PAGE_W - MARGIN, PAGE_H - 44, "Term 2 sessions · Term 3 lessons & capstone",
                  size=8.5, color=CREAM, align="right")
        self.y = PAGE_H - band_h - 18
        self.text(MARGIN, self.y,
                  "Thank you for being part of this program! Please answer honestly – you do not "
                  "need to write your name.", size=8.5)
        self.y -= 11
        self.text(MARGIN, self.y,
                  "Tick (or shade) one box per row with a pen. You can also fill this form in "
                  "on screen.", size=8.5, color=GREY)
        self.y -= 12

    def grid(self, x, width, rows, labels, values, prefix, legend, first_col):
        """Rating grid inside a column starting at ``x``; returns the bottom y."""
        y = self.y
        self.text(x, y, legend, size=7, color=GREY)
        y -= 12
        x_last = x + width - BOX / 2 - 4
        col_x = [x_last - (len(labels) - 1 - i) * COL_STEP for i in range(len(labels))]
        self.text(x + 3, y, first_col, size=6.5, bold=True, color=GREY)
        for cx, label in zip(col_x, labels):
            self.text(cx, y, label, size=6.5, bold=True, color=GREY, align="centre")
        y -= 4
        for index, (key, label) in enumerate(rows):
            if index % 2 == 0:
                self.c.setFillColor(CREAM)
                self.c.rect(x, y - ROW_H, width, ROW_H, stroke=0, fill=1)
            self.text(x + 3, y - ROW_H + 4.5, label, size=7.5)
            for cx, value, col_label in zip(col_x, values, labels):
                self.radio(f"{prefix}_{key}", value, f"{label}: {col_label}",
                           cx - BOX / 2, y - ROW_H + (ROW_H - BOX) / 2)
            y -= ROW_H
        return y

    def sessions(self):
        self.y -= 4
        self.bar(MARGIN, CONTENT_W, "1. Rate each session")
        self.y -= 26
        labels = ["1", "2", "3", "4", "5", "N/A"]
        values = ["1", "2", "3", "4", "5", "NA"]
        legend = "1 = not useful  ·  5 = very useful  ·  N/A = I missed it"
        left = self.grid(MARGIN, HALF_W, SESSIONS_LEFT, labels, values, "rate", legend,
                         "SESSION")
        right = self.grid(MARGIN + HALF_W + GUTTER, HALF_W, SESSIONS_RIGHT, labels, values,
                          "rate", "", "LESSON")
        self.y = min(left, right) - 10

    def skills_and_experience(self):
        right_x = MARGIN + HALF_W + GUTTER
        self.bar(MARGIN, HALF_W, "2. Your skills now")
        self.bar(right_x, HALF_W, "3. The program experience")
        self.y -= 26
        scale = ["1", "2", "3", "4", "5"]
        left = self.grid(MARGIN, HALF_W, SKILLS, scale, scale, "skill",
                         "1 = not confident yet  ·  5 = very confident", "SKILL")
        right = self.grid(right_x, HALF_W, STATEMENTS, scale, scale, "agree",
                          "1 = strongly disagree  ·  5 = strongly agree", "STATEMENT")
        self.y = min(left, right) - 10

    def inline_choices(self, x, y, group, options, tooltip):
        for value, label in options:
            self.radio(group, value, f"{tooltip}: {label}", x, y - 2)
            self.text(x + BOX + 3, y, label, size=7.5)
            x += BOX + 3 + self.c.stringWidth(label, "Helvetica", 7.5) + 9
        return x

    def looking_ahead(self):
        self.bar(MARGIN, CONTENT_W, "4. Looking ahead")
        self.y -= 28
        scale = [(str(i), str(i)) for i in range(1, 6)]
        x = MARGIN
        self.text(x, self.y, "Interest in a tech career  BEFORE:", size=8, bold=True)
        x += self.c.stringWidth("Interest in a tech career  BEFORE:", "Helvetica-Bold", 8) + 6
        x = self.inline_choices(x, self.y, "interest_before", scale, "Interest before")
        self.text(x + 4, self.y, "NOW:", size=8, bold=True)
        x += 4 + self.c.stringWidth("NOW:", "Helvetica-Bold", 8) + 6
        x = self.inline_choices(x, self.y, "interest_now", scale, "Interest now")
        self.text(x, self.y, "(1 = not at all · 5 = extremely)", size=7, color=GREY)
        self.y -= 17
        label = "Would you recommend this program to a friend?"
        self.text(MARGIN, self.y, label, size=8, bold=True)
        self.inline_choices(MARGIN + self.c.stringWidth(label, "Helvetica-Bold", 8) + 8,
                            self.y, "recommend",
                            [("yes", "Yes"), ("maybe", "Maybe"), ("no", "No")], "Recommend")
        self.y -= 17
        self.text(MARGIN, self.y, "Which tech fields would you like to explore next? "
                  "(tick all that apply)", size=8, bold=True)
        self.y -= 15
        columns = 5
        col_w = CONTENT_W / columns
        for i, (key, label) in enumerate(CAREER_PATHS):
            x = MARGIN + (i % columns) * col_w
            y = self.y - (i // columns) * 14
            self.checkbox(f"explore_{key}", f"Field to explore: {label}", x, y - 2)
            self.text(x + BOX + 4, y, label, size=7.5)
        rows = (len(CAREER_PATHS) + columns - 1) // columns
        self.y -= (rows - 1) * 14 + 16

    def writing_box(self, name, question, x, width, lines):
        line_gap = 17
        self.text(x, self.y, question, size=8, bold=True)
        top = self.y - 5
        height = lines * line_gap + 4
        self.c.setStrokeColor(LINE)
        self.c.setLineWidth(0.7)
        self.c.roundRect(x, top - height, width, height, 3, stroke=1, fill=0)
        self.c.setLineWidth(0.5)
        for i in range(1, lines + 1):
            ly = top - i * line_gap
            self.c.line(x + 6, ly, x + width - 6, ly)
        self.form.textfield(name=name, tooltip=question, x=x + 2, y=top - height + 2,
                            width=width - 4, height=height - 4, fontSize=9, textColor=NAVY,
                            fieldFlags="multiline doNotScroll", **HIDDEN)
        return top - height

    def tell_us_more(self, lines):
        self.bar(MARGIN, CONTENT_W, "5. Tell us more")
        self.y -= 28
        pairs = [OPEN_QUESTIONS[i:i + 2] for i in range(0, len(OPEN_QUESTIONS), 2)]
        for pair in pairs:
            bottoms = [self.writing_box(name, question, MARGIN + i * (HALF_W + GUTTER),
                                        HALF_W, lines)
                       for i, (name, question) in enumerate(pair)]
            self.y = min(bottoms) - 14

    def closing(self):
        self.checkbox("quote_consent", "Consent to share comments anonymously", MARGIN,
                      self.y - 2)
        self.text(MARGIN + BOX + 5, self.y,
                  "I agree that my comments may be shared anonymously (without my name) to "
                  "improve the program.", size=7.5)
        self.text(PAGE_W - MARGIN, self.y, "Thank you – keep building!", size=9.5, bold=True,
                  color=PINK, align="right")
        self.y -= 10
        if self.y < BOTTOM:
            raise SystemExit("Feedback form no longer fits on one page – shorten the content.")
        self.text(MARGIN, 18, "TOFA × Alliance Girls Alumni · Alliance Girls High School",
                  size=7, color=GREY)

    def save(self):
        self.c.save()


def build(path=OUTPUT, writing_lines=6):
    form = OnePageForm(path)
    form.header()
    form.sessions()
    form.skills_and_experience()
    form.looking_ahead()
    form.tell_us_more(writing_lines)
    form.closing()
    form.save()
    return path


if __name__ == "__main__":
    print(f"Wrote {build()}")
