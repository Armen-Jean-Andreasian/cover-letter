import configparser

initialized = False

if not initialized:
    filepath = 'config/configuration.ini'
    config = configparser.ConfigParser()
    config.read(filepath)

    # constant file paths
    greeting_txt: str = config.get("txt_filepaths", "greeting_txt")
    body_txt: str = config.get("txt_filepaths", "body_txt")
    footer_txt: str = config.get("txt_filepaths", "footer_txt")

    initialized = True
