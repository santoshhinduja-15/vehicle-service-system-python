class Mechanic:

    def __init__(self, mechanic_id, name, mobile,specialization,password_hash):
        self.mechanic_id = mechanic_id
        self.name = name
        self.mobile = mobile
        self.specialization = specialization
        self.password_hash = password_hash

    def to_record(self):
        return ( f"{self.mechanic_id}|" f"{self.name}|" f"{self.mobile}|" f"{self.specialization}|" f"{self.password_hash}")

    @staticmethod
    def from_record(record):
        data = record.strip().split("|")
        return Mechanic(data[0], data[1], data[2], data[3], data[4])