from services.auth_service import AuthService
from services.customer_service import CustomerService
from menus.admin_menu import AdminMenu
from menus.customer_menu import CustomerMenu
from menus.mechanic_menu import MechanicMenu

class MainMenu:
    def start(self):
        while True:
            print("\n")
            print("=" * 50)
            print("VEHICLE SERVICE SYSTEM")
            print("=" * 50)

            print("1. Admin Login")
            print("2. Customer Login")
            print("3. Mechanic Login")
            print("4. Customer Registration")
            print("5. Exit")

            choice = input("Enter choice: ").strip()

            try:
                if choice == "1":
                    self.admin_login()

                elif choice == "2":
                    self.customer_login()

                elif choice == "3":
                    self.mechanic_login()

                elif choice == "4":
                    self.customer_registration()

                elif choice == "5":
                    print("\nThank You.")
                    break

                else:
                    print("\nInvalid Choice.")

            except Exception as e:
                print(f"\nError: {e}")

    def admin_login(self):
        print("\nADMIN LOGIN")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        admin = AuthService.admin_login(username, password)

        if admin:
            print("\nLogin Successful.")
            AdminMenu().start()

        else:
            print("\nInvalid Credentials.")

    def customer_login(self):

        print("\nCUSTOMER LOGIN")
        customer_id = input("Customer ID: ").strip()
        password = input("Password: ").strip()
        customer = (AuthService.customer_login(customer_id, password))
        
        if customer:
            print("\nLogin Successful.")
            CustomerMenu(customer.customer_id).start()

        else:
            print("\nInvalid Credentials.")

    def mechanic_login(self):
        print("\nMECHANIC LOGIN")
        mechanic_id = input("Mechanic ID: ").strip()
        password = input("Password: ").strip()
        mechanic = (AuthService.mechanic_login(mechanic_id, password))

        if mechanic:
            print("\nLogin Successful.")
            MechanicMenu(mechanic.mechanic_id).start()

        else:
            print("\nInvalid Credentials.")

    def customer_registration(self):
        print("\nCUSTOMER REGISTRATION")
        name = input("Name: ").strip()
        mobile = input("Mobile: ").strip()
        email = input("Email: ").strip()
        address = input("Address: ").strip()
        password = input("Password: ").strip()
        customer = (CustomerService.add_customer(name, mobile, email, address, password))

        print(f"\nRegistration Successful.")
        print(f"Customer ID: "f"{customer.customer_id}")