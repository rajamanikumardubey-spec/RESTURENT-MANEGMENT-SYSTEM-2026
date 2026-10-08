import json
import os
from PROJECT.LOGS.error import log_info, log_error


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ORDER_FILE = os.path.join(BASE_DIR, "DATABASE", "order.json")
BILL_FILE = os.path.join(BASE_DIR, "DATABASE", "bill.json")


def load_orders():
    if not os.path.exists(ORDER_FILE):
        return []

    with open(ORDER_FILE, "r") as file:
        return json.load(file)

def load_bills():
    try:
        with open(BILL_FILE, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_bills(bills):

    with open(BILL_FILE, "w") as file:
        json.dump(bills, file, indent=4)

def bill_ganret():

    orders = load_orders()
    bills = load_bills()

    if not orders:
        log_error("No orders found")
        print("No orders found")
        return

    order_id = input("Enter Order ID: ").strip()

    for bill in  bills:
        if bill["order_id"] == order_id:
            log_info("Bill already generated for this Order ID")
            print("Bill already generated for this Order ID")
            return
            

    bill_items = []
    total = 0

    for order in orders:

        if order["order_id"] == order_id:

            item = order["item"]
            qty = order["quantity"]
            price = order["price"]

            amount = qty * price
            total += amount

            bill_items.append({
                "item": item,
                "quantity": qty,
                "price": price,
                "amount": amount,
                "order_id": order_id
            })


    if not bill_items:
        log_info("Order ID not found")
        print("Order ID not found")
        return

    print("\n================ BILL ================")

    print("Order ID     :", order_id)

    for item in bill_items:

        print(
            f'{item["item"]} x {item["quantity"]} = ₹{item["amount"]}'
        )

    discount = total * 10 / 100
    after_discount = total - discount

    print("--------------------------------")
    print(f"Subtotal       : {total:.0f}") 
    print(f"Discount (10%) : {discount:.0f}")
    print(f"After Discount : {after_discount:.0f}")


    gst = after_discount * 5 / 100
    Grand_Total = after_discount + gst


    print("--------------------------------")
    print(f"After discount   : {after_discount:.0f}")
    print(f"GST     :          {gst:.0f}")
    print(f"Grand Total       : {Grand_Total:.0f}")
    print("--------------------------------")

    print("\n========== PAYMENT ==========")
    print("1. UPI")
    print("2. Cass")
    print("3. Exit")

    payment_method = ""
    payment_status = ""


    choice = input("Select Payment Option: ").strip()

    if choice == "1":

        print("\n========== UPI PAYMENT ==========")
        print(f"Amount to Pay: {Grand_Total}")

        confirm = input("Confirm Payment? (yes/no): ").strip().lower()

        if confirm == "yes":
            payment_method = "UPI"
            payment_status = "Conform"

            log_info("Payment Successful")
            print("\nPayment Successful")

        else:
            log_info("Payment Cencle")
            print("Payment Cencle") 
            return   


    elif choice == "2":
        print("\n========== CASS PAYMENT ==========")
        print(f"Amount to Pay: {Grand_Total}")

        confirm = input("Confirm Payment? (yes/no): ").strip().lower()

        if confirm == "yes":
            payment_method = "Cass"
            payment_status = "Conform"

            log_info("Payment Successful")
            print("\nPayment Successful")

        else:
            log_info("Payment Cencle")
            print("Payment Cencle") 
            return
            

    elif choice == "3":
        log_info("Exit")
        print("Exit")

    else:
        print("Invalid Payment Option.")
        return


    bills = load_bills()

    bill = {
        "order_id": order_id,
        "items": bill_items,
        "subtotal": total,
        "discount": discount,
        "after_discount": after_discount,
        "gst": gst,
        "Grand_Total": Grand_Total,
        "payment_method": payment_method,
        "payment_status": payment_status
        }

    bills.append(bill)

    save_bills(bills)

    log_info("Bill Generated Successfully")
    print("\nBill Generated Successfully")

    



def view_bills():

    bills = load_bills()

    if not bills:
        log_error("No bills found")
        print("No bills found")
        return

    print("\n==========VIEW BILLS ==========")

    for number, bill in enumerate(bills, start=1):

        print(f"\nBill No : {number}")

        for item in bill["items"]:
        
            print("---------------------------")
            print("Order ID :",    item["order_id"])
            print("Item     :", item["item"])
            print("Quantity :", item["quantity"])
            print("Price    :", item["price"])
            print("Amount   :", item["amount"])
            print("---------------------------")

        print(f"Subtotal :       {bill['subtotal']:.0f}")
        print(f"Discount (10%) : {bill['discount']:.0f}")
        print(f"after_discount : {bill['after_discount']:.0f}")
        print(f"GST 5%   :       {bill['gst']:.0f}")
        print(f"Grand Total    : {bill['Grand_Total']:.0f}")
        print(f"payment_method : {bill['payment_method']}")
        print(f"payment_status : {bill['payment_status']}")
   

def menu4():

    while True:

        print("\n========== BILLING ==========")

        print("1. Bill Generate")
        print("2. View Bill")
        print("3. Exit")

        choice = input("Please enter your choice: ").strip()

        if choice == "1":
            bill_ganret()


        elif choice == "2":
            view_bills()

        elif choice == "3":
            print("Exit")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu4()