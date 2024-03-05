class Applicant:
    """Holds the information provided by user """

    def __init__(self, name: str, company: str, position: str, email: str, phone: str):
        self.name = name
        self.company = company
        self.position = position
        self.email = email
        self.phone = phone
