def reverse_string(text: str) -> str:
    """
    Take a string and reverse it using slicing technique
    :param text: string to be reversed.
    :return: reversed string
    """
    return text[-1::-1]


def capitalize_text(text: str) -> str:
    """
    Take a string and capitalize it using capitalize method.
    :param text: string to be capitalized.
    :return: capitalized string
    """
    return text.capitalize()
