class Admin:

    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

    def to_record(self):
        return f"{self.username}|{self.password_hash}"

    @staticmethod
    def from_record(record):
        data = record.strip().split("|")
        return Admin(data[0],data[1])