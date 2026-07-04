from config.constants import (
    PAYMENT_FILE,
    PAYMENT_PAID
)

from models.payment import Payment

from utils.file_handler import FileHandler
from utils.id_generator import IdGenerator
from utils.date_util import DateUtil

from services.billing_service import (
    BillingService
)


class PaymentService:

    @staticmethod
    def get_all_payments():

        records = FileHandler.read_all_lines(
            PAYMENT_FILE
        )

        return [
            Payment.from_record(record)
            for record in records
        ]

    @staticmethod
    def get_payment_by_id(
            payment_id
    ):

        payments = (
            PaymentService.get_all_payments()
        )

        for payment in payments:

            if payment.payment_id == payment_id:
                return payment

        return None

    @staticmethod
    def record_payment(
            bill_id,
            amount
    ):

        bill = (
            BillingService.get_bill_by_id(
                bill_id
            )
        )

        if bill is None:
            raise ValueError(
                "Bill not found."
            )

        try:
            amount = float(amount)

        except ValueError:
            raise ValueError(
                "Invalid amount."
            )

        if amount <= 0:
            raise ValueError(
                "Amount must be greater than zero."
            )

        if round(amount, 2) != round(bill.total_amount, 2):
            raise ValueError(
                "Payment amount mismatch."
            )

        payments = (
            PaymentService.get_all_payments()
        )

        for payment in payments:

            if (
                payment.bill_id == bill_id
                and
                payment.payment_status
                ==
                PAYMENT_PAID
            ):
                raise ValueError(
                    "Bill already paid."
                )

        existing_ids = [
            payment.payment_id
            for payment in payments
        ]

        payment_id = (
            IdGenerator.generate_payment_id(
                existing_ids
            )
        )

        payment = Payment(
            payment_id,
            bill.bill_id,
            bill.customer_id,
            amount,
            DateUtil.get_current_date(),
            PAYMENT_PAID
        )

        FileHandler.append_line(
            PAYMENT_FILE,
            payment.to_record()
        )

        return payment