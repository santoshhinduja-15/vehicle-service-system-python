from config.constants import CUSTOMER_FILE
from models.customer import Customer
from utils.file_handler import FileHandler
from utils.id_generator import IdGenerator
from utils.password_hasher import PasswordHasher
from utils.validator import Validator

class CustomerService:

    @staticmethod
    def get_all_customers():
        records = FileHandler.read_all_lines(CUSTOMER_FILE)

        return [
            Customer.from_record(record)
            for record in records
        ]

    @staticmethod
    def get_customer_by_id(customer_id):
        customers = (CustomerService.get_all_customers())

        for customer in customers:
            if customer.customer_id == customer_id:
                return customer

        return None

    @staticmethod
    def add_customer(name, mobile, email, address, password):
        errors = []

        if not Validator.is_non_empty(name):
            errors.append("Customer name cannot be empty.")

        if not Validator.is_non_empty(address):
            errors.append("Address cannot be empty.")

        if not Validator.is_valid_mobile(mobile):
            errors.append("Invalid mobile number.")

        if not Validator.is_valid_email(email):
            errors.append("Invalid email address.")

        if not Validator.is_valid_password(password):
            errors.append("Password must be at least 6 characters.")

        customers = (CustomerService.get_all_customers())

        for customer in customers:
            if (customer.email.lower() == email.lower()):
                errors.append("Email already exists.")

            if customer.mobile == mobile:
                errors.append("Mobile number already exists.")

        if errors:
            raise ValueError("\n".join(errors))

        existing_ids = [
            customer.customer_id
            for customer in customers
        ]

        customer_id = (IdGenerator.generate_customer_id(existing_ids))
        customer = Customer(customer_id, name, mobile, email, address, PasswordHasher.hash_password(password))
        FileHandler.append_line(CUSTOMER_FILE,customer.to_record())
        return customer

    @staticmethod
    def update_customer(customer_id, name, mobile, email, address):
        errors = []

        if not Validator.is_non_empty(name):
            errors.append("Customer name cannot be empty.")

        if not Validator.is_non_empty(address):
            errors.append("Address cannot be empty.")

        if not Validator.is_valid_mobile(mobile):
            errors.append("Invalid mobile number.")

        if not Validator.is_valid_email(email):
            errors.append("Invalid email address.")

        customers = (CustomerService.get_all_customers())

        for customer in customers:

            if (customer.customer_id != customer_id and customer.email.lower() == email.lower()):
                errors.append("Email already exists.")

            if (customer.customer_id != customer_id and customer.mobile == mobile):
                errors.append("Mobile number already exists.")

        if errors:
            raise ValueError("\n".join(errors))

        updated_records = []
        found = False

        for customer in customers:

            if customer.customer_id == customer_id:
                customer.name = name
                customer.mobile = mobile
                customer.email = email
                customer.address = address
                found = True
            
            updated_records.append(customer.to_record())

        if not found:
            raise ValueError("Customer not found.")

        FileHandler.write_all_lines(CUSTOMER_FILE,updated_records)
        return True

    @staticmethod
    def delete_customer(customer_id):
        customers = (CustomerService.get_all_customers())
        updated_records = []
        deleted = False

        for customer in customers:
            if customer.customer_id == customer_id:
                deleted = True
                continue

            updated_records.append(customer.to_record())

        if deleted:
            FileHandler.write_all_lines(CUSTOMER_FILE,updated_records)
            return True

        raise ValueError("Customer not found.")