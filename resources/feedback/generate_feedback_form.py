"""Generate the fillable end-of-program student feedback form (PDF).

Usage (from the repository root):

    pip install reportlab
    python resources/feedback/generate_feedback_form.py

The PDF is written next to this script as ``student-feedback-form.pdf``.
Edit the question lists below and re-run the script to update the form.
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

OUTPUT = Path(__file__).with_name("student-feedback-form.pdf")

PAGE_W, PAGE_H = A4
MARGIN = 40
BOTTOM = 45
CONTENT_W = PAGE_W - 2 * MARGIN

NAVY = colors.HexColor("#0b1022")
BLUE = colors.HexColor("#315ee7")
PINK = colors.HexColor("#ed6a9a")
GOLD = colors.HexColor("#f5c95f")
GREEN = colors.HexColor("#72c4a7")
CREAM = colors.HexColor("#f8f4ea")
GREY = colors.HexColor("#5b6275")
FIELD_BG = colors.HexColor("#f4f6fd")

PROGRAM_SESSIONS = [
    ("t2_s1", "Term 2 · Session 1 – Introduction to Software Engineering"),
    ("t2_s2", "Term 2 · Session 2 – Career Conversations"),
    ("t2_s3", "Term 2 · Session 3 – Resource Session"),
    ("t2_panel", "Term 2 · Tech Careers Panel & Group Discussion"),
    ("t3_l1", "Lesson 1 – Create a landing page with HTML"),
    ("t3_l2", "Lesson 2 – Add CSS to beautify your page"),
    ("t3_l3", "Lesson 3 – Advanced HTML/CSS concepts"),
    ("t3_l4", "Lesson 4 – JavaScript functions, loops, and more"),
    ("t3_l5", "Lesson 5 – Add interactivity to your website"),
    ("t3_l6", "Lesson 6 – APIs and fetching internet data"),
    ("t3_l7", "Lesson 7 – Version control with Git and GitHub"),
    ("t3_l8", "Lesson 8 – Deploy web applications"),
]

SKILLS = [
    ("html", "Writing HTML to structure a web page"),
    ("css", "Styling a page with CSS (incl. responsive layouts)"),
    ("js", "Writing JavaScript (functions, loops, events)"),
    ("api", "Fetching data from an API"),
    ("git", "Using Git and GitHub with a team"),
    ("deploy", "Deploying a website with GitHub Pages"),
]

STATEMENTS = [
    ("pace", "The lessons moved at a good pace for me."),
    ("explain", "Facilitators explained concepts clearly."),
    ("help", "I could get help when I was stuck."),
    ("tools", "I had enough access to devices and the internet."),
    ("capstone", "The capstone helped me apply what I learned."),
    ("team", "My team worked well together."),
    ("career", "I can picture myself in a tech career."),
]

CAPSTONES = [
    ("hub", "School Opportunities Hub"),
    ("weather", "Kenya Weather Dashboard"),
    ("cyber", "CyberSmart Quest"),
    ("none", "Did not build one"),
]

INTEREST_SCALE = [
    ("1", "Not at all"),
    ("2", "A little"),
    ("3", "Somewhat"),
    ("4", "Very"),
    ("5", "Extremely"),
]

CAREER_PATHS = [
    ("web", "Web Development"),
    ("mobile", "Mobile Development"),
    ("security", "Cybersecurity"),
    ("ai", "AI & Machine Learning"),
    ("data", "Data Analysis & Science"),
    ("cloud", "Cloud & DevOps"),
    ("uiux", "UI/UX Design"),
    ("games", "Game Development"),
    ("qa", "Quality Assurance & Testing"),
    ("unsure", "Not sure yet"),
]

BUTTON_STYLE = dict(
    borderColor=BLUE, fillColor=colors.white, textColor=BLUE, borderWidth=0.8, forceBorder=True,
)
FIELD_STYLE = dict(
    fontSize=10, borderWidth=0.8, borderColor=GREY, fillColor=FIELD_BG, textColor=NAVY,
    forceBorder=True,
)


class FormBuilder:
    """Small helper that tracks the cursor position while drawing the form."""

    def __init__(self, path):
        self.c = canvas.Canvas(str(path), pagesize=A4)
        self.c.setTitle("Student Feedback Form – Software Engineering Program")
        self.c.setAuthor("TOFA & Alliance Girls Alumni")
        self.c.setSubject("End-of-program student feedback")
        self.form = self.c.acroForm
        self.page = 0
        self.y = 0
        self.new_page()

    # ----- page furniture -------------------------------------------------
    def new_page(self):
        if self.page:
            self.footer()
            self.c.showPage()
        self.page += 1
        self.y = PAGE_H - MARGIN
        if self.page == 1:
            self.title_block()
        else:
            self.c.setFillColor(GREY)
            self.c.setFont("Helvetica", 8)
            self.c.drawString(MARGIN, self.y, "Student Feedback Form · Software Engineering Program")
            self.y -= 22

    def footer(self):
        self.c.setFillColor(GREY)
        self.c.setFont("Helvetica", 8)
        self.c.drawString(MARGIN, 22, "TOFA × Alliance Girls Alumni · Alliance Girls High School")
        self.c.drawRightString(PAGE_W - MARGIN, 22, f"Page {self.page}")

    def ensure(self, height):
        if self.y - height < BOTTOM:
            self.new_page()

    def title_block(self):
        band_h = 92
        self.c.setFillColor(NAVY)
        self.c.rect(0, PAGE_H - band_h, PAGE_W, band_h, stroke=0, fill=1)
        stripe_w = PAGE_W / 4
        for i, col in enumerate((BLUE, PINK, GOLD, GREEN)):
            self.c.setFillColor(col)
            self.c.rect(i * stripe_w, PAGE_H - band_h - 5, stripe_w, 5, stroke=0, fill=1)
        self.c.setFillColor(GOLD)
        self.c.setFont("Helvetica-Bold", 9)
        self.c.drawString(MARGIN, PAGE_H - 30,
                          "ALLIANCE GIRLS HIGH SCHOOL · SOFTWARE ENGINEERING PROGRAM")
        self.c.setFillColor(colors.white)
        self.c.setFont("Helvetica-Bold", 22)
        self.c.drawString(MARGIN, PAGE_H - 58, "Student Feedback Form")
        self.c.setFont("Helvetica", 10)
        self.c.setFillColor(CREAM)
        self.c.drawString(MARGIN, PAGE_H - 77,
                          "Final class · Term 2 sessions, Term 3 lessons and capstone")
        self.y = PAGE_H - band_h - 24
        intro = [
            "Thank you for being part of this program! Your honest answers help us improve it for",
            "future students at Alliance Girls and at other schools. Your name is optional and there",
            "are no wrong answers. Click a box to choose an answer and type in the shaded boxes",
            "to write – or print this form and fill it in by hand.",
        ]
        self.c.setFillColor(NAVY)
        self.c.setFont("Helvetica", 9.5)
        for line in intro:
            self.c.drawString(MARGIN, self.y, line)
            self.y -= 13
        self.y -= 6

    # ----- content helpers ------------------------------------------------
    def section(self, letter, title, hint=None, keep_with=60):
        self.ensure(30 + (14 if hint else 0) + keep_with)
        self.y -= 6
        self.c.setFillColor(BLUE)
        self.c.roundRect(MARGIN, self.y - 16, CONTENT_W, 20, 4, stroke=0, fill=1)
        self.c.setFillColor(colors.white)
        self.c.setFont("Helvetica-Bold", 11)
        self.c.drawString(MARGIN + 8, self.y - 10, f"{letter}. {title}")
        self.y -= 30
        if hint:
            self.c.setFillColor(GREY)
            self.c.setFont("Helvetica-Oblique", 8.5)
            self.c.drawString(MARGIN, self.y, hint)
            self.y -= 14

    def label(self, text):
        self.c.setFillColor(NAVY)
        self.c.setFont("Helvetica-Bold", 9.5)
        self.c.drawString(MARGIN, self.y, text)

    def text_field(self, name, label, tooltip, x, width, label_w):
        self.c.setFillColor(NAVY)
        self.c.setFont("Helvetica-Bold", 9.5)
        self.c.drawString(x, self.y, label)
        self.form.textfield(name=name, tooltip=tooltip, x=x + label_w, y=self.y - 5,
                            width=width - label_w, height=17, **FIELD_STYLE)

    def text_area(self, name, question, tooltip, height=70):
        self.ensure(height + 26)
        self.label(question)
        self.y -= 6
        self.form.textfield(name=name, tooltip=tooltip, x=MARGIN, y=self.y - height,
                            width=CONTENT_W, height=height, fieldFlags="multiline doNotScroll",
                            **FIELD_STYLE)
        self.y -= height + 18

    def scale_header(self, labels, x0, step, first_col):
        lines = max(len(text.split("\n")) for text in labels)
        self.c.setFillColor(GREY)
        self.c.setFont("Helvetica-Bold", 7.5)
        self.c.drawString(MARGIN + 4, self.y - 9 * (lines - 1), first_col)
        for i, text in enumerate(labels):
            for j, part in enumerate(text.split("\n")):
                self.c.drawCentredString(x0 + i * step, self.y - 9 * j, part)
        self.y -= 9 * (lines - 1) + 10

    def rating_grid(self, rows, labels, values, prefix, first_col):
        step = 46
        x0 = PAGE_W - MARGIN - step * (len(labels) - 1) - 20
        self.ensure(40)
        self.scale_header(labels, x0, step, first_col)
        for index, (key, text) in enumerate(rows):
            if self.y - 18 < BOTTOM:
                self.new_page()
                self.scale_header(labels, x0, step, first_col)
            if index % 2 == 0:
                self.c.setFillColor(CREAM)
                self.c.rect(MARGIN, self.y - 13, CONTENT_W, 18, stroke=0, fill=1)
            self.c.setFillColor(NAVY)
            self.c.setFont("Helvetica", 9)
            self.c.drawString(MARGIN + 4, self.y - 7, text)
            for i, value in enumerate(values):
                self.form.radio(name=f"{prefix}_{key}", tooltip=f"{text}: {labels[i]}",
                                value=value, selected=False, x=x0 + i * step - 5.5,
                                y=self.y - 9.5, size=11, buttonStyle="circle", shape="square",
                                **BUTTON_STYLE)
            self.y -= 18
        self.y -= 10

    def inline_radios(self, group, options, tooltip):
        x = MARGIN
        for value, text in options:
            self.form.radio(name=group, tooltip=f"{tooltip}: {text}", value=value,
                            selected=False, x=x, y=self.y - 3, size=11, buttonStyle="circle",
                            shape="square", **BUTTON_STYLE)
            self.c.setFillColor(NAVY)
            self.c.setFont("Helvetica", 9)
            self.c.drawString(x + 15, self.y, text)
            x += 15 + self.c.stringWidth(text, "Helvetica", 9) + 18

    def radio_question(self, question, group, options, tooltip):
        self.ensure(40)
        self.label(question)
        self.y -= 16
        self.inline_radios(group, options, tooltip)
        self.y -= 24

    def checkbox(self, name, text, tooltip, x, y):
        self.form.checkbox(name=name, tooltip=tooltip, x=x, y=y - 10, size=11,
                           buttonStyle="check", **BUTTON_STYLE)
        self.c.setFillColor(NAVY)
        self.c.setFont("Helvetica", 9)
        self.c.drawString(x + 16, y - 8, text)

    def checkbox_question(self, question, prefix, options, columns, tooltip):
        rows = (len(options) + columns - 1) // columns
        self.ensure(rows * 18 + 30)
        self.label(question)
        self.y -= 10
        col_w = CONTENT_W / columns
        for i, (key, text) in enumerate(options):
            col, row = i % columns, i // columns
            self.checkbox(f"{prefix}_{key}", text, f"{tooltip}: {text}",
                          MARGIN + col * col_w, self.y - row * 18)
        self.y -= rows * 18 + 12

    def save(self):
        self.footer()
        self.c.save()


def build(path=OUTPUT):
    f = FormBuilder(path)

    f.section("A", "About you")
    half = CONTENT_W / 2
    f.text_field("name", "Name (optional)", "Your name (optional)", MARGIN, half - 10, 88)
    f.text_field("team", "Team name", "Your capstone team name", MARGIN + half + 10,
                 half - 10, 62)
    f.y -= 28
    f.radio_question("Which capstone did your team build?", "capstone", CAPSTONES,
                     "Capstone built")

    f.section("B", "Rate each session",
              "1 = not useful / did not enjoy  ·  5 = very useful / loved it  ·  "
              "N/A = I missed this session", keep_with=60)
    f.rating_grid(PROGRAM_SESSIONS, ["1", "2", "3", "4", "5", "N/A"],
                  ["1", "2", "3", "4", "5", "NA"], "rate", "SESSION")

    f.section("C", "Your skills now",
              "How confident do you feel doing each of these on your own today?",
              keep_with=6 * 18 + 30)
    f.rating_grid(SKILLS, ["Not yet", "A little", "Somewhat", "Confident", "Very\nconfident"],
                  ["1", "2", "3", "4", "5"], "skill", "SKILL")

    f.section("D", "The program experience", "How much do you agree with each statement?",
              keep_with=7 * 18 + 30)
    f.rating_grid(STATEMENTS, ["Strongly\ndisagree", "Disagree", "Neutral", "Agree",
                               "Strongly\nagree"],
                  ["1", "2", "3", "4", "5"], "agree", "STATEMENT")

    f.section("E", "Looking ahead")
    f.radio_question("Before this program, how interested were you in a tech career?",
                     "interest_before", INTEREST_SCALE, "Interest before the program")
    f.radio_question("How interested are you in a tech career now?", "interest_now",
                     INTEREST_SCALE, "Interest now")
    f.radio_question("Would you recommend this program to a friend?", "recommend",
                     [("yes", "Yes"), ("maybe", "Maybe"), ("no", "No")], "Recommend to a friend")
    f.checkbox_question("Which tech fields would you like to explore next? (tick all that apply)",
                        "explore", CAREER_PATHS, 3, "Field to explore")

    f.section("F", "Tell us more", keep_with=96)
    f.text_area("enjoyed_most", "What did you enjoy most, and why?", "What you enjoyed most")
    f.text_area("hardest", "What was the hardest part? What would have helped?",
                "Hardest part and what would have helped")
    f.text_area("proudest", "What are you most proud of building or learning?",
                "What you are most proud of")
    f.text_area("change",
                "What should we change, add, or remove for the next group of students?",
                "Suggestions for next time", height=90)
    f.text_area("message", "Any message for the facilitators, speakers, or alumni volunteers?",
                "Message for facilitators")

    f.ensure(50)
    f.checkbox("quote_consent",
               "I agree that my comments may be shared anonymously (without my name) to "
               "improve the program.",
               "Consent to share comments anonymously", MARGIN, f.y)
    f.y -= 34
    f.c.setFillColor(PINK)
    f.c.setFont("Helvetica-Bold", 12)
    f.c.drawCentredString(PAGE_W / 2, f.y, "Thank you – keep building!")

    f.save()
    return path


if __name__ == "__main__":
    print(f"Wrote {build()}")
