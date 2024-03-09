from PyQt5.QtWidgets import QLineEdit, QFormLayout, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from source import CoverLetterGenerator
from source.applicant import Applicant
from .widgets import RGBColorPicker, CompletionPopUp
from utils.file_readers import read_text
from utils.titleize_input import titleize
from config_files.gui_configuration import GuiConfig


class MainFrame(QWidget):
    gui_config = GuiConfig()

    title = gui_config.title
    icon = gui_config.app_icon
    window_size = gui_config.window_size

    pdf_background_color = None
    style_sheet = read_text(filepath=gui_config.css_style_sheet_fp)

    def __init__(self):
        super().__init__()
        # loading Applicant data
        self.applicant_old_data = Applicant()

        # set window icon, title, size
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setMinimumSize(*self.window_size)
        self.setMaximumSize(*self.window_size)

        # setting the style
        self.setStyleSheet(self.style_sheet)

        # setting the widgets
        self.dialog = RGBColorPicker()
        self.dialog.colorSelected.connect(self.handle_color_selection)  # Connect signal to slot

        # setting elements
        self.name_field = QLineEdit(self.applicant_old_data.applicant_name)
        self.name_field.setPlaceholderText("Enter your full name")

        self.company_field = QLineEdit()
        self.company_field.setPlaceholderText("Enter the company name")

        self.hr_name = QLineEdit()
        self.hr_name.setPlaceholderText('Leave empty for "Dear Hiring Manager"')

        self.position_field = QLineEdit(self.applicant_old_data.position)
        self.position_field.setPlaceholderText("Enter the position")

        self.email_field = QLineEdit(self.applicant_old_data.email)
        self.email_field.setPlaceholderText("Enter your email")

        self.phone_field = QLineEdit(self.applicant_old_data.phone)
        self.phone_field.setPlaceholderText("Enter your phone number")

        self.personal_website = QLineEdit(self.applicant_old_data.website)
        self.personal_website.setPlaceholderText("Enter your website URL for a QR code")

        self.pick_color_button = QPushButton("Pick")
        self.pick_color_button.clicked.connect(self.pick_color)

        self.generate_button = QPushButton("Generate Cover Letter")
        self.generate_button.clicked.connect(self.generate_cover_letter)

        # layout of elements
        layout = QFormLayout()

        layout.addRow("Name:", self.name_field)
        layout.addRow("Company:", self.company_field)
        layout.addRow("HR name:", self.hr_name)
        layout.addRow("Position:", self.position_field)
        layout.addRow("Email:", self.email_field)
        layout.addRow("Phone:", self.phone_field)
        layout.addRow("Website", self.personal_website)
        layout.addRow("Pick a background color:", self.pick_color_button)
        layout.addRow("", self.generate_button)

        self.setLayout(layout)
        self.show()

    def pick_color(self):
        """Show the color picker dialog"""
        self.dialog.show()

    def handle_color_selection(self, color_tuple):
        """Assigns the obtained value to an instance attribute"""
        self.pdf_background_color = color_tuple
        return self

    def generate_cover_letter(self):
        applicant_name = titleize(self.name_field.text())
        company = titleize(self.company_field.text())
        hr_name = titleize(self.hr_name.text())
        position = titleize(self.position_field.text())
        email = self.email_field.text().strip()
        phone = self.phone_field.text().strip()
        website = self.personal_website.text().strip()

        cover_letter_generator = CoverLetterGenerator(applicant_name=applicant_name,
                                                      hr_name=hr_name,
                                                      email=email,
                                                      phone=phone,
                                                      company=company,
                                                      position=position,
                                                      website=website,
                                                      background_color=self.pdf_background_color)

        result = cover_letter_generator.generate()
        if result:
            pop_up = CompletionPopUp()
            pop_up.display(result=result)
