from utils.take_input import take_input
from source import CoverLetterGenerator


def run_cli():
    name = take_input("Enter your full name: ")
    company = take_input("Enter the company name: ")
    hr_name = take_input("HR name: ")
    position = take_input("Enter the position you're applying for: ")
    email = take_input("Enter your email address: ")
    phone = take_input("Enter your phone number: ")
    website = take_input("Enter your website URL for a QR code")

    cover_letter = CoverLetterGenerator(applicant_name=name,
                                        hr_name=hr_name,
                                        email=email,
                                        phone=phone,
                                        company=company,
                                        position=position,
                                        website=website)
    print(cover_letter.generate().replace('<br>', '\n'))
