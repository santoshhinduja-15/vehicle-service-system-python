from services.customer_service import CustomerService
from services.vehicle_service import VehicleService
from services.service_request_service import ServiceRequestService
from services.history_service import HistoryService

class CustomerMenu:
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def start(self):
        while True:
            print("\n")
            print("=" * 50)
            print("CUSTOMER MENU")
            print("=" * 50)

            print("1. View Profile")
            print("2. Update Profile")
            print("3. My Vehicles")
            print("4. Add Vehicle")
            print("5. Create Service Request")
            print("6. View Service History")
            print("7. Logout")

            choice = input("Enter Choice: ").strip()

            try:
                if choice == "1":
                    self.view_profile()

                elif choice == "2":
                    self.update_profile()

                elif choice == "3":
                    self.view_vehicles()

                elif choice == "4":
                    self.add_vehicle()

                elif choice == "5":
                    self.create_service_request()

                elif choice == "6":
                    self.view_service_history()

                elif choice == "7":
                    print("\nLogged Out Successfully.")
                    break

                else:
                    print("\nInvalid Choice.")

            except Exception as e:
                print(f"\nError: {e}")

    def view_profile(self):
        customer = (CustomerService.get_customer_by_id(self.customer_id))

        if customer is None:
            print("\nCustomer Not Found.")
            return

        print("\n------------------")

        print(f"Customer ID: "f"{customer.customer_id}")
        print(f"Mobile: "f"{customer.mobile}")
        print(f"Email: "f"{customer.email}")
        print(f"Address: "f"{customer.address}")

    def update_profile(self):
        customer = (CustomerService.get_customer_by_id(self.customer_id))

        if customer is None:
            raise ValueError("Customer not found." )

        name = input("Name: ").strip()
        mobile = input("Mobile: ").strip()
        email = input("Email: ").strip()
        address = input("Address: ").strip()
        CustomerService.update_customer(self.customer_id,name,mobile,email, address)
        print("\nProfile Updated Successfully.")

    def view_vehicles(self):
        vehicles = VehicleService.get_vehicles_by_customer(self.customer_id)

        if not vehicles:
            print("\nNo Vehicles Found.")
            return

        for vehicle in vehicles:
            print("\n------------------")
            print(f"Vehicle ID: "f"{vehicle.vehicle_id}")
            print(f"Vehicle Number: "f"{vehicle.vehicle_number}")
            print(f"Vehicle Type: "f"{vehicle.vehicle_type}")
            print(f"Company: "f"{vehicle.company}")
            print(f"Model: "f"{vehicle.model}")
            print(f"Year: "f"{vehicle.manufacturing_year}")

    def add_vehicle(self):
        vehicle_number = input("Vehicle Number: ").strip()
        vehicle_type = input("Vehicle Type: ").strip()
        company = input("Company: ").strip()
        model = input("Model: ").strip()
        year = input("Manufacturing Year: ").strip()

        vehicle = (
            VehicleService.add_vehicle(
                self.customer_id,
                vehicle_number,
                vehicle_type,
                company,
                model,
                year
            )
        )

        print(f"\nVehicle Added: "f"{vehicle.vehicle_id}")

    def create_service_request(self):
        vehicle_id = input("Vehicle ID: ").strip()
        service_type = input("Service Type: ").strip()
        problem_description = input("Problem Description: ").strip()

        request = (
            ServiceRequestService.create_request(
                self.customer_id,
                vehicle_id,
                service_type,
                problem_description
            )
        )
        print(f"\nRequest Created: "f"{request.request_id}")

    def view_service_history(self):
        requests = (HistoryService.get_customer_history(self.customer_id))
        if not requests:
            print("\nNo Service History Found.")
            return

        for request in requests:
            print("\n------------------")
            print(f"Request ID: "f"{request.request_id}")
            print(f"Vehicle ID: "f"{request.vehicle_id}")
            print(f"Service Type: "f"{request.service_type}")
            print(f"Problem: "f"{request.problem_description}")
            print(f"Request Date: "f"{request.request_date}")
            print(f"Status: "f"{request.status}")