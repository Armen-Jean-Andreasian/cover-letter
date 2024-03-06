from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal


class RGBColorPicker(QWidget):
    colorSelected = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.status = False
        self.color_tuple = None

    def init_ui(self):
        self.setWindowTitle('RGB Color Picker')
        self.layout = QVBoxLayout()

        # Red slider
        self.red_label = QLabel('Red: 0')
        self.red_slider = QSlider(Qt.Orientation.Horizontal)
        self.red_slider.setRange(0, 255)
        self.red_slider.valueChanged.connect(self.update_color)

        # Green slider
        self.green_label = QLabel('Green: 0')
        self.green_slider = QSlider(Qt.Orientation.Horizontal)
        self.green_slider.setRange(0, 255)
        self.green_slider.valueChanged.connect(self.update_color)

        # Blue slider
        self.blue_label = QLabel('Blue: 0')
        self.blue_slider = QSlider(Qt.Orientation.Horizontal)
        self.blue_slider.setRange(0, 255)
        self.blue_slider.valueChanged.connect(self.update_color)

        # Color preview label
        self.color_label = QLabel()
        self.color_label.setFixedSize(100, 100)
        self.update_color()

        # Confirm button
        self.confirm_button = QPushButton('Confirm')
        self.confirm_button.clicked.connect(self.confirm_color)

        # Layout setup
        self.layout.addWidget(self.red_label)
        self.layout.addWidget(self.red_slider)
        self.layout.addWidget(self.green_label)
        self.layout.addWidget(self.green_slider)
        self.layout.addWidget(self.blue_label)
        self.layout.addWidget(self.blue_slider)
        self.layout.addWidget(self.color_label)
        self.layout.addWidget(self.confirm_button)
        # apply layout
        self.setLayout(self.layout)

    def update_color(self):
        red = self.red_slider.value()
        green = self.green_slider.value()
        blue = self.blue_slider.value()
        self.color_label.setStyleSheet(f'background-color: rgb({red}, {green}, {blue})')
        self.red_label.setText(f'Red: {red}')
        self.green_label.setText(f'Green: {green}')
        self.blue_label.setText(f'Blue: {blue}')

    def confirm_color(self):
        """Emits the colorSelected signal with the selected color tuple"""
        red = self.red_slider.value()
        green = self.green_slider.value()
        blue = self.blue_slider.value()
        color_tuple = (red, green, blue)

        self.colorSelected.emit(color_tuple)
        self.close()
