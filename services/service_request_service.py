from config.constants import (SERVICE_REQUEST_FILE, SERVICE_TYPES, REQUEST_PENDING, REQUEST_ASSIGNED, REQUEST_IN_PROGRESS, REQUEST_COMPLETED, REQUEST_STATUS)
from models.service_request import ServiceRequest
from utils.file_handler import FileHandler
from utils.id_generator import IdGenerator
from utils.date_util import DateUtil
from utils.validator import Validator
from services.customer_service import CustomerService
from services.vehicle_service import VehicleService

class ServiceRequestService:

    @staticmethod
    def get_all_requests():
        records = FileHandler.read_all_lines(SERVICE_REQUEST_FILE)

        return [
            ServiceRequest.from_record(record)
            for record in records
        ]

    @staticmethod
    def get_request_by_id(request_id):
        requests = ServiceRequestService.get_all_requests()

        for request in requests:

            if request.request_id == request_id:
                return request

        return None

    @staticmethod
    def create_request(customer_id, vehicle_id, service_type, problem_description):
        errors = []
        customer = None
        vehicle = None

        if not Validator.is_non_empty(customer_id):
            errors.append("Customer ID is required.")
        
        else:
            customer = CustomerService.get_customer_by_id(customer_id)

            if customer is None:
                errors.append("Customer not found.")

        if not Validator.is_non_empty(vehicle_id):
            errors.append("Vehicle ID is required.")
        
        else:
            vehicle = VehicleService.get_vehicle_by_id(vehicle_id)

            if vehicle is None:
                errors.append("Vehicle not found.")

        if customer is not None and vehicle is not None:

            if vehicle.customer_id != customer_id:
                errors.append("Vehicle does not belong to customer.")

        if service_type not in SERVICE_TYPES:
            errors.append("Invalid service type.")

        if not Validator.is_non_empty(problem_description):
            errors.append("Problem description is required.")

        if errors:
            raise ValueError("\n".join(errors))

        requests = ServiceRequestService.get_all_requests()
        existing_ids = [
            request.request_id
            for request in requests
        ]

        request_id = IdGenerator.generate_request_id(existing_ids)
        service_request = ServiceRequest(request_id, customer_id, vehicle_id, service_type, problem_description, DateUtil.get_current_date(), REQUEST_PENDING)
        FileHandler.append_line(SERVICE_REQUEST_FILE,service_request.to_record())
        return service_request

    @staticmethod
    def update_status(request_id,new_status):

        if new_status not in REQUEST_STATUS:
            raise ValueError("Invalid request status.")

        requests = ServiceRequestService.get_all_requests()

        status_flow = {
            REQUEST_PENDING: [REQUEST_ASSIGNED],
            REQUEST_ASSIGNED: [REQUEST_IN_PROGRESS],
            REQUEST_IN_PROGRESS: [REQUEST_COMPLETED],
            REQUEST_COMPLETED: []
        }

        updated_records = []
        found = False

        for request in requests:

            if request.request_id == request_id:
                current_status = request.status

                if new_status not in status_flow[current_status]:
                    raise ValueError(f"Invalid status transition "f"from {current_status} "f"to {new_status}")

                request.status = new_status
                found = True

            updated_records.append(request.to_record())

        if not found:
            raise ValueError("Service request not found.")

        FileHandler.write_all_lines(SERVICE_REQUEST_FILE, updated_records)
        return True

    @staticmethod
    def get_requests_by_customer(customer_id):
        customer = CustomerService.get_customer_by_id(customer_id)

        if customer is None:
            raise ValueError("Customer not found.")

        requests = ServiceRequestService.get_all_requests()

        return [
            request
            for request in requests
            if request.customer_id == customer_id
        ]

    @staticmethod
    def get_requests_by_vehicle(vehicle_id):
        vehicle = VehicleService.get_vehicle_by_id(vehicle_id)

        if vehicle is None:
            raise ValueError("Vehicle not found.")

        requests = ServiceRequestService.get_all_requests()

        return [
            request
            for request in requests
            if request.vehicle_id == vehicle_id
        ]