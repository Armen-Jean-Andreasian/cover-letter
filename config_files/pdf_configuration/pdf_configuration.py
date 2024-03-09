from utils.patterns import Singleton
from utils.file_readers import read_json


class PdfConfig(dict, metaclass=Singleton):
    json_config_file = "config_files/pdf_configuration/pdf_config.json"

    def __init__(self):
        super().__init__(read_json(self.json_config_file))

        self.background_color = self["background_color"]
        self.output_file_name_prototype = self["output_file_name_prototype"]
        self.pdf_output_folder = self["pdf_output_folder"]

        self.content_font_family = self["content_font_family"]
        self.content_font_size = self["content_font_size"]
        self.heading_font_family = self["heading_font_family"]
        self.heading_font_size = self["heading_font_size"]
        self.heading_font_style = self["heading_font_style"]