from PROJECT.MENU.food_menu import menu1
from PROJECT.BOOKING.table__boking import main
from PROJECT.ORDERS.food_order import menu3
from PROJECT.INVENTORY.product import menu2
from PROJECT.BILLING.bill import menu4
from PROJECT.WETER.t_singup import menu6
from PROJECT.LOGS.error import view_error




def admin_dhasbod():
    while True:
        print("\n==========================================")
        print("============== ADMIN DASHBOARD =============")
        print("============================================")

        print("1. View Menu")
        print("2. Inventory")
        print("3. Billing")
        print("4. Table Booking")
        print("5. Food Orders")
        print("6. View Logs Error")
        print("7. Staf Manegment")
        print("8. Logout")

        choice = input("Enter Choice: ").strip()

        if choice == "1":
            menu1()

        elif choice == "2":
            menu2()


        elif choice == "3":
            menu4()

        elif choice == "4":
            main()

        elif choice == "5":
            menu3()

        elif choice == "6":
            view_error()
            

        elif choice == "7":
            menu6()    


        elif choice == "8":
            print("Exit")
            break

        else:
            print("Invalid choice.")