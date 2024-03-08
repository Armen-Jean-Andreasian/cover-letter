from .pdf_file import PdfFile
from resources.text_samples import GREETING_TEXT, BODY_TEXT, FOOTER_TEXT

from utils.qr_code_generator.qr import qr_builder
from utils.date_stampt import date_today
from utils.file_readers import read_ini


class CoverLetter:
    __output_folder = read_ini(
        ini_path='configuration.ini',
        items=(
            ("output_filepaths", "output_folder"),
        )
    )[0]

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.file_name_prototype = "{output_folder}/{applicant_name}-{position_applied}-Cover_Letter.pdf"
        return instance

    def __init__(self, background_color, font_family="Arial", font_size=12, ):
        self.background_color = background_color
        self.font_family = font_family
        self.font_size = font_size

        self.heading_font_family = "Arial"
        self.heading_font_style = "I"
        self.heading_font_size = 16

        self.content_font_family = "Arial"
        self.content_font_size = 12

        self.pdf_file = PdfFile()

        self.file_name = None

    def set_page_config(self):
        """Should be called after the page is added."""
        self.pdf_file.set_fill_color(*self.background_color)
        self.pdf_file.rect(0, 0, self.pdf_file.w, self.pdf_file.h, 'F')

    def add_content(self, applicant_name, hr_name, email, phone, company, position, website):
        """Adds content to the page"""
        self.pdf_file.set_font(family=self.content_font_family, size=self.content_font_size)  # content font
        self.pdf_file.add_cell(w=190, txt=f"Date: {date_today()}", align="R")

        self.pdf_file.set_font(family=self.heading_font_family, size=self.heading_font_size,
                               style=self.heading_font_style)  # heading font
        self.pdf_file.add_cell(txt=f"Dear {hr_name}", align="C")

        self.pdf_file.set_font(family=self.content_font_family, size=self.content_font_size)  # content font
        self.pdf_file.add_multi_cell(txt=GREETING_TEXT.format(position=position, company=company))
        self.pdf_file.add_multi_cell(txt=BODY_TEXT)
        self.pdf_file.add_multi_cell(txt=FOOTER_TEXT.format(email=email, phone=phone))

        self.pdf_file.add_cell(txt="Sincerely,", add_break_line=False)
        self.pdf_file.add_cell(txt=f"{applicant_name}")

        if website:
            qr_builder(message=website)  # generating QR code
            self.pdf_file.image(name="OUTPUT_FOLDER/qrcode.png", x=10, y=10, w=15)  # adding QR code

        self._init_file_name(applicant_name, position)

        return self

    def _init_file_name(self, applicant_name: str, position: str):
        self.file_name = self.file_name_prototype.format(
            output_folder=self.__output_folder,
            applicant_name=applicant_name.replace(' ', '_'),
            position_applied=position.replace(' ', '_')
        )
        return self

    def save_file(self):
        """Saves the PDF file to computer"""
        self.pdf_file.output(name=self.file_name)
        return self
