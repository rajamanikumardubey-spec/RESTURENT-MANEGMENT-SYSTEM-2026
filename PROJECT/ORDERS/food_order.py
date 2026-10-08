import json
import os
import uuid
from PROJECT.LOGS.error import log_info, log_warning, log_error
from PROJECT.MENU.food_menu import view_menu

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MENU_FILE = os.path.join(BASE_DIR, "DATABASE", "menu.json")
ORDER_FILE = os.path.join(BASE_DIR, "DATABASE", "order.json")


def load_menu():
    try:
        with open(MENU_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def load_order():
    try:
        with open(ORDER_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []



def save_orders(orders):
    with open(ORDER_FILE, "w") as file:
        json.dump(orders, file, indent=4)


def view_order():

    orders = load_order()

    if not orders:
        log_error("No orders found" + str(orders))
        print("\nNo orders found.")
        return

    print("\n=============================================")
    print("                         ORDER DETAILS")
    print("=================================================")

    for order in orders:

        print(f"Order ID      : {order['order_id']}")
        
        print("-------------------------------------------")

        print(f"Food ID       : {order['food_id']}")
        print(f"Item          : {order['item']}")
        print(f"Category      : {order['category']}")
        print(f"Quantity      : {order['quantity']}")
        print(f"Price         : ₹{order['price']}")
        print(f"Description   : {order['description']}")
        print(f"Available     : {order['available']}")

        print("==============================================")
    

def order_book():

    orders = load_order()
    menu = load_menu()

    if not menu:
        log_error("Menu Not Found")
        print("\nMenu Not Found")
        return

    food_id = input("Food ID: ").strip()

    try:

        quantity = float(input("Quantity: "))
        
        if quantity <= 0:
            log_info("Number 0 ya usse kam nahi ho sakta")
            print("Number 0 ya usse kam nahi ho sakta")
            return


    except ValueError:
        print("Please enter a valid number.")
        return    


    for food in menu:

        if food["food_id"].casefold() == food_id.casefold():

            order = {
                "food_id": food["food_id"],
                "order_id": str(uuid.uuid4()),
                "item": food["name"],
                "price": food["price"],
                "quantity": quantity,
                "category": food["category"],
                "description": food["description"],
                "available": food["available"]
            }

            orders.append(order)
            save_orders(orders)

            log_info("Order booked successfully: " + order["order_id"])

            print("\nOrder Booked Successfully!")
            print("Food ID      :", order["food_id"])
            print("Order ID     :", order["order_id"])
            print("Item         :", order["item"])
            print("Price        :", order["price"])
            print("Quantity     :", order["quantity"])

            return

    log_warning("Food ID not found: " + food_id)
    print("Food ID not found")


def order_delete():

    orders = load_order()

    if not orders:
        log_error("No order found")
        print("\nNo order found")
        return

    order_id = input("Order ID: ").strip()

    new_orders = []

    for order in orders:

        if order["order_id"].casefold() == order_id.casefold():
            continue

        new_orders.append(order)

    if len(new_orders) < len(orders):

        save_orders(new_orders)

        log_info("Order deleted successfully")
        print("Order deleted successfully")

    else:

        log_warning("Invalid order ID")
        print("Invalid order id")    



def item_add():

    orders = load_order()

    if not orders:
        log_warning("Order not found")
        print("\nOrder Not Found")
        return

    menu = load_menu()

    if not menu:
        log_error("Menu not found")
        print("\nMenu Not Found")
        return

    order_id = input("Order ID: ").strip()
    name = input("Item Name: ").strip()

    try:

        quantity = float(input("Quantity: "))

        if quantity <= 0:
            log_info("Number 0 ya usse kam nahi ho sakta")
            print("Number 0 ya usse kam nahi ho sakta")
            return
        
    except ValueError:
        log_warning("Invalid quantity")
        print("Invalid quantity")
        return

    for order in orders:

        if order["order_id"].casefold() == order_id.casefold():

            for food in menu:

                if food["name"].lower() == name.lower():

                    new_order = {
                        "food_id": food["food_id"],
                        "order_id": order["order_id"],
                        "item": food["name"],
                        "price": food["price"],
                        "quantity": quantity,
                        "category": food["category"],
                        "description": food["description"],
                        "available": food["available"]
                    }

                    orders.append(new_order)
                    save_orders(orders)

                    log_info("Item added successfully")

                    print("Item added successfully")
                    return

            log_warning("Invalid item name")
            print("Invalid item name")
            return

    log_warning("Invalid order ID")
    print("Invalid order ID")
     


def item_delete():

    orders = load_order()

    if not orders:
        log_warning("Order not found")
        print("\nOrder Not Found")
        return

    order_id = input("Order ID: ").strip()
    name = input("Item Name: ").strip()

    for order in orders:

        if (order["order_id"].casefold() == order_id.casefold() and order["item"].lower() == name.lower()):

            orders.remove(order)
            save_orders(orders)

            log_info("Item deleted successfully")

            print("Item deleted successfully")
            return

    log_warning("Invalid Order ID or Item Name")

    print("Invalid Order ID or Item Name")


def menu3():
    while True:

         print("\n1. View Order") 
         print("2. Order Book")  
         print("3. Order Delete")
         print("4. Item Add")
         print("5. Item Delete")
         print("6. View Menu")
         print("7. Exit")

         choice = input("please enter tour Choice")

         if choice == "1":
             view_order()

         elif choice == "2":
             order_book()

         elif choice == "3":
             order_delete()

         elif  choice == "4":
             item_add()

         elif choice == "5":
             item_delete()

         elif choice == "6":
              view_menu()     

         elif choice == "7":
             print("Exit")
             break

         else:
             print("Envelid Choice")     

if __name__ == "__main__":
    menu3()
                            