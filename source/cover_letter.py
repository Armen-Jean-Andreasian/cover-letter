from .pdf_file import PdfFile
from config_files.pdf_configuration import PdfConfig
from resources.text_samples import GREETING_TEXT, BODY_TEXT, FOOTER_TEXT
from utils.qr_code_generator.qr import qr_builder
from utils.date_stampt import date_today


class CoverLetter:

    def __init__(self, background_color):
        self.config = PdfConfig()

        self.background_color = background_color if background_color is not None else self.config.background_color
        self.pdf_file = PdfFile()
        self.file_name = None

    def set_page_config(self):
        """Should be called after the page is added."""
        self.pdf_file.set_fill_color(*self.background_color)
        self.pdf_file.rect(0, 0, self.pdf_file.w, self.pdf_file.h, 'F')

    def add_content(self, applicant_name, hr_name, email, phone, company, position, website):
        """Adds content to the page"""
        # content font

        print(company)
        print(hr_name)
        self.pdf_file.set_font(family=self.config.content_font_family, size=self.config.content_font_size)

        self.pdf_file.add_cell(w=190, txt=f"Date: {date_today()}", align="R")

        self.pdf_file.set_font(family=self.config.heading_font_family, size=self.config.heading_font_size,
                               style=self.config.heading_font_style)  # heading font

        self.pdf_file.add_cell(txt=f"Dear {hr_name}", align="C")

        # content font
        self.pdf_file.set_font(family=self.config.content_font_family, size=self.config.content_font_size)
        self.pdf_file.add_multi_cell(txt=GREETING_TEXT.format(position=position, company=company))
        self.pdf_file.add_multi_cell(txt=BODY_TEXT)
        self.pdf_file.add_multi_cell(txt=FOOTER_TEXT.format(email=email, phone=phone))

        self.pdf_file.add_cell(txt="Sincerely,", add_break_line=False)
        self.pdf_file.add_cell(txt=f"{applicant_name}")

        # generating QR image
        if website:
            qr_builder(message=website)
            self.pdf_file.image(name="OUTPUT_FOLDER/qrcode.png", x=10, y=10, w=15)  # adding QR

        self._init_file_name(applicant_name, position)

        return self

    def _init_file_name(self, applicant_name: str, position: str):
        self.file_name = self.config.output_file_name_prototype.format(
            output_folder=self.config.pdf_output_folder,
            applicant_name=applicant_name.replace(' ', '_'),
            position_applied=position.replace(' ', '_')
        )
        return self

    def save_file(self):
        """Saves the PDF file to computer"""
        self.pdf_file.output(name=self.file_name)
        return self
