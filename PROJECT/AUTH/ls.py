from PROJECT.AUTH.loggin import Loggin
from PROJECT.WETER.t_singup import Login

def menu():

        while True:

            print("\n========== RESTAURANT MANAGEMENT ==========")
            print("1. Admin Login")
            print("2. Staf Login")
            print("3. Exit")

            choice = input("Enter Choice: ").strip()

            if choice == "1":
                Loggin()

            elif choice == "2":
                 Login()    

            elif choice == "3":
                print("\nThank you for using Restaurant Management System.")
                break

            else:
                print("Invalid choice. Please select 1 to 3.")
                
    

if __name__ == "__main__":
    menu()