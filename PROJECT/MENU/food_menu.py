import json
import os
from PROJECT.LOGS.error import log_info, log_warning, log_error



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_NAME = os.path.join(BASE_DIR, "DATABASE", "menu.json")


CATEGORIES = [
    "Breakfast",
    "Starter",
    "Soup",
    "Salad",
    "Main Course",
    "Rice & Biryani",
    "Roti / Naan",
    "Chinese",
    "Fast Food",
    "Combo",
    "Dessert",
    "Beverages",
    "Tea & Coffee"
]


def load_menu():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_menu(menu):
    with open(FILE_NAME, "w") as file:
        json.dump(menu,file, indent=4)

def view_menu():
    menu = load_menu()

    if not menu:
        log_error("No Menu found")
        print("\nNo Menu found")
        return

    print("\n=============================================")
    print("                  MENU DETAILS                 ")
    print("===============================================")


    for item in menu:

        print(f"ID      : {item['food_id']}")
        print(f"Name : {item['name']}")

        print("--------------------------------------------")

        print(f"Category      : {item['category']}")
        print(f"Price         : ₹{item['price']}")
        print(f"Description   : {item['description']}")
        print(f"Available     : {item['available']}")

        print("===============================================")


def add_menu():
    menu = load_menu()

    if not menu:
        log_error("No Menu found")
        print("\n No Menu Found")
        return

    food_id = input("please enter your food id").strip()
    name = input("please enter your name").strip()

    for food in menu:
        if food["food_id"].casefold() == food_id.casefold():
            log_warning("food id all ready exist")
            print("food id all ready exist")
            return

    for food in menu:
        if food["name"] == name.lower():
            log_warning("food name all ready exist")
            print("food name all ready exist")  


    category = input("Category: ")
    price = int(input("Price: "))
    description = input("description")
    available = input("available")


    item = {
        "food_id": food_id,
        "name": name,
        "category": category,
        "price": price,
        "description":description,
        "available":available
    }

    menu.append(item)
    save_menu(menu)

    log_info("Menu added successfully")   
    print("Menu added successfully")


def delete_menu():
    menu = load_menu()

    if not menu:
        log_warning("Menu not found")
        print("\nMenu Not Found")
        return

    food_id = input("Enter Food ID: ")

    for item in menu:
        if item["food_id"] == food_id.casefold():

            menu.remove(item)
            save_menu(menu)

            log_info("Menu deleted successfully")

            print("Menu deleted successfully")
            return

    log_warning("Food ID not found")

    print("Food ID not found")

def menu1():
    while True:

        print("\n1.View Menu")
        print("2. Add Menu")
        print("3. Delete Menu")
        print("4. exit")

        choice = input("please enter your choice")

        if choice == "1":
            view_menu()

        elif choice == "2":
            add_menu()   

        elif choice == "3":
            delete_menu()

        elif choice == "4":
            print("exit")  
            break    

        else:
            print("envelid choic")    
        
if __name__ == "__main__":
    menu1()