class ServiceRequest:

    def __init__(
            self,
            request_id,
            customer_id,
            vehicle_id,
            service_type,
            problem_description,
            request_date,
            status
    ):
        self.request_id = request_id
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id
        self.service_type = service_type
        self.problem_description = problem_description
        self.request_date = request_date
        self.status = status

    def to_record(self):
        return (
            f"{self.request_id}|"
            f"{self.customer_id}|"
            f"{self.vehicle_id}|"
            f"{self.service_type}|"
            f"{self.problem_description}|"
            f"{self.request_date}|"
            f"{self.status}"
        )

    @staticmethod
    def from_record(record):

        data = record.strip().split("|")

        return ServiceRequest(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4],
            data[5],
            data[6]
        )