from utils.patterns import Singleton
from utils.file_readers import read_json


class GuiConfig(dict, metaclass=Singleton):
    filename = "config_files/gui_configuration/gui_config.json"

    def __init__(self):
        super().__init__(read_json(self.filename))

        self.title = self["title"]
        self.app_icon = self["app_icon"]
        self.window_size = self["window_size"]
        self.css_style_sheet_fp = self["css_style_sheet_fp"]