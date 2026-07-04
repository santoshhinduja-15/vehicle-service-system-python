class Bill:

    def __init__(self, bill_id, request_id, customer_id, vehicle_id, service_charges, spare_part_charges, total_amount, bill_date):
        self.bill_id = bill_id
        self.request_id = request_id
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id
        self.service_charges = service_charges
        self.spare_part_charges = spare_part_charges
        self.total_amount = total_amount
        self.bill_date = bill_date

    def to_record(self):
        return (f"{self.bill_id}|" f"{self.request_id}|" f"{self.customer_id}|" f"{self.vehicle_id}|" f"{self.service_charges}|" f"{self.spare_part_charges}|" f"{self.total_amount}|" f"{self.bill_date}" )

    @staticmethod
    def from_record(record):
        data = record.strip().split("|")
        return Bill(data[0], data[1], data[2], data[3], float(data[4]), float(data[5]), float(data[6]), data[7])