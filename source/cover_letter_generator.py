import os
from .pdf_file import PdfFile
from .applicant import Applicant
from resources.text_samples import GREETING_TEXT, BODY_TEXT, FOOTER_TEXT
from utils.export_binary import export_file
from utils.qr_code_generator.qr import qr_builder
from utils.date_stampt import date_today
from utils.file_readers import read_ini


class CoverLetterGenerator(Applicant):
    __output_folder = read_ini(
        ini_path='configuration.ini',
        items=(
            ("output_filepaths", "output_folder"),
        )
    )[0]

    file_name_prototype = "{output_folder}/{applicant_name}-{position_applied}-Cover_Letter.pdf"

    __slots__ = Applicant.__slots__ + ("file_name", "background_color", "font_family", "font_size", "pdf_file",
                                       "heading_font_family", "heading_font_style", "heading_font_size",
                                       "content_font_family", "content_font_size")

    def __init__(self, name, company, position, email, phone, website, background_color=(189, 212, 188),
                 font_family="Arial",
                 font_size=12):
        super().__init__(name=name, company=company, position=position, email=email, phone=phone, website=website)
        self.background_color = background_color
        self.font_family = font_family
        self.font_size = font_size

        self.heading_font_family = "Arial"
        self.heading_font_style = "I"
        self.heading_font_size = 16

        self.content_font_family = "Arial"
        self.content_font_size = 12

        self.pdf_file = PdfFile()

        self.file_name = self.file_name_prototype.format(
            output_folder=self.__output_folder,
            applicant_name=self.name.replace(' ', '_'),
            position_applied=self.position.replace(' ', '_')
        )

    def set_page_config(self):
        """Should be called after the page is added."""
        self.pdf_file.set_fill_color(*self.background_color)
        self.pdf_file.rect(0, 0, self.pdf_file.w, self.pdf_file.h, 'F')

    def add_content(self):
        """Adds content to the page"""
        self.pdf_file.set_font(family=self.content_font_family, size=self.content_font_size)  # content font
        self.pdf_file.add_cell(w=190, txt=f"Date: {date_today()}", align="R")

        self.pdf_file.set_font(family=self.heading_font_family, size=self.heading_font_size,
                               style=self.heading_font_style)  # heading font
        self.pdf_file.add_cell(txt=f"Dear Hiring Manager", align="C")

        self.pdf_file.set_font(family=self.content_font_family, size=self.content_font_size)  # content font
        self.pdf_file.add_multi_cell(txt=GREETING_TEXT.format(position=self.position, company=self.company))
        self.pdf_file.add_multi_cell(txt=BODY_TEXT)
        self.pdf_file.add_multi_cell(txt=FOOTER_TEXT.format(email=self.email, phone=self.phone))

        self.pdf_file.add_cell(txt="Sincerely,", add_break_line=False)
        self.pdf_file.add_cell(txt=f"{self.name}")

        if self.website:
            qr_builder(message=self.website)  # generating QR code
            self.pdf_file.image(name="OUTPUT_FOLDER/qrcode.png", x=10, y=10, w=15) # adding QR code

        return self

    def save_file(self):
        """Saves the PDF file to computer"""
        self.save_new_data()
        self.pdf_file.output(name=self.file_name)
        return self

    def generate(self):
        # adding one page
        self.pdf_file.add_page()

        # setting the config of the page
        self.set_page_config()

        # adding content
        self.add_content()

        # exporting pdf using threading
        export_file(io_bound_function=self.save_file)

        filepath_to_show = os.path.join(os.path.abspath(os.curdir), self.file_name.replace('/', '\\'))

        return f"Cover letter generated successfully! <br> Output location: {filepath_to_show}"
