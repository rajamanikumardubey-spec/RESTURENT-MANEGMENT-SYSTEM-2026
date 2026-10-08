from PROJECT.MENU.food_menu import view_menu
from PROJECT.BOOKING.table__boking import main 
from PROJECT.ORDERS.food_order import menu3
from PROJECT.BILLING.bill import menu4


def waitstaff_dhasbod():
    while True:
        print("===============================")
        print("======== WAITSTAFF DASHBOARD ========")
        print("===============================")

        print("1 . View Menu")
        print("2 . Billing")
        print("3 . Table Booking")
        print("4 . Food Orders")
        print("5 . Logout")

        choice = input("Please enter your Choice: ").strip()

        if choice == "1":
            view_menu()

        elif choice == "2":
            menu4()

        elif choice == "3":
            main()

        elif choice == "4":
            menu3()

        elif choice == "5":
            print("Exit, Thank You ")
            break

        else:
            print("Invalid choice, Please Select 1,2,3,4 or 5")




