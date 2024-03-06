from PyQt5.QtWidgets import QLineEdit, QFormLayout, QPushButton, QWidget, QMessageBox
from PyQt5.QtGui import QIcon
from utils.file_readers import read_ini
from utils import titleize
from source import CoverLetterGenerator


class MainFrame(QWidget):
    title = "Cover Letter Generator"
    icon = read_ini(items=(("binary_filepaths", "app_icon"),))[0]
    window_size = (610, 200)

    gui_style = read_ini(items=(("styles_filepaths", "gui_design"),))[0]

    with open(gui_style) as css_file:
        style_sheet = css_file.read()

    def __init__(self):
        super().__init__()

        # set window icon, title, size
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setMinimumSize(*self.window_size)
        self.setMaximumSize(*self.window_size)

        # setting the style
        self.setStyleSheet(self.style_sheet)

        self.name_field = QLineEdit()
        self.name_field.setPlaceholderText("Enter your full name")

        self.company_field = QLineEdit()
        self.company_field.setPlaceholderText("Enter the company name")

        self.position_field = QLineEdit()
        self.position_field.setPlaceholderText("Enter the position")

        self.email_field = QLineEdit()
        self.email_field.setPlaceholderText("Enter your email")

        self.phone_field = QLineEdit()
        self.phone_field.setPlaceholderText("Enter your phone number")

        self.generate_button = QPushButton("Generate Cover Letter")
        self.generate_button.clicked.connect(self.generate_cover_letter)

        layout = QFormLayout()
        layout.addRow("Name:", self.name_field)
        layout.addRow("Company:", self.company_field)
        layout.addRow("Position:", self.position_field)
        layout.addRow("Email:", self.email_field)
        layout.addRow("Phone:", self.phone_field)
        layout.addRow("", self.generate_button)

        self.setLayout(layout)
        self.show()

    def generate_cover_letter(self):
        name = titleize(self.name_field.text())
        company = titleize(self.company_field.text())
        position = titleize(self.position_field.text())
        email = self.email_field.text().strip()
        phone = self.phone_field.text().strip()

        cover_letter = CoverLetterGenerator(name, company, position, email, phone)
        result = cover_letter.generate()

        # Pop-up window
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Success")
        msg_box.setIcon(QMessageBox.Information)

        if result:
            msg_box.setText(result)
        else:
            # Default message
            msg_box.setText("Cover letter generation completed.")

        msg_box.setStandardButtons(QMessageBox.Ok)
        # Show the Pop-up window
        msg_box.exec_()
