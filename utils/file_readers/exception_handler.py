import os


def exception_handler(fnf_error):
    file_name = fnf_error.filename
    file_path = os.path.abspath(file_name)
    raise FileNotFoundError(f"The file \"{file_name}\" was not found by \"{file_path}\" location")
