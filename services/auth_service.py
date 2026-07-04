from config.constants import (ADMIN_FILE, CUSTOMER_FILE, MECHANIC_FILE)
from models.admin import Admin
from models.customer import Customer
from models.mechanic import Mechanic
from utils.file_handler import FileHandler
from utils.password_hasher import PasswordHasher

class AuthService:
    @staticmethod
    def admin_login(username, password):
        records = FileHandler.read_all_lines(ADMIN_FILE)

        for record in records:
            admin = Admin.from_record(record)

            if (admin.username == username and PasswordHasher.verify_password( password,admin.password_hash)):
                return admin

        return None

    @staticmethod
    def customer_login(customer_id, password):
        records = FileHandler.read_all_lines(CUSTOMER_FILE)

        for record in records:
            customer = Customer.from_record(record)

            if (customer.customer_id == customer_id and PasswordHasher.verify_password(password,customer.password_hash)):
                return customer

        return None

    @staticmethod
    def mechanic_login(mechanic_id, password):
        records = FileHandler.read_all_lines(MECHANIC_FILE)

        for record in records:
            mechanic = Mechanic.from_record(record)

            if (mechanic.mechanic_id == mechanic_id and PasswordHasher.verify_password(password, mechanic.password_hash)):
                return mechanic

        return None