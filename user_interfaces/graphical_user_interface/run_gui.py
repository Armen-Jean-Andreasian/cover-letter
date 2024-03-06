from .main_frame import QApplication, MainFrame


def run_gui():
    app = QApplication([])
    window = MainFrame()
    app.exec_()
