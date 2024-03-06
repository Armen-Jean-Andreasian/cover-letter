from utils.file_readers import read_ini, read_text


path = "configuration.ini"

greeting_txt_file, body_txt_file, footer_txt_file = read_ini(
    ini_path=path,
    items=(
        ("txt_filepaths", "greeting_txt"),
        ("txt_filepaths", "body_txt"),
        ("txt_filepaths", "footer_txt")
    )
)

GREETING_TEXT = read_text(greeting_txt_file)
BODY_TEXT = read_text(body_txt_file)
FOOTER_TEXT = read_text(footer_txt_file)
