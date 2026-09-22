import json
import os
import re
import msvcrt


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILE_PATH = os.path.join(
    BASE_DIR,
    "DATABASE",
    "users.json"
)


def load_users():
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        print("users.json must contain a list.")
        return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_users(users):
    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)


def get_password():
    password = ""

    while True:
        char = msvcrt.getch()

        if char == b"\r":
            print()
            return password

        elif char == b"\b":
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)

        else:
            try:
                password += char.decode()
                print("*", end="", flush=True)
            except UnicodeDecodeError:
                pass


class Signup:

    def __init__(self):
        self.users = load_users()

    def validate_name(self):
        while True:
            name = input("Enter Full Name: ").strip()

            if not name:
                print("Name cannot be empty.👍")

            elif len(name) < 3:
                print("Name must contain at least 3 characters.👍")

            elif len(name) > 50:
                print("Name cannot contain more than 50 characters.👍")

            elif not re.fullmatch(r"[A-Za-z ]+", name):
                print("Name can contain only letters and spaces.👍")

            elif "  " in name:
                print("Do not use multiple spaces together.👍")

            else:
                return name

    def validate_user_id(self):
        while True:
            user_id = input("Enter User ID: 👍").strip()

            if not user_id:
                print("User ID cannot be empty.👍")

            elif len(user_id) < 4:
                print("User ID must contain at least 4 characters.👍")

            elif len(user_id) > 20:
                print("User ID cannot contain more than 20 characters.👍")

            elif not re.fullmatch(r"[A-Za-z0-9_]+", user_id):
                print("Only letters, numbers and underscore are allowed.👍")

            elif user_id[0].isdigit():
                print("User ID cannot start with a number.👍")

            elif any(
                user.get("user_id", "").lower() == user_id.lower()
                for user in self.users
            ):
                print("This User ID already exists.")

            else:
                return user_id

    def validate_mobile(self):
        while True:
            mobile = input("Enter Mobile Number: 😊").strip()

            if not mobile:
                print("Mobile number cannot be empty.😊")

            elif not mobile.isdigit():
                print("Mobile number must contain digits only.😊")

            elif len(mobile) != 10:
                print("Mobile number must contain exactly 10 digits.😊")

            elif mobile[0] not in "6789":
                print("Mobile number must start with 6, 7, 8 or 9.😊")

            elif len(set(mobile)) == 1:
                print("Please enter a valid mobile number.😊")

            elif any(
                user.get("mobile") == mobile
                for user in self.users
            ):
                print("This mobile number is already registered.")

            else:
                return mobile

    def validate_password(self):
        while True:
            print("Enter Password:👍 ", end="", flush=True)
            password = get_password()

            if not password:
                print("Password cannot be empty.👍")

            elif len(password) < 8:
                print("Password must contain at least 8 characters.👍")

            elif len(password) > 32:
                print("Password cannot contain more than 32 characters.👍")

            elif " " in password:
                print("Password cannot contain spaces.👍")

            elif not re.search(r"[A-Z]", password):
                print("Password must contain uppercase letter.👍")

            elif not re.search(r"[a-z]", password):
                print("Password must contain lowercase letter.👍")

            elif not re.search(r"[0-9]", password):
                print("Password must contain a number.👍")

            elif not re.search(r"[^A-Za-z0-9]", password):
                print("Password must contain a special character.👍")

            else:
                return password

    def confirm_password(self, password):
        while True:
            print("Confirm Password:😊 ", end="", flush=True)
            confirm = get_password()

            if not confirm:
                print("Confirm password cannot be empty.😊")

            elif confirm != password:
                print("Password does not match.😊")

            else:
                return True

    def signup(self):
        print("\n========== WAITSTAFF SIGN UP ==========")

        name = self.validate_name()
        user_id = self.validate_user_id()
        mobile = self.validate_mobile()
        password = self.validate_password()

        self.confirm_password(password)

        new_user = {
            "name": name,
            "user_id": user_id,
            "mobile": mobile,
            "password": password,
            "role": "Waitstaff"
        }

        self.users.append(new_user)
        save_users(self.users)

        print("\nRegistration Successful!😊")
        print("Name   :😊", name)
        print("User ID:👍", user_id)
        print("Mobile :😊", mobile)
        print("Role   : Waitstaff😊")
