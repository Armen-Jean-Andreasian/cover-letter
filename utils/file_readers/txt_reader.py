def read_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()
