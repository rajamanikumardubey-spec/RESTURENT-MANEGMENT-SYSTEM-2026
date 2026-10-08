import json
import os
import stdiomask
from PROJECT.LOGS.error import log_info,log_warning



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_NAME = os.path.join(BASE_DIR, "DATABASE", "users.json")


def load_users():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def Loggin():

    print("\n========== LOGIN ==========")

    users = load_users()

    if not users:
        log_warning("No registered users found")
        print("No registered users found.")
        return

    user_id = input("Enter User ID: ").strip()
    password = stdiomask.getpass("Enter Password:", mask="@")

    for user in users:

        if user["user_id"] == user_id:

            if user["password"] == password:

                log_info("Login successful")

                print("\nLogin Successful")
                print("Welcome :", user["name"])
                print("Role    :", user["role"])

                if user["role"].lower() == "admin":

                    log_info("Admin dashboard opened")

                    from PROJECT.DASHBOARD.admin__dhasbod import admin_dhasbod
                    admin_dhasbod()

                else:

                    log_warning("Invalid user role")
                    print("Invalid user role.")

                return

            else:

                log_warning("Incorrect password for User ID")
                print("Incorrect Password.")
                return

    log_warning("User ID not found")
    print("User ID not found.")

if __name__ == "__main__":
    Loggin()