from .main_frame import MainFrame
from PyQt5.QtWidgets import QApplication


def run_gui():
    app = QApplication([])
    window = MainFrame()
    app.exec_()
