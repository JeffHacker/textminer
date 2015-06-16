import re

def phone_numbers(text):
    phone_pattern = r'\(\d{3}\) ?\d{3}\-.{4}'
    return re.findall(phone_pattern, text)


def emails(text):
    email_pattern = r'[\w.\w]+\@\w+\....'
    return re.findall(email_pattern, text)