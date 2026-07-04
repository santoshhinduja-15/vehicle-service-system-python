class Payment:
    def __init__(self, payment_id, bill_id, customer_id, amount, payment_date, payment_status):
        self.payment_id = payment_id
        self.bill_id = bill_id
        self.customer_id = customer_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_status = payment_status

    def to_record(self):
        return (f"{self.payment_id}|" f"{self.bill_id}|" f"{self.customer_id}|" f"{self.amount}|" f"{self.payment_date}|" f"{self.payment_status}")

    @staticmethod
    def from_record(record):
        data = record.strip().split("|")
        return Payment(data[0], data[1], data[2], float(data[3]), data[4], data[5])