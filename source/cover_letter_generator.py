import threading
from static.samples.text_samples import GREETING_TEXT, BODY_TEXT, FOOTER_TEXT
from utils import date_today
from .pdf_file import PdfFile
from .applicant import Applicant


class CoverLetterGenerator(Applicant):

    def __init__(self, name, company, position, email, phone, background_color=(189, 212, 188), font_family="Arial",
                 font_size=12):
        super().__init__(name, company, position, email, phone)

        self.background_color = background_color
        self.font_family = font_family
        self.font_size = font_size

        self.pdf_file = PdfFile()
        self.file_name = f"output/{self.name.replace(' ', '_')}-{self.position.replace(' ', '_')}-Cover_Letter.pdf"

    def set_page_config(self):
        """Should be called after the page is added."""
        self.pdf_file.set_fill_color(*self.background_color)
        self.pdf_file.rect(0, 0, self.pdf_file.w, self.pdf_file.h, 'F')
        self.pdf_file.set_font(family=self.font_family, size=self.font_size)

    def add_content(self):
        """Adds content to the page"""
        self.pdf_file.add_cell(w=190, txt=f"Date: {date_today()}", align="R")
        self.pdf_file.add_cell(txt=f"Dear Hiring Manager,")
        self.pdf_file.add_multi_cell(txt=GREETING_TEXT.format(position=self.position, company=self.company))
        self.pdf_file.add_multi_cell(txt=BODY_TEXT)
        self.pdf_file.add_multi_cell(txt=FOOTER_TEXT.format(email=self.email, phone=self.phone))

        self.pdf_file.add_cell(txt="Sincerely,", add_break_line=False)
        self.pdf_file.add_cell(txt=f"{self.name}")
        return self

    def save_file(self):
        """Saves the PDF file to computer"""
        self.pdf_file.output(name=self.file_name)
        return self

    def generate(self):
        # adding one page
        self.pdf_file.add_page()

        # setting the config of the page
        self.set_page_config()

        # adding content
        self.add_content()

        import string
        # exporting it using threading

        save_file_thread = threading.Thread(target=self.save_file)
        save_file_thread.start()
        save_file_thread.join()
        import os

        filepath_to_show = os.path.join(os.path.abspath(os.curdir), self.file_name.replace('/', '\\'))

        return f"Cover letter generated successfully! <br> Output location: {filepath_to_show}"