from config import greeting_txt, body_txt, footer_txt


def read_file(filepath):
    with open(filepath) as file:
        return file.read()


GREETING_TEXT = read_file(greeting_txt)
BODY_TEXT = read_file(body_txt)
FOOTER_TEXT = read_file(footer_txt)

