from utils import InputError


def titleize(text: str) -> str:
    """Title the given sting by grammar, ignores uppercase-only words"""

    # yet take_input function can't provide non str, however this block is rather for the future scaling
    if type(text) is not str:
        raise InputError(given_object=text, func_name=titleize.__name__, accepted_type=str)

    lower_words = ["a", "an", "the", "and", "but", "or", "for", "nor", "on", "at", "to", "by", "with", "in", "of"]

    words = text.strip().split()
    # if more than one word in text
    if len(words) > 1:
        title_case_words = []

        for word in words:
            # if the word contains non-letters
            if not word.isalpha():
                title_case_words.append(word)
            else:
                # if the word contains upper letters only
                if word.isupper():
                    title_case_words.append(word)
                else:
                    # if the 'lowercased' word is not in lower_words
                    if word.lower() not in lower_words:
                        title_case_words.append(word.capitalize())
                    else:
                        title_case_words.append(word.lower())
        return " ".join(title_case_words)

    else:
        # if one word contains uppercase letters only or contains non-letters
        if text.isupper() or not text.isalpha():
            return text
        else:
            return text.capitalize()
