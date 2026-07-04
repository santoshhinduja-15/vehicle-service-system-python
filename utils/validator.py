import re
from datetime import datetime
from config.constants import (MOBILE_LENGTH,MIN_PASSWORD_LENGTH,CURRENT_YEAR)

class Validator:
    @staticmethod
    def is_valid_mobile(mobile):
        if not mobile.isdigit():
            return False

        if len(mobile) != 10:
            return False

        if mobile[0] not in ["6", "7", "8", "9"]:
            return False

        if len(set(mobile)) == 1:
            return False

        return True

    @staticmethod
    def is_valid_email(email):
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        return bool(re.fullmatch(pattern, email))

    @staticmethod
    def is_valid_password(password):
        return len(password) >= MIN_PASSWORD_LENGTH

    @staticmethod
    def is_positive_amount(amount):
        try:
            return float(amount) > 0
        except ValueError:
            return False

    @staticmethod
    def is_valid_year(year):
        try:
            year = int(year)
            return 1900 <= year <= CURRENT_YEAR
        except ValueError:
            return False

    @staticmethod
    def is_non_empty(value):
        return value.strip() != ""

    @staticmethod
    def is_valid_vehicle_number(vehicle_number):
        """
        Valid Indian Vehicle Number Examples:
        MH01AB1234
        DL8CAF5031
        KA03MN9876
        MH 01 AB 1234
        mh01ab1234
        """

        vehicle_number = vehicle_number.strip().upper()
        vehicle_number = vehicle_number.replace(" ", "")

        pattern = r'^[A-Z]{2}[0-9]{1,2}[A-Z]{1,3}[0-9]{4}$'

        return bool(re.fullmatch(pattern, vehicle_number))

    @staticmethod
    def is_valid_status(status, allowed_statuses):
        return status in allowed_statuses

    @staticmethod
    def is_valid_name(name):
        pattern = r'^[A-Za-z ]+$'
        return bool(re.fullmatch(pattern, name.strip()))

    @staticmethod
    def is_valid_customer_id(customer_id):
        return bool(re.fullmatch(r'C\d+',customer_id.strip().upper()))

    @staticmethod
    def is_valid_vehicle_id(vehicle_id):
        return bool(re.fullmatch(r'V\d+',vehicle_id.strip().upper()))

    @staticmethod
    def is_valid_mechanic_id(mechanic_id):
        return bool(re.fullmatch(r'M\d+',mechanic_id.strip().upper()))

    @staticmethod
    def is_valid_request_id(request_id):
        return bool(re.fullmatch(r'R\d+',request_id.strip().upper()))

    @staticmethod
    def is_valid_assignment_id(assignment_id):
        return bool(re.fullmatch(r'A\d+',assignment_id.strip().upper()))

    @staticmethod
    def is_valid_bill_id(bill_id):
        return bool(re.fullmatch(r'B\d+',bill_id.strip().upper()))

    @staticmethod
    def is_valid_payment_id(payment_id):
        return bool(re.fullmatch(r'P\d+',payment_id.strip().upper()))

    @staticmethod
    def is_valid_integer(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_date(date_string, date_format="%d-%m-%Y"):
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False