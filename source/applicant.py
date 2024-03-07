from utils.file_readers.json_reader import read_json, write_json


class SingletonApplicant(type):
    instances = set()

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)

        instance.file = "user_data.json"  # read only, kill it with fire
        if instance not in cls.instances:
            cls.instances.add(instance)
        return instance


class Applicant(metaclass=SingletonApplicant):
    """Holds the information provided by user """

    __slots__ = ("data", "company",  "name", "position", "email", "phone")

    def __init__(self, company: str = None, name: str = None, position: str = None, email: str = None,
                 phone: str = None):
        # loading last data
        self.data = self.load_last_data()

        self.company = company

        attributes = {"name": name, "position": position, "email": email, "phone": phone}

        # Achtung, dynamic assignment and in-place update of self.data
        for attribute, value in attributes.items():
            if value:
                setattr(self, attribute, value)
                self.data[attribute] = value
            else:
                setattr(self, attribute, self.data[attribute])

    def __str__(self):
        return str(self)

    def load_last_data(self) -> dict:
        return read_json(file_name=self.file)

    def save_new_data(self) -> None:
        return write_json(file_name=self.file, data=self.data)


class UserData:
    """
    A user data model, utilizing you're gonna need it principle.
    """
    blueprint = {
        "name": "",
        "position": "",
        "email": "",
        "phone": ""
    }
