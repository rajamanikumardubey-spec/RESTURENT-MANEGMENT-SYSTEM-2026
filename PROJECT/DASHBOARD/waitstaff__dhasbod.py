from PROJECT.MENU.menu import view_food 
from PROJECT.BOOKING.table__boking import main 
def waitstaff_dhasbod():
    print("===============================") 
    print("========WAITSTAFF DASHBOARD========") 
    print("===============================")


    
    print("1😊. View Menu")
    print("2😊. Billing")
    print("3👍. Booking")
    print("4😎. Orders")
    print("5😎. Exit")

    choice = input("Please enter your Choice"). strip()

    if choice == "1":
        view_food()

    elif choice == "2":
        print("Billing Section in progress👍")

    elif choice == "3":
        main()

    elif choice == "4":
        print("Orders Section in progress 🐱‍🚀")

    elif choice == "5":
        print("Exit, Thank You 😊🐱‍🚀😊")

    else:
        print("Envelide choice, Please Select 1,2,3,4 or 5")




