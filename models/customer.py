class Customer:

    def __init__(self,customer_id,name,mobile,email,address,password_hash):
        self.customer_id = customer_id
        self.name = name
        self.mobile = mobile
        self.email = email
        self.address = address
        self.password_hash = password_hash

    def to_record(self):
        return (f"{self.customer_id}|" f"{self.name}|" f"{self.mobile}|" f"{self.email}|" f"{self.address}|" f"{self.password_hash}")

    @staticmethod
    def from_record(record):
        data = record.strip().split("|")
        return Customer(data[0], data[1], data[2], data[3], data[4], data[5])