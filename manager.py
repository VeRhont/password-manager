import json

from password import generate_password
from encryption import encryption
from decryption import decryption


def print_item(data):
    print()
    print(f"website: {data['website']}")
    print(f"login: {data['login']}")
    print(f"password: {data['password']}")
    print()


def encrypt(func):
    def wrapper(*args):
        decryption("data.json.crp", "05070524390")
        func(*args)
        encryption("data.json", "05070524390")
    return wrapper


@encrypt
def create_account(website, login):
    password = generate_password()

    user_data = {
        "website": website,
        "login": login,
        "password": password
    }

    with open("data.json", "r", encoding="utf-8") as file:
        file_data = json.load(file)

    with open("data.json", "w") as file:
        file_data.append(user_data)
        json.dump(file_data, file, indent=4)

    print(f"Your generated password: {password}")
    print()


@encrypt
def get_account_password(website):
    with open("data.json", "r", encoding="utf-8") as file:
        file_data = json.load(file)

        for item in file_data:
            if item.get("website") == website:
                print_item(item)


@encrypt
def get_all_passwords():

    with open("data.json", "r", encoding="utf-8") as file:
        file_data = json.load(file)

        for item in file_data:
            print_item(item)


@encrypt
def delete_all():
    with open("data.json", "w", encoding="utf-8") as file:
        file.write("["
                   ""
                   "]")


def get_input(code):
    temp = input("0 - create account\t1 - get password\t2 - get all passwords\t3 - delete all"
                     "\t4 - quit\n--> ")

    try:
        temp = int(temp)
    except:
        print("Invalid input")

    if temp == 0:
        website = input("website: ")
        login = input("login: ")
        create_account(website, login)

    elif temp == 1:
        website = input("website: ")
        get_account_password(website)

    elif temp == 2:
        get_all_passwords()

    elif temp == 3:
        delete_all()

    elif temp == 4:
        quit()
