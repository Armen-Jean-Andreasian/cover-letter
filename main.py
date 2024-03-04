from fpdf import FPDF
from scripts import date_today
from scripts import take_input
from texts import GREETING_TEXT, BODY_TEXT, FOOTER_TEXT


class CoverLetterGenerator:
    background_color = 189, 212, 188

    def __init__(self, name, company, position, email, phone):
        self.name = name
        self.company = company
        self.position = position
        self.email = email
        self.phone = phone
        self.pdf_file = ...
        self.pdf = FPDF()

    def add_cell(self, txt, w=200, h=10, ln=True, align="L", add_break_line=True):
        """
        Adds a cell to the PDF document.

        Args:
            txt (str): The text content to add to the cell.
            w (int, optional): The width of the cell in millimeters. Defaults to 200.
            h (int, optional): The height of the cell in millimeters. Defaults to 10.
            ln (bool, optional): Whether to start a new line after adding the cell. Defaults to True.
            align (str, optional): The alignment of the text within the cell ("L" for left, "R" for right).
            Defaults to "L".
            add_break_line (bool, optional): Whether to add a line break of 10 points after the cell. Defaults to True.

        Returns:
            CoverLetterGenerator: Returns itself for method chaining.
        """
        self.pdf.cell(w=w, h=h, txt=txt, ln=ln, align=align)
        if add_break_line:
            self.pdf.ln(10)
        return self

    def add_multi_cell(self, txt, w=0, h=10, add_break_line=True):
        self.pdf.multi_cell(w, h, txt=txt)
        if add_break_line:
            self.pdf.ln(10)
        return self

    def save_file(self):
        self.pdf_file = f"output/{self.name.replace(' ', '_')}-{self.position.replace(' ', '_')}-Cover_Letter.pdf"
        self.pdf.output(self.pdf_file)

    def generate_cover_letter(self):
        self.pdf.add_page()
        self.pdf.set_fill_color(*self.background_color)
        self.pdf.set_font(family="Arial", size=12)

        self.add_cell(w=190, txt=f"Date: {date_today()}", align="R")
        self.add_cell(txt=f"Dear Hiring Manager,")
        self.add_multi_cell(txt=GREETING_TEXT.format(position=self.position, company=self.company))
        self.add_multi_cell(txt=BODY_TEXT)
        self.add_multi_cell(txt=FOOTER_TEXT.format(email=self.email, phone=self.phone))

        self.add_cell(txt="Sincerely,", add_break_line=False)
        self.add_cell(txt=f"{self.name}")

        return self.save_file()


def main():
    name = take_input("Enter your full name: ")
    company = input("Enter the company name: ")
    position = input("Enter the position you're applying for: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")

    cover_letter = CoverLetterGenerator(name, company, position, email, phone)
    cover_letter.generate_cover_letter()

    print(f"Cover letter generated successfully: {cover_letter.pdf_file}")


if __name__ == "__main__":
    g = CoverLetterGenerator("name", "company", "position", "email", "phone")
    g.add_multi_cell(txt="", h="ww")
