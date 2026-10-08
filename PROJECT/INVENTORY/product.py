import json
import os
from PROJECT.LOGS.error import log_error, log_info, log_warning


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_NAME = os.path.join(BASE_DIR, "DATABASE", "product.json")


def load_product():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return {"materials": []}


def save_product(product):
    with open(FILE_NAME, "w") as file:
        json.dump(product, file, indent=4)


def view_product():
    product = load_product()

    if not product["materials"]:
        log_error("No products found:" + product)
        print("\nNo products found.")
        return

    print("\n========== PRODUCT LIST ==========")

    for i, material in enumerate(product["materials"], start=1):
        print(f"{i}. {material}")


def add_product():
    product = load_product()

    if not product:
        log_error("Product data not found")
        print("\nProduct not found")
        return

    name = input("Please enter your product: ").strip()

    for material in product["materials"]:

        if material.casefold() == name.casefold():
            log_warning("Product already exists: " + name)
            print("Product already exists!")
            return

    product["materials"].append(name)

    save_product(product)

    log_info("Product added successfully: " + name)

    print("Product added successfully.")


def del_product():
    product = load_product()

    if not product["materials"]:
        log_warning("No products found")
        print("\nNo products found.")
        return

    name = input("Please enter your product: ").strip()

    for material in product["materials"]:

        if material.casefold() == name.casefold():
            product["materials"].remove(material)

            save_product(product)

            log_info("Product deleted successfully: " + name)

            print("Product deleted successfully.")
            return

    log_warning("Product not found: " + name)

    print("Product not found.")


def menu2():

    while True:

        print("\n========== INVENTORY ==========")
        print("1. View Product")
        print("2. Add Product")
        print("3. Delete Product")
        print("4. Exit")

        choice = input("Please enter your choice: ").strip()

        if choice == "1":
            view_product()

        elif choice == "2":
            add_product()

        elif choice == "3":
            del_product()

        elif choice == "4":
            print("Exit")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu2()