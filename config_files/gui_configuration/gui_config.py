from utils.patterns import Singleton
from utils.file_readers import read_json


class GuiConfig(dict, metaclass=Singleton):
    json_config_file = "config_files/gui_configuration/gui_config.json"

    def __init__(self):
        super().__init__(read_json(self.json_config_file))

        self.title = self["title"]
        self.app_icon = self["app_icon"]
        self.window_size = self["window_size"]
        self.css_style_sheet_fp = self["css_style_sheet_fp"]