from utils.file_readers.json_reader import read_json, write_json


class SingletonApplicant(type):
    _instance = None

    def __new__(cls, name, bases, dct):
        if not cls._instance:
            cls._instance = super().__new__(cls, name, bases, dct)
            cls._instance.file = "user_data.json"
        return cls._instance


class Applicant(metaclass=SingletonApplicant):
    """Holds the information provided by user """

    __slots__ = ("applicant_data", "applicant_name", "position", "email", "phone", "website")

    def __init__(self, applicant_name: str = None, position: str = None, email: str = None,
                 phone: str = None, website: str = None):
        # loading last data
        self.applicant_data = self.load_last_data()

        # hold on, wait a minute. you were thinking about setters, right? this approach is better.

        attributes = {"applicant_name": applicant_name, "position": position, "email": email, "phone": phone,
                      "website": website}

        # Achtung, dynamic assignment and in-place update of self.data
        for attribute, value in attributes.items():
            if value:
                setattr(self, attribute, value)
                self.applicant_data[attribute] = value
            else:
                setattr(self, attribute, self.applicant_data[attribute])

    def __str__(self):
        return str(self)

    def load_last_data(self) -> dict:
        return read_json(file_name=self.file)

    def save_new_data(self) -> None:
        return write_json(file_name=self.file, data=self.applicant_data)


class UserData:
    """
    A user data model, utilizing you're gonna need it principle.
    """
    blueprint = {
        "name": "",
        "position": "",
        "email": "",
        "phone": "",
        "website": ""
    }
