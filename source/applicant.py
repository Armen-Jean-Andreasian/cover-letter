import json


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Applicant(metaclass=Singleton):
    """Holds the information provided by user """

    def __init__(self, company: str = None, name: str = None, position: str = None, email: str = None,
                 phone: str = None):
        # before assigning
        self.data = self.load_data()

        self.company = company

        if name:
            self.name = name
            self.data["name"] = name
        else:
            self.name = self.data["name"]

        if position:
            self.position = position
            self.data["position"] = position
        else:
            self.position = self.data["position"]

        if email:
            self.email = email
            self.data["email"] = email
        else:
            self.email = self.data["email"]

        if phone:
            self.phone = phone
            self.data["phone"] = phone
        else:
            self.phone = self.data["phone"]

    def load_data(self) -> dict:
        return UserData.load_data()

    def save_data(self) -> None:
        return UserData.save_data(data=self.data)


class UserData:
    file = "user_data.json"

    blueprint = {
        "name": "",
        "position": "",
        "email": "",
        "phone": ""
    }

    @staticmethod
    def load_data() -> dict:
        with open(file=UserData.file) as db:
            return json.load(db)

    @staticmethod
    def save_data(data: dict) -> None:
        with open(file=UserData.file, mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        return None
