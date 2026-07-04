from config.constants import VEHICLE_FILE,VEHICLE_TYPES
from models.vehicle import Vehicle
from utils.file_handler import FileHandler
from utils.id_generator import IdGenerator
from utils.validator import Validator
from services.customer_service import CustomerService

class VehicleService:

    @staticmethod
    def get_all_vehicles():
        records = FileHandler.read_all_lines(VEHICLE_FILE)

        return [
            Vehicle.from_record(record)
            for record in records
        ]

    @staticmethod
    def get_vehicle_by_id(vehicle_id):
        vehicles = VehicleService.get_all_vehicles()

        for vehicle in vehicles:

            if vehicle.vehicle_id == vehicle_id:
                return vehicle

        return None

    @staticmethod
    def add_vehicle(customer_id, vehicle_number, vehicle_type, company, model, manufacturing_year):
        errors = []

        if not Validator.is_non_empty(customer_id):
            errors.append("Customer ID is required.")

        customer = CustomerService.get_customer_by_id(customer_id)

        if customer is None:
            errors.append("Customer does not exist.")

        if not Validator.is_valid_vehicle_number(vehicle_number):
            errors.append("Invalid vehicle number.")

        if vehicle_type not in VEHICLE_TYPES:
            errors.append("Invalid vehicle type.")

        if not Validator.is_non_empty(company):
            errors.append("Company is required.")

        if not Validator.is_non_empty(model):
            errors.append("Model is required.")

        if not Validator.is_valid_year(manufacturing_year):
            errors.append("Invalid manufacturing year.")

        vehicles = VehicleService.get_all_vehicles()

        for vehicle in vehicles:

            if vehicle.vehicle_number.upper() == vehicle_number.upper():
                errors.append("Vehicle number already exists.")
                break

        if errors:
            raise ValueError("\n".join(errors))

        existing_ids = [
            vehicle.vehicle_id
            for vehicle in vehicles
        ]

        vehicle_id = IdGenerator.generate_vehicle_id(existing_ids)
        vehicle = Vehicle(vehicle_id, customer_id, vehicle_number, vehicle_type, company, model, manufacturing_year)
        FileHandler.append_line(VEHICLE_FILE, vehicle.to_record())

        return vehicle

    @staticmethod
    def update_vehicle(vehicle_id, vehicle_number, vehicle_type, company, model, manufacturing_year):
        errors = []

        if not Validator.is_valid_vehicle_number(vehicle_number):
            errors.append("Invalid vehicle number.")

        if vehicle_type not in VEHICLE_TYPES:
            errors.append("Invalid vehicle type.")

        if not Validator.is_non_empty(company):
            errors.append("Company is required.")

        if not Validator.is_non_empty(model):
            errors.append("Model is required.")

        if not Validator.is_valid_year(manufacturing_year):
            errors.append("Invalid manufacturing year.")

        vehicles = VehicleService.get_all_vehicles()

        for vehicle in vehicles:

            if (vehicle.vehicle_id != vehicle_id and vehicle.vehicle_number.upper() == vehicle_number.upper()):
                errors.append("Vehicle number already exists.")
                break

        if errors:
            raise ValueError("\n".join(errors))
        
        updated_records = []
        found = False

        for vehicle in vehicles:

            if vehicle.vehicle_id == vehicle_id:
                vehicle.vehicle_number = (vehicle_number)
                vehicle.vehicle_type = (vehicle_type)
                vehicle.company = company
                vehicle.model = model
                vehicle.manufacturing_year = (manufacturing_year)
                found = True
            
            updated_records.append(vehicle.to_record())

        if not found:
            raise ValueError("Vehicle not found.")

        FileHandler.write_all_lines(VEHICLE_FILE,updated_records)
        return True

    @staticmethod
    def delete_vehicle(vehicle_id):
        vehicles = (VehicleService.get_all_vehicles())

        updated_records = []
        deleted = False

        for vehicle in vehicles:

            if vehicle.vehicle_id == vehicle_id:
                deleted = True
                continue

            updated_records.append(vehicle.to_record())

        if deleted:
            FileHandler.write_all_lines(VEHICLE_FILE,updated_records)
            return True

        raise ValueError("Vehicle not found.")

    @staticmethod
    def get_vehicles_by_customer(customer_id):
        customer = (CustomerService.get_customer_by_id(customer_id))

        if customer is None:
            raise ValueError("Customer not found.")

        vehicles = (VehicleService.get_all_vehicles())

        return [
            vehicle
            for vehicle in vehicles
            if vehicle.customer_id == customer_id
            ]