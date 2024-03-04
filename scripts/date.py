from datetime import datetime


def date_today() -> str:
    today = datetime.today()
    formatted_date = today.strftime("%d %b %Y")
    return formatted_date
