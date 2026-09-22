import json
import os


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

    except FileNotFoundError:
        return []


def save_menu(menu):
    with open(FILE_NAME, "w") as file:
        json.dump(menu, file, indent=4)


def generate_food_id(menu):
    if not menu:
        return "F001"

    numbers = []

    for item in menu:
        number = int(item["food_id"][1:])
        numbers.append(number)

    new_number = max(numbers) + 1

    return f"F{new_number:03d}"


def get_name():
    while True:
        name = input("Food Name: ").strip()

        if not name:
            print("Food name cannot be empty!😊")
        elif len(name) < 2:
            print("Food name must contain at least 2 characters!👍")
        elif not all(char.isalpha() or char.isspace() for char in name):
            print("Food name can contain only letters and spaces!😎")
        else:
            return name


def get_price():
    while True:
        try:
            price = float(input("Price:"))

            if price <= 0:
                print("Price must be greater than 0!👍")
            else:
                return price

        except ValueError:
            print("Please enter a valid price!😊")


def get_description():
    while True:
        description = input("Description:😎 ").strip()

        if not description:
            print("Description cannot be empty!👍")
        else:
            return description


def select_category():
    print("\nSelect Category:😎")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    while True:
        try:
            choice = int(input("Enter choice:😊 "))

            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]

            print("Invalid category choice!😎")

        except ValueError:
            print("Please enter a number!😊")


def get_availability():
    while True:
        choice = input(
            "Available? (yes/no): "
        ).strip().lower()

        if choice == "yes":
            return True

        if choice == "no":
            return False

        print("Please enter yes or no!😊")


def add_food():
    menu = load_menu()

    print("\n========== ADD FOOD ==========😊")

    food = {
        "food_id": generate_food_id(menu),
        "name": get_name(),
        "category": select_category(),
        "price": get_price(),
        "description": get_description(),
        "available": get_availability()
    }

    menu.append(food)
    save_menu(menu)

    print("\nFood added successfully!🤔")
    print(f"Food ID😊: {food['food_id']}")


def view_food():
    menu = load_menu()

    print("\n========== MENU ==========😎")

    if not menu:
        print("No food available!😊")
        return

    for category in CATEGORIES:

        category_items = [
            item for item in menu
            if item["category"] == category
        ]

        if category_items:
            print(f"\n--- {category} ---👍")

            for item in category_items:
                status = "Available" if item["available"] else "Not Available"

                print(
                    f"{item['food_id']} | "
                    f"{item['name']} | "
                    f"₹{item['price']} | "
                    f"{status}"
                )
                print(f"Description😊: {item['description']}")
                


def find_food(menu):
    food_id = input("Enter Food ID:😎 ").strip().upper()

    for item in menu:
        if item["food_id"] == food_id:
            return item

    return None


def update_food():
    menu = load_menu()

    print("\n========== UPDATE FOOD ==========😊")

    food = find_food(menu)

    if food is None:
        print("Food not found!😎")
        return

    print(f"\nFood: {food['name']}👍")

    print("\n1. Update Name")
    print("2. Update Category")
    print("3. Update Price")
    print("4. Update Description")
    print("5. Update Availability")

    while True:
        try:
            choice = int(input("Enter choice:😊"))

            if choice == 1:
                food["name"] = get_name()

            elif choice == 2:
                food["category"] = select_category()

            elif choice == 3:
                food["price"] = get_price()

            elif choice == 4:
                food["description"] = get_description()

            elif choice == 5:
                food["available"] = get_availability()

            else:
                print("Invalid choice!👍")
                continue

            save_menu(menu)

            print("Food updated successfully!👍")
            break

        except ValueError:
            print("Please enter a valid number!😎")


def delete_food():
    menu = load_menu()

    print("\n========== DELETE FOOD ==========😊")

    food = find_food(menu)

    if food is None:
        print("Food not found!👍")
        return

    print(f"Food😊: {food['name']}")

    confirm = input("Are you sure? (yes/no): ").strip().lower()

    if confirm == "yes":
        menu.remove(food)
        save_menu(menu)

        print("Food deleted successfully!👍")

    else:
        print("Delete cancelled!😊")


def menu_management():
    while True:

        print("\n==========😊😊 MENU MANAGEMENT 😊😊==========")

        print("1. ➕ Add Food")
        print("2. 👀 View Food")
        print("3. ✏️ Update Food")
        print("4. 🗑️ Delete Food")
        print("5. 🚪 Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_food()

        elif choice == "2":
            view_food()

        elif choice == "3":
            update_food()

        elif choice == "4":
            delete_food()

        elif choice == "5":
            break

        else:
            print("Invalid choice!🤦‍♂️")

