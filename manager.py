from password import generate_password
import json


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

    print()
    print(f"Your generated password: {password}")


def get_account_password(website):
    with open("data.json", "r", encoding="utf-8") as file:
        file_data = json.load(file)

        for item in file_data:
            if item.get("website") == website:
                print(item)


def get_all_passwords():
    with open("data.json", "r", encoding="utf-8") as file:
        file_data = json.load(file)

        for item in file_data:
            print(item)


def main():
    temp = int(input("0 - create account\t1 - get password\n--> "))

    if temp == 0:
        website = input("website: ")
        login = input("login: ")

        create_account(website, login)

    elif temp == 1:
        website = input("website: ")

        get_account_password(website)

    else:
        print("Invalid command")


if __name__ == "__main__":
    main()
