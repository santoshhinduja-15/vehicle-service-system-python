from config.constants import (REQUEST_IN_PROGRESS,REQUEST_COMPLETED)
from services.assignment_service import (AssignmentService)
from services.service_request_service import (ServiceRequestService)

class MechanicMenu:
    def __init__(self, mechanic_id):
        self.mechanic_id = mechanic_id

    def start(self):

        while True:
            print("\n")
            print("=" * 50)
            print("MECHANIC MENU")
            print("=" * 50)

            print("1. View Assigned Jobs")
            print("2. Update Job Status")
            print("3. Logout")

            choice = input("Enter Choice: ").strip()

            try:
                if choice == "1":
                    self.view_assigned_jobs()

                elif choice == "2":
                    self.update_job_status()

                elif choice == "3":
                    print("\nLogged Out Successfully.")
                    break

                else:
                    print("\nInvalid Choice.")

            except Exception as e:
                print(f"\nError: {e}")

    def view_assigned_jobs(self):
        assignments = (AssignmentService.get_assignments_by_mechanic(self.mechanic_id))

        if not assignments:
            print("\nNo Assigned Jobs Found.")
            return

        for assignment in assignments:
            request = (ServiceRequestService.get_request_by_id(assignment.request_id))

            if request is None:
                continue

            print("\n------------------")

            print(f"Assignment ID: "f"{assignment.assignment_id}")
            print(f"Request ID: "f"{request.request_id}")
            print(f"Customer ID: "f"{request.customer_id}")
            print(f"Vehicle ID: "f"{request.vehicle_id}")
            print(f"Service Type: "f"{request.service_type}")
            print(f"Problem: "f"{request.problem_description}")
            print(f"Request Date: "f"{request.request_date}")
            print(f"Current Status: "f"{request.status}")

    def update_job_status(self):
        request_id = input("Request ID: ").strip()
        request = (ServiceRequestService.get_request_by_id(request_id))

        if request is None:
            raise ValueError("Request not found.")

        assignment = (AssignmentService.get_assignment_by_request(request_id))

        if assignment is None:
            raise ValueError("Assignment not found.")

        if (assignment.mechanic_id != self.mechanic_id):
            raise ValueError("Unauthorized request.")

        print("\nStatus Options")
        print("1. In Progress")
        print("2. Completed")
        choice = input("Select Status: ").strip()

        if choice == "1":
            ServiceRequestService.update_status(request_id,REQUEST_IN_PROGRESS)
            print("\nStatus Updated.")

        elif choice == "2":
            ServiceRequestService.update_status(request_id, REQUEST_COMPLETED)
            print("\nStatus Updated.")

        else:
            print("\nInvalid Choice.")