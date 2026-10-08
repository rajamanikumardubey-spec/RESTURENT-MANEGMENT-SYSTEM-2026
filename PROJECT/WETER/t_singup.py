import json
import os
import re
import stdiomask
import uuid
from PROJECT.LOGS.error import log_info,log_warning,log_error


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_NAME = os.path.join(BASE_DIR, "DATABASE", "weter.json")


def load_weter():

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_weter(weter):
    with open(FILE_NAME, "w") as file:
        json.dump(weter, file, indent=4)


def Signup():

    weter = load_weter()

    print("\n===== WAITSTAFF SIGN UP =====")

    
    while True:
        name = input("Name: ").strip()

        if len(name) < 3:
            log_info("Name must contain at least 3 characters")
            print("Name must contain at least 3 characters")

        elif not re.fullmatch(r"[A-Za-z ]+", name):
            log_info("Name can contain only letters and spaces")
            print("Name can contain only letters and spaces")

        else:
            break

    
    while True:
        user_id = str(uuid.uuid4().int % 10000000000).zfill(10)

        if not any(u["user_id"] == user_id for u in weter):
            break

    
    while True:
        mobile = input("Mobile: ").strip()

        if not mobile.isdigit() or len(mobile) != 10:
            log_info("Mobile must contain exactly 10 digits")
            print("Mobile must contain exactly 10 digits")

        elif any(u["mobile"] == mobile for u in weter):
            log_info("Mobile number already registered")
            print("Mobile number already registered")

        else:
            break

    
    while True:
        password = stdiomask.getpass("Password: ", mask="*")

        if len(password) < 8:
            log_info("Password must contain at least 8 characters")
            print("Password must contain at least 8 characters")

        elif " " in password:
            log_info("Password cannot contain spaces")
            print("Password cannot contain spaces")

        elif not re.search(r"[A-Z]", password):
            log_info("Password needs an uppercase letter")
            print("Password needs an uppercase letter")

        elif not re.search(r"[a-z]", password):
            log_info("Password needs a lowercase letter")
            print("Password needs a lowercase letter")

        elif not re.search(r"[0-9]", password):
            log_info("Password needs a number")
            print("Password needs a number")

        elif not re.search(r"[^A-Za-z0-9]", password):
            log_info("Password needs a special character")
            print("Password needs a special character")

        else:
            break

    while True:
        confirm = stdiomask.getpass("Confirm Password: ", mask="*")

        if confirm == password:
            break
        log_warning("Password does not match")
        print("Password does not match")

    new_wetar = {
        "name": name,
        "user_id": user_id,
        "mobile": mobile,
        "password": password,
        "role": "Waitstaff"
    }

    weter.append(new_wetar)
    save_weter(weter)

    log_info("Registration Successful")
    print("\nRegistration Successful")

    print("Name    :", name)
    print("User ID :", user_id)
    print("Mobile  :", mobile)
    print("Password:", password)
    print("Role    : Waitstaff")


def Login():

    print("\n========== LOGIN ==========")

    weter = load_weter()

    if not weter:
        log_warning("No registered users found")
        print("No registered users found.")
        return

    user_id = input("Enter User ID: ").strip()
    password = stdiomask.getpass("Enter Password:", mask="@")

    for weter in weter:

        if weter["user_id"] == user_id:

            if weter["password"] == password:

                log_info("Login successful")

                print("\nLogin Successful")
                print("Welcome :", weter["name"])
                print("Role    :", weter["role"])


                if weter["role"].lower() == "waitstaff":

                    log_info("Waitstaff dashboard opened")

                    from PROJECT.DASHBOARD.waitstaff__dhasbod import waitstaff_dhasbod
                    waitstaff_dhasbod()

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

def delete():

    weter = load_weter()

    if not weter:
        log_error("User not found")
        print("User not found")
        return

    user_id = input("User ID: ").strip()

    new_weter = []

    for weter in weter:

        if weter["user_id"].casefold() == user_id.casefold():
            log_error("User not found")
            print("User not found")
            continue

        new_weter.append(weter)

    if len(new_weter) < len(weter):
        save_weter(new_weter)

        log_info("User deleted successfully")
        print("User deleted successfully")
        return

def view_staf():
    weter = load_weter()
    
    if not weter:
        log_error("Weter not found")
        print("Weter not found")
        return

    print("\n=============================================")
    print("                   STAF DETAILS               ")
    print("===============================================")

    for staf in weter:
        print("\nName :", staf["name"]),
        print("User Id:", staf["user_id"]),
        print("Mobile:", staf["mobile"]),
        print("Pssaword:", staf["password"]),
        print("Role:", staf["role"])

        print("===============================================")
         

def menu6():
    while True:
    
            print("\n========== RESTAURANT MANAGEMENT ==========")
            print("1. Login")
            print("2. Signup")
            print("3. Delete")
            print("4. View Staf")
            print("5. Exit")
    
            choice = input("Enter Choice: ").strip()
    
            if choice == "1":
                Login()
    
            elif choice == "2":
                Signup()
    
            elif choice == "3":
                delete()

            elif choice == "4":
                view_staf()    
    
            elif choice == "5":
                print("\nThank you for using Restaurant Management System.")
                break
    
            else:
                print("Invalid choice. Please select 1 to 4.")
    
if __name__ == "__main__":
    menu6()




