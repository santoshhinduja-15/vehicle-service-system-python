class Vehicle:

    def __init__(self,vehicle_id,customer_id,vehicle_number,vehicle_type,company,model,manufacturing_year):
        self.vehicle_id = vehicle_id
        self.customer_id = customer_id
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.company = company
        self.model = model
        self.manufacturing_year = manufacturing_year

    def to_record(self):
        return (f"{self.vehicle_id}|" f"{self.customer_id}|" f"{self.vehicle_number}|" f"{self.vehicle_type}|" f"{self.company}|" f"{self.model}|" f"{self.manufacturing_year}")

    @staticmethod
    def from_record(record):
        data = record.strip().split("|")

        return Vehicle(data[0], data[1], data[2], data[3], data[4], data[5], data[6])