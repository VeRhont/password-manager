from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice


def generate_password(length=8, nums=True, lower=False, upper=False, special=False):
    available = nums and digits
    available += lower and ascii_lowercase
    available += upper and ascii_uppercase
    available += special and punctuation

    return available


if __name__ == '__main__':
    pass