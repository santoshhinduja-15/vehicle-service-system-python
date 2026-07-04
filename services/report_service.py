from config.constants import REQUEST_PENDING,REQUEST_COMPLETED
from services.service_request_service import ServiceRequestService
from services.billing_service import BillingService
from services.assignment_service import AssignmentService

class ReportService:
    @staticmethod
    def pending_service_report():
        requests = (ServiceRequestService.get_all_requests())

        return [
            request
            for request in requests
            if request.status == REQUEST_PENDING
            ]

    @staticmethod
    def completed_service_report():
        requests = (ServiceRequestService.get_all_requests())

        return [
            request
            for request in requests
            if request.status == REQUEST_COMPLETED]

    @staticmethod
    def revenue_report():
        bills = (BillingService.get_all_bills())
        total_revenue = 0

        for bill in bills:
            total_revenue += (bill.total_amount)

        return total_revenue

    @staticmethod
    def mechanic_work_report():
        assignments = (AssignmentService.get_all_assignments())

        requests = (ServiceRequestService.get_all_requests())

        report = {}

        for assignment in assignments:
            completed_jobs = 0

            for request in requests:

                if (request.request_id == assignment.request_id and request.status == REQUEST_COMPLETED):
                    completed_jobs += 1

            if (assignment.mechanic_id not in report):
                report[assignment.mechanic_id] = 0

            report[assignment.mechanic_id] += completed_jobs

        return report