from config.constants import MECHANIC_FILE
from models.mechanic import Mechanic
from utils.file_handler import FileHandler
from utils.id_generator import IdGenerator
from utils.password_hasher import PasswordHasher
from utils.validator import Validator

class MechanicService:
    @staticmethod
    def get_all_mechanics():
        records = FileHandler.read_all_lines(MECHANIC_FILE)

        return [
            Mechanic.from_record(record)
            for record in records
        ]

    @staticmethod
    def get_mechanic_by_id(mechanic_id):
        mechanics = (MechanicService.get_all_mechanics())

        for mechanic in mechanics:

            if mechanic.mechanic_id == mechanic_id:
                return mechanic

        return None

    @staticmethod
    def add_mechanic(name,mobile, specialization, password):
        errors = []

        if not Validator.is_non_empty(name):
            errors.append("Mechanic name is required.")

        if not Validator.is_valid_mobile(mobile):
            errors.append("Invalid mobile number.")

        if not Validator.is_non_empty(specialization):
            errors.append("Specialization is required.")

        if not Validator.is_valid_password(password):
            errors.append("Password must be at least 6 characters.")

        mechanics = (MechanicService.get_all_mechanics())

        for mechanic in mechanics:

            if mechanic.mobile == mobile:
                errors.append("Mobile number already exists.")

        if errors:
            raise ValueError("\n".join(errors))

        existing_ids = [
            mechanic.mechanic_id
            for mechanic in mechanics
        ]

        mechanic_id = (IdGenerator.generate_mechanic_id(existing_ids))

        mechanic = Mechanic(mechanic_id, name, mobile, specialization, PasswordHasher.hash_password(password))

        FileHandler.append_line(MECHANIC_FILE,mechanic.to_record())
        return mechanic

    @staticmethod
    def update_mechanic(mechanic_id, name, mobile, specialization):
        errors = []

        if not Validator.is_non_empty(name):
            errors.append("Mechanic name is required.")

        if not Validator.is_valid_mobile(mobile):
            errors.append("Invalid mobile number.")

        if not Validator.is_non_empty(specialization):
            errors.append("Specialization is required.")
        
        mechanics = (MechanicService.get_all_mechanics())

        for mechanic in mechanics:

            if (mechanic.mechanic_id != mechanic_id and mechanic.mobile == mobile):
                errors.append("Mobile number already exists.")

        if errors:
            raise ValueError("\n".join(errors))

        updated_records = []
        found = False

        for mechanic in mechanics:

            if mechanic.mechanic_id == mechanic_id:
                mechanic.name = name
                mechanic.mobile = mobile
                mechanic.specialization = specialization
                found = True

            updated_records.append(mechanic.to_record())

        if not found:
            raise ValueError("Mechanic not found.")
        
        FileHandler.write_all_lines(MECHANIC_FILE,updated_records)
        return True

    @staticmethod
    def delete_mechanic(mechanic_id):
        mechanics = (MechanicService.get_all_mechanics())
        updated_records = []
        deleted = False

        for mechanic in mechanics:

            if mechanic.mechanic_id == mechanic_id:
                deleted = True
                continue

            updated_records.append(mechanic.to_record())

        if deleted:
            FileHandler.write_all_lines(MECHANIC_FILE,updated_records)
            return True

        raise ValueError("Mechanic not found.")