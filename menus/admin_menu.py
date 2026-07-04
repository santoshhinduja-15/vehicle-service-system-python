from services.customer_service import CustomerService
from services.vehicle_service import VehicleService
from services.mechanic_service import MechanicService
from services.service_request_service import ServiceRequestService
from services.assignment_service import AssignmentService
from services.billing_service import BillingService
from services.payment_service import PaymentService
from services.report_service import ReportService

class AdminMenu:
    def start(self):
        while True:
            print("\n" + "=" * 60)
            print("ADMIN MENU")
            print("=" * 60)

            print("1. Customer Management")
            print("2. Vehicle Management")
            print("3. Mechanic Management")
            print("4. Service Requests")
            print("5. Mechanic Assignment")
            print("6. Billing")
            print("7. Payments")
            print("8. Reports")
            print("9. Logout")

            choice = input("Enter Choice: ").strip()

            try:
                if choice == "1":
                    self.customer_management()

                elif choice == "2":
                    self.vehicle_management()

                elif choice == "3":
                    self.mechanic_management()

                elif choice == "4":
                    self.service_requests()

                elif choice == "5":
                    self.mechanic_assignment()

                elif choice == "6":
                    self.billing_menu()

                elif choice == "7":
                    self.payment_menu()

                elif choice == "8":
                    self.report_menu()

                elif choice == "9":
                    print("\nLogged Out Successfully.")
                    break

                else:
                    print("\nInvalid Choice.")

            except Exception as e:
                print(f"\nError: {e}")

    # CUSTOMER MANAGEMENT
    def customer_management(self):
        while True:
            print("\n")
            print("=" * 50)
            print("CUSTOMER MANAGEMENT")
            print("=" * 50)

            print("1. Add Customer")
            print("2. View Customers")
            print("3. Update Customer")
            print("4. Delete Customer")
            print("5. Back")

            choice = input("Enter Choice: ").strip()

            try:
                if choice == "1":
                    name = input("Name: ")
                    mobile = input("Mobile: ")
                    email = input("Email: ")
                    address = input("Address: ")
                    password = input("Password: ")

                    customer = (CustomerService.add_customer(name,mobile, email, address, password))
                    print(f"\nCustomer Created: "f"{customer.customer_id}")

                elif choice == "2":
                    customers = (CustomerService.get_all_customers())

                    if not customers:
                        print("\nNo Customers Found.")

                    else:
                        for customer in customers:
                            print("\n------------------")
                            print(f"ID: "f"{customer.customer_id}")
                            print(f"Name: "f"{customer.name}")
                            print(f"Mobile: "f"{customer.mobile}")
                            print(f"Email: "f"{customer.email}")
                            print(f"Address: "f"{customer.address}")

                elif choice == "3":
                    customer_id = input("Customer ID: ")
                    name = input("New Name: ")
                    mobile = input("New Mobile: ")
                    email = input("New Email: ")
                    address = input("New Address: ")
                    CustomerService.update_customer(customer_id,name,mobile,email,address)
                    print("\nCustomer Updated.")

                elif choice == "4":
                    customer_id = input("Customer ID: ")
                    CustomerService.delete_customer(customer_id)
                    print("\nCustomer Deleted.")

                elif choice == "5":
                    break

                else:
                    print("\nInvalid Choice.")

            except Exception as e:
                print(f"\nError: {e}")
    
    # VEHICLE MANAGEMENT
    def vehicle_management(self):
        while True:
            print("\n")
            print("=" * 50)
            print("VEHICLE MANAGEMENT")
            print("=" * 50)

            print("1. Add Vehicle")
            print("2. View Vehicles")
            print("3. Update Vehicle")
            print("4. Delete Vehicle")
            print("5. Back")

            choice = input("Enter Choice: ").strip()

            try:
                if choice == "1":
                    customer_id = input("Customer ID: ")
                    vehicle_number = input("Vehicle Number: ")
                    vehicle_type = input("Vehicle Type: ")
                    company = input("Company: ")
                    model = input("Model: ")
                    year = input("Manufacturing Year: ")
                    vehicle = (VehicleService.add_vehicle(customer_id, vehicle_number, vehicle_type, company, model, year))
                    print(f"\nVehicle Added: "f"{vehicle.vehicle_id}")

                elif choice == "2":
                    vehicles = (VehicleService.get_all_vehicles())

                    if not vehicles:
                        print("\nNo Vehicles Found.")
                    
                    else:
                        for vehicle in vehicles:
                            print("\n------------------")
                            print(f"Vehicle ID: "f"{vehicle.vehicle_id}")
                            print(f"Customer ID: "f"{vehicle.customer_id}")
                            print(f"Vehicle No: "f"{vehicle.vehicle_number}")
                            print(f"Type: "f"{vehicle.vehicle_type}")
                            print(f"Company: "f"{vehicle.company}")
                            print(f"Model: "f"{vehicle.model}")
                            print(f"Year: "f"{vehicle.manufacturing_year}")

                elif choice == "3":
                    vehicle_id = input("Vehicle ID: ")
                    vehicle_number = input("Vehicle Number: ")
                    vehicle_type = input("Vehicle Type: ")
                    company = input("Company: ")
                    model = input("Model: ")
                    year = input("Manufacturing Year: ")

                    VehicleService.update_vehicle(vehicle_id, vehicle_number, vehicle_type,company,model,year)

                    print("\nVehicle Updated.")

                elif choice == "4":
                    vehicle_id = input("Vehicle ID: ")
                    VehicleService.delete_vehicle(vehicle_id)
                    print("\nVehicle Deleted.")

                elif choice == "5":
                    break

                else:
                    print("\nInvalid Choice.")

            except Exception as e:
                print(f"\nError: {e}")

    # MECHANIC MANAGEMENT
    def mechanic_management(self):
        while True:
            print("\n")
            print("=" * 50)
            print("MECHANIC MANAGEMENT")
            print("=" * 50)

            print("1. Add Mechanic")
            print("2. View Mechanics")
            print("3. Update Mechanic")
            print("4. Delete Mechanic")
            print("5. Back")

            choice = input("Enter Choice: ").strip()
            
            try:
                if choice == "1":
                    name = input("Name: ")
                    mobile = input("Mobile: ")
                    specialization = input("Specialization: ")
                    password = input("Password: ")

                    mechanic = (MechanicService.add_mechanic(name,mobile,specialization,password))
                    print(f"\nMechanic Created: "f"{mechanic.mechanic_id}")

                elif choice == "2":
                    mechanics = (MechanicService.get_all_mechanics())

                    if not mechanics:
                        print("\nNo Mechanics Found.")

                    else:
                        for mechanic in mechanics:
                            print("\n------------------")
                            print(f"Mechanic ID: "f"{mechanic.mechanic_id}")
                            print(f"Name: "f"{mechanic.name}")
                            print(f"Mobile: "f"{mechanic.mobile}")
                            print(f"Specialization: "f"{mechanic.specialization}")

                elif choice == "3":
                    mechanic_id = input("Mechanic ID: ")
                    name = input("Name: ")
                    mobile = input("Mobile: ")
                    specialization = input("Specialization: ")
                    MechanicService.update_mechanic(mechanic_id,name,mobile,specialization)
                    print("\nMechanic Updated.")

                elif choice == "4":
                    mechanic_id = input("Mechanic ID: ")
                    MechanicService.delete_mechanic(mechanic_id)
                    print("\nMechanic Deleted.")

                elif choice == "5":
                    break

                else:
                    print("\nInvalid Choice.")

            except Exception as e:
                print(f"\nError: {e}")

    # SERVICE REQUESTS
    def service_requests(self):
        while True:
            print("\n")
            print("=" * 50)
            print("SERVICE REQUESTS")
            print("=" * 50)
            print("1. View All Requests")
            print("2. Update Request Status")
            print("3. Back")

            choice = input("Enter Choice: ").strip()

            try:
                if choice == "1":
                    requests = (ServiceRequestService.get_all_requests())

                    if not requests:
                        print("\nNo Requests Found.")

                    else:
                        for request in requests:
                            print("\n------------------")
                            print(f"Request ID: "f"{request.request_id}")
                            print(f"Customer ID: "f"{request.customer_id}")
                            print(f"Vehicle ID: "f"{request.vehicle_id}")
                            print(f"Service Type: "f"{request.service_type}")
                            print(f"Problem: "f"{request.problem_description}")
                            print(f"Date: "f"{request.request_date}")
                            print(f"Status: "f"{request.status}")

                elif choice == "2":
                    request_id = input("Request ID: ")
                    print("\nStatus Options")
                    print("Assigned")
                    print("In Progress")
                    print("Completed")

                    status = input("New Status: ")
                    ServiceRequestService.update_status(request_id,status)
                    print("\nStatus Updated.")

                elif choice == "3":
                    break

                else:
                    print("\nInvalid Choice.")

            except Exception as e:
                print(f"\nError: {e}")

    # MECHANIC ASSIGNMENT
    def mechanic_assignment(self):
        while True:
            print("\n")
            print("=" * 50)
            print("MECHANIC ASSIGNMENT")
            print("=" * 50)

            print("1. Assign Mechanic")
            print("2. View Assignments")
            print("3. Back")

            choice = input("Enter Choice: ").strip()
            
            try:
                if choice == "1":
                    request_id = input("Request ID: ")
                    mechanic_id = input("Mechanic ID: ")
                    assignment = (AssignmentService.assign_mechanic(request_id, mechanic_id))
                    print(f"\nAssignment Created: "f"{assignment.assignment_id}")

                elif choice == "2":
                    assignments = (AssignmentService.get_all_assignments())
                    
                    if not assignments:
                        print("\nNo Assignments Found.")

                    else:
                        for assignment in assignments:
                            print("\n------------------")
                            print(f"Assignment ID: "f"{assignment.assignment_id}")
                            print(f"Request ID: "f"{assignment.request_id}")
                            print(f"Mechanic ID: "f"{assignment.mechanic_id}")
                            print(f"Assigned On: "f"{assignment.assignment_date}")

                elif choice == "3":
                    break

                else:
                    print("\nInvalid Choice.")

            except Exception as e:
                print(f"\nError: {e}")
    
    def billing_menu(self):
        while True:

            print("\n")
            print("=" * 50)
            print("BILLING MENU")
            print("=" * 50)

            print("1. Generate Bill")
            print("2. View Bills")
            print("3. Back")

            choice = input("Enter Choice: ").strip()

            try:
                if choice == "1":
                    request_id = input("Request ID: ")
                    service_charges = input("Service Charges: ")
                    spare_part_charges = input("Spare Part Charges: ")

                    bill = (
                        BillingService.generate_bill(
                            request_id,
                            service_charges,
                            spare_part_charges
                        )
                    )
                    print(f"\nBill Generated: "f"{bill.bill_id}")

                elif choice == "2":
                    bills = (BillingService.get_all_bills())
                    
                    if not bills:
                        print("\nNo Bills Found.")

                    else:
                        for bill in bills:
                            print("\n------------------")

                            print(f"Bill ID: "f"{bill.bill_id}")
                            print(f"Request ID: "f"{bill.request_id}")
                            print(f"Customer ID: "f"{bill.customer_id}")
                            print(f"Vehicle ID: "f"{bill.vehicle_id}")
                            print(f"Service Charges: "f"{bill.service_charges}")
                            print(f"Spare Part Charges: "f"{bill.spare_part_charges}")
                            print(f"Total Amount: "f"{bill.total_amount}")
                            print(f"Bill Date: "f"{bill.bill_date}")

                elif choice == "3":
                    break

                else:
                    print("\nInvalid Choice.")

            except Exception as e:
                print(f"\nError: {e}")

    def payment_menu(self):
        while True:
            print("\n")
            print("=" * 50)
            print("PAYMENT MENU")
            print("=" * 50)

            print("1. Record Payment")
            print("2. View Payments")
            print("3. Back")

            choice = input("Enter Choice: ").strip()

            try:
                if choice == "1":
                    bill_id = input("Bill ID: ")
                    amount = input("Amount: ")
                    payment = (PaymentService.record_payment(bill_id, amount))
                    print(f"\nPayment Recorded: "f"{payment.payment_id}")

                elif choice == "2":
                    payments = (PaymentService.get_all_payments())
                    
                    if not payments:
                        print("\nNo Payments Found.")

                    else:
                        for payment in payments:
                            print("\n------------------")
                            print(f"Payment ID: "f"{payment.payment_id}")
                            print(f"Bill ID: "f"{payment.bill_id}")
                            print(f"Customer ID: "f"{payment.customer_id}")
                            print(f"Amount: "f"{payment.amount}")
                            print(f"Payment Date: "f"{payment.payment_date}")
                            print(f"Status: "f"{payment.payment_status}")

                elif choice == "3":
                    break

                else:
                    print("\nInvalid Choice.")

            except Exception as e:
                print(f"\nError: {e}")

    def report_menu(self):
        while True:
            print("\n")
            print("=" * 50)
            print("REPORT MENU")
            print("=" * 50)

            print("1. Pending Service Report")
            print("2. Completed Service Report")
            print("3. Revenue Report")
            print("4. Mechanic Work Report")
            print("5. Back")

            choice = input("Enter Choice: ").strip()

            try:
                if choice == "1":
                    requests = (ReportService.pending_service_report())

                    if not requests:
                        print("\nNo Pending Requests.")

                    else:
                        for request in requests:
                            print("\n------------------")
                            print(f"Request ID: "f"{request.request_id}")
                            print(f"Customer ID: "f"{request.customer_id}")
                            print(f"Vehicle ID: "f"{request.vehicle_id}")
                            print(f"Status: "f"{request.status}")

                elif choice == "2":
                    requests = (ReportService.completed_service_report())

                    if not requests:
                        print("\nNo Completed Requests.")

                    else:
                        for request in requests:
                            print("\n------------------")
                            print(f"Request ID: "f"{request.request_id}")
                            print(f"Customer ID: "f"{request.customer_id}")
                            print(f"Vehicle ID: "f"{request.vehicle_id}")
                            print(f"Status: "f"{request.status}")

                elif choice == "3":
                    revenue = (ReportService.revenue_report())
                    print(f"\nTotal Revenue: "f"{revenue}")

                elif choice == "4":
                    report = (ReportService.mechanic_work_report())

                    if not report:
                        print("\nNo Data Found.")

                    else:
                        for mechanic_id, count in report.items():
                            print(f"{mechanic_id}"f" -> "f"{count} completed jobs")

                elif choice == "5":
                    break

                else:
                    print("\nInvalid Choice.")

            except Exception as e:
                print(f"\nError: {e}")