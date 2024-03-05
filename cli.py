from utils import take_input
from source import CoverLetterGenerator


def main():
    name = take_input("Enter your full name: ")
    company = input("Enter the company name: ")
    position = input("Enter the position you're applying for: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")

    cover_letter = CoverLetterGenerator(name, company, position, email, phone)
    cover_letter.generate()


if __name__ == "__main__":
    main()
