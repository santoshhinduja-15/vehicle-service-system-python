from config.constants import (
    CUSTOMER_ID_PREFIX,
    VEHICLE_ID_PREFIX,
    MECHANIC_ID_PREFIX,
    REQUEST_ID_PREFIX,
    ASSIGNMENT_ID_PREFIX,
    BILL_ID_PREFIX,
    PAYMENT_ID_PREFIX
)


class IdGenerator:

    @staticmethod
    def generate_id(prefix, existing_ids):
        if not existing_ids:
            return f"{prefix}101"

        max_number = 100

        for current_id in existing_ids:
            try:
                number = int(current_id.replace(prefix, ""))
                if number > max_number:
                    max_number = number
            except ValueError:
                pass

        return f"{prefix}{max_number + 1}"

    @staticmethod
    def generate_customer_id(existing_ids):
        return IdGenerator.generate_id(CUSTOMER_ID_PREFIX, existing_ids)

    @staticmethod
    def generate_vehicle_id(existing_ids):
        return IdGenerator.generate_id(VEHICLE_ID_PREFIX, existing_ids)

    @staticmethod
    def generate_mechanic_id(existing_ids):
        return IdGenerator.generate_id(MECHANIC_ID_PREFIX, existing_ids)

    @staticmethod
    def generate_request_id(existing_ids):
        return IdGenerator.generate_id(REQUEST_ID_PREFIX, existing_ids)

    @staticmethod
    def generate_assignment_id(existing_ids):
        return IdGenerator.generate_id(ASSIGNMENT_ID_PREFIX, existing_ids)

    @staticmethod
    def generate_bill_id(existing_ids):
        return IdGenerator.generate_id(BILL_ID_PREFIX, existing_ids)

    @staticmethod
    def generate_payment_id(existing_ids):
        return IdGenerator.generate_id(PAYMENT_ID_PREFIX, existing_ids)