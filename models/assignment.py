class Assignment:
    def __init__(self, assignment_id, request_id, mechanic_id, assignment_date):
        self.assignment_id = assignment_id
        self.request_id = request_id
        self.mechanic_id = mechanic_id
        self.assignment_date = assignment_date

    def to_record(self):
        return (f"{self.assignment_id}|" f"{self.request_id}|" f"{self.mechanic_id}|" f"{self.assignment_date}")

    @staticmethod
    def from_record(record):
        data = record.strip().split("|")
        return Assignment(data[0], data[1], data[2], data[3])