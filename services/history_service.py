from services.customer_service import (
    CustomerService
)

from services.vehicle_service import (
    VehicleService
)

from services.service_request_service import (
    ServiceRequestService
)


class HistoryService:

    @staticmethod
    def get_customer_history(
            customer_id
    ):

        customer = (
            CustomerService.get_customer_by_id(
                customer_id
            )
        )

        if customer is None:
            raise ValueError(
                "Customer not found."
            )

        return (
            ServiceRequestService
            .get_requests_by_customer(
                customer_id
            )
        )

    @staticmethod
    def get_vehicle_history(
            vehicle_id
    ):

        vehicle = (
            VehicleService.get_vehicle_by_id(
                vehicle_id
            )
        )

        if vehicle is None:
            raise ValueError(
                "Vehicle not found."
            )

        requests = (
            ServiceRequestService
            .get_all_requests()
        )

        return [
            request
            for request in requests
            if request.vehicle_id
            ==
            vehicle_id
        ]