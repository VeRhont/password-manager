from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice


def generate_password(length=20, nums=True, lower=True, upper=True, special=True):
    available = ""
    if nums: available += digits
    if lower: available += ascii_lowercase
    if upper: available += ascii_uppercase
    if special: available += punctuation

    password = "".join(choice(available) for _ in range(length))
    return password


if __name__ == "__main__":
    print(generate_password())
