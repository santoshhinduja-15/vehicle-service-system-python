from config.constants import (
    BILL_FILE,
    REQUEST_COMPLETED
)

from models.bill import Bill

from utils.file_handler import FileHandler
from utils.id_generator import IdGenerator
from utils.date_util import DateUtil

from services.service_request_service import (
    ServiceRequestService
)


class BillingService:

    @staticmethod
    def get_all_bills():

        records = FileHandler.read_all_lines(
            BILL_FILE
        )

        return [
            Bill.from_record(record)
            for record in records
        ]

    @staticmethod
    def get_bill_by_id(bill_id):

        bills = BillingService.get_all_bills()

        for bill in bills:

            if bill.bill_id == bill_id:
                return bill

        return None

    @staticmethod
    def get_bill_by_request_id(
            request_id
    ):

        bills = BillingService.get_all_bills()

        for bill in bills:

            if bill.request_id == request_id:
                return bill

        return None

    @staticmethod
    def generate_bill(
            request_id,
            service_charges,
            spare_part_charges
    ):

        request = (
            ServiceRequestService
            .get_request_by_id(request_id)
        )

        if request is None:
            raise ValueError(
                "Service request not found."
            )

        if request.status != REQUEST_COMPLETED:
            raise ValueError(
                "Service is not completed."
            )

        if BillingService.get_bill_by_request_id(
                request_id
        ):
            raise ValueError(
                "Bill already exists."
            )

        try:
            service_charges = float(
                service_charges
            )

            spare_part_charges = float(
                spare_part_charges
            )

        except ValueError:
            raise ValueError(
                "Charges must be numeric."
            )

        if service_charges < 0:
            raise ValueError(
                "Invalid service charges."
            )

        if spare_part_charges < 0:
            raise ValueError(
                "Invalid spare part charges."
            )

        bills = BillingService.get_all_bills()

        existing_ids = [
            bill.bill_id
            for bill in bills
        ]

        bill_id = (
            IdGenerator.generate_bill_id(
                existing_ids
            )
        )

        total_amount = (
            service_charges +
            spare_part_charges
        )

        bill = Bill(
            bill_id,
            request.request_id,
            request.customer_id,
            request.vehicle_id,
            service_charges,
            spare_part_charges,
            total_amount,
            DateUtil.get_current_date()
        )

        FileHandler.append_line(
            BILL_FILE,
            bill.to_record()
        )

        return bill