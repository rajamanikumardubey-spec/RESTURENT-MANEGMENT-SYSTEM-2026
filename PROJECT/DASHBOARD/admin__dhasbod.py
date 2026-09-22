from PROJECT.MENU.menu import menu_management
from PROJECT.BOOKING.table__boking import main 
def admin_dhasbod():
    print("=============😊😊😊😊😊😊😊===========") 
    print("==============ADMIN DASHBOARD=============") 
    print("=============😊😊😊😊😊😊😊===========") 


    
    print("1👍.  View Menu")
    print("2😊. Inventory")
    print("3😎. Staff Management")
    print("4🤔. Billing")
    print("5👍. Booking")
    print("6😎. Orders")
    print("7😊. Logs")
    print("8 🤦‍♂️. Exit")


    choice = input("Enter Choice: ").strip()

    if choice == "1":
        menu_management()
        

    elif choice == "2":
        print("Inventory Section in progress😊")

    elif choice == "3":
        print("Staff Management Section in progress😊")

    elif choice == "4":
        print("Billing Section in progress😊")

    elif choice == "5":
        main()

    elif choice == "6":
        print("Orders Section in progress😊") 

    elif choice == "7":
        print("Logs Section in progress😊")

    elif choice =="8":
        print("Exit 🤦‍♂️")

    else:
        print("Invalid choice. Please select 1,2,3,4,5,6,7 or 8.")
