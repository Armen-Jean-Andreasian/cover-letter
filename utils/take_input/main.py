from utils.titleize_input import titleize


def take_input(text: str) -> str:
    """Returns stripped titled input"""
    user_input = input(titleize(text))
    return titleize(user_input)
