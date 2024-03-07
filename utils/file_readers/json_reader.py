import json
from .exception_handler import exception_handler


def read_json(file_name: str) -> dict:
    """
    Loads data from a json file.
    Raises:
        FileNotFoundError: If an error occurs during data loading.
    """
    try:
        with open(file=file_name) as db:
            return json.load(db)
    except FileNotFoundError as fnf_error:
        exception_handler(fnf_error)


def write_json(file_name: str, data: dict, mode='w') -> None:
    """
    Writes data to a json file.
    Raises:
        FileNotFoundError: If an error occurs during data loading.
    """
    try:
        with open(file=file_name, mode=mode) as json_file:
            json.dump(data, json_file, indent=4)
            return None
    except FileNotFoundError as fnf_error:
        exception_handler(fnf_error)


if __name__ == '__main__':
    read_json("sad")
