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

GREETING_TEXT = read_text(filepath="resources/text_samples/files/greeting.txt")
BODY_TEXT = read_text(filepath="resources/text_samples/files/body.txt")
FOOTER_TEXT = read_text(filepath="resources/text_samples/files/footer.txt")
