import json
import os
import msvcrt



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILE_PATH = os.path.join(
    BASE_DIR,
    "DATABASE",
    "users.json"
)


def load_users():
    with open(FILE_PATH, "r") as file:
        data = json.load(file)

    if isinstance(data, list):
        return data

    print("users.json must contain a list.")
    return []


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
            password += char.decode()
            print("*", end="", flush=True)


class Loggin:

    def __init__(self):
        self.users = load_users()

    def validate_user_id(self):
        while True:
            user_id = input("Enter User ID: ").strip()

            if not user_id:
                print("User ID cannot be empty.")

            elif len(user_id) < 4:
                print("User ID must contain at least 4 characters.")

            elif len(user_id) > 20:
                print("User ID cannot contain more than 20 characters.")

            else:
                return user_id

    def validate_password(self):
        while True:
            print("Enter Password: ", end="", flush=True)
            password = get_password()

            if not password:
                print("Password cannot be empty.")

            elif len(password) < 8:
                print("Password must contain at least 8 characters.")

            else:
                return password

    def loggin(self):
        print("\n========== LOG IN ==========")

        if not self.users:
            print("No registered users found.")
            print("Please register first.")
            return None

        user_id = self.validate_user_id()
        password = self.validate_password()

        for user in self.users:

            if user.get("user_id", "").lower() == user_id.lower():

                if user.get("password") == password:

                    print("\nLogin Successful!")
                    print("Welcome: 😊", user.get("name"))
                    print("Role   : 👍", user.get("role"))

                    return user

                else:
                    print("Incorrect Password.🤦‍♂️")
                    return None

        print("User ID not found.")
        return None
