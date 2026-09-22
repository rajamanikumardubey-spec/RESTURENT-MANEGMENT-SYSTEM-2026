from .singup import Signup
from .loggin import Loggin
from PROJECT.DASHBOARD.admin__dhasbod import admin_dhasbod 
from PROJECT.DASHBOARD.waitstaff__dhasbod import waitstaff_dhasbod 


def menu():

    while True:

        print("\n========== RESTAURANT MANAGEMENT ==========")
        print("1😊. Signup")
        print("2😊. Login")
        print("3👍. Admin Dhasbod")
        print("4👍. Waitstaff Dhasbod")
        print("4😎. exit")

        choice = input("Enter Choice: ").strip()

        if choice == "1":

            signup = Signup()
            signup.signup()

        elif choice == "2":

            login = Loggin()
            login.loggin()

        elif choice == "3":
            admin_dhasbod()

        elif choice == "4":
            waitstaff_dhasbod()

            
            

        elif choice == "4":

            print("\nThank you for using Restaurant Management System.")
            break

        else:
            print("Invalid choice. Please select 1, 2 or 3.")


menu()
