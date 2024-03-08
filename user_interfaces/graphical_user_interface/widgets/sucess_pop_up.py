from PyQt5.QtWidgets import QMessageBox


class CompletionPopUp(QMessageBox):
    """A pop-up window showing a status"""
    window_title = "Success"

    def display(self, result: str):
        self.setWindowTitle(self.window_title)
        self.setIcon(QMessageBox.Information)
        self.setStandardButtons(QMessageBox.Ok)

        # showing the on-completion message
        self.setText(result)
        # Show the Pop-up window
        self.exec_()
