import os
from utils.export_binary import export_file
from .cover_letter import CoverLetter
from .applicant import Applicant


class CoverLetterGenerator(CoverLetter):
    def __init__(self, background_color, applicant_name, hr_name, email, phone, company, position, website):
        super().__init__(background_color)

        self.applicant = Applicant()
        self.applicant.applicant_name = applicant_name
        self.applicant.email = email
        self.applicant.phone = phone
        self.applicant.position = position
        self.applicant.website = website

        self.hr_name = hr_name
        self.company = company

    def generate(self):
        # adding one page
        self.pdf_file.add_page()
        # setting the config of the page
        self.set_page_config()

        # adding content
        self.add_content(applicant_name=self.applicant.applicant_name,
                         hr_name=self.hr_name,
                         email=self.applicant.email,
                         phone=self.applicant.phone,
                         company=self.company,
                         position=self.applicant.position,
                         website=self.applicant.website)

        # exporting pdf using threading
        export_file(io_bound_function=self.applicant.save_new_data)
        export_file(io_bound_function=self.save_file)

        filepath_to_show = os.path.join(os.path.abspath(os.curdir), self.file_name.replace('/', '\\'))

        return f"Cover letter generated successfully! <br> Output location: {filepath_to_show}"
