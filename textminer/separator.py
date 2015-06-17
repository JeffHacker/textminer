import re

def phone_number(text):
    area_code = "919"
    # close on this pattern
    phone_num = "\d{3}.\d{4}"
    answer = area_code, phone_num
    # yeild {}

    return re.findall(answer, text)


def money(text):
    symbol = "\$"
    amount = "\d+\.\d+"
    answer = symbol, amount
    return re.findall(answer, text)

