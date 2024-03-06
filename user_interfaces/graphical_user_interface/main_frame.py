from PyQt5.QtWidgets import QLineEdit, QFormLayout, QPushButton, QWidget, QMessageBox, QApplication
from utils import titleize
from source import CoverLetterGenerator


class MainFrame(QWidget):

    def __init__(self):
        super().__init__()

        self.name_field = QLineEdit()
        self.company_field = QLineEdit()
        self.position_field = QLineEdit()
        self.email_field = QLineEdit()
        self.phone_field = QLineEdit()

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
        self.setWindowTitle("Cover Letter Generator")
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



