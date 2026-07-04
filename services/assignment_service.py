from config.constants import (
    ASSIGNMENT_FILE,
    REQUEST_PENDING,
    REQUEST_ASSIGNED
)

from models.assignment import Assignment

from utils.file_handler import FileHandler
from utils.id_generator import IdGenerator
from utils.date_util import DateUtil

from services.mechanic_service import MechanicService
from services.service_request_service import (
    ServiceRequestService
)


class AssignmentService:

    @staticmethod
    def get_all_assignments():

        records = FileHandler.read_all_lines(
            ASSIGNMENT_FILE
        )

        return [
            Assignment.from_record(record)
            for record in records
        ]

    @staticmethod
    def get_assignment_by_id(
            assignment_id
    ):

        assignments = (
            AssignmentService.get_all_assignments()
        )

        for assignment in assignments:

            if (
                assignment.assignment_id
                ==
                assignment_id
            ):
                return assignment

        return None

    @staticmethod
    def assign_mechanic(
            request_id,
            mechanic_id
    ):

        request = (
            ServiceRequestService
            .get_request_by_id(request_id)
        )

        if request is None:
            raise ValueError(
                "Service request not found."
            )

        mechanic = (
            MechanicService
            .get_mechanic_by_id(mechanic_id)
        )

        if mechanic is None:
            raise ValueError(
                "Mechanic not found."
            )

        if request.status != REQUEST_PENDING:
            raise ValueError(
                "Only pending requests can be assigned."
            )

        assignments = (
            AssignmentService
            .get_all_assignments()
        )

        for assignment in assignments:

            if assignment.request_id == request_id:
                raise ValueError(
                    "Request already assigned."
                )

        existing_ids = [
            assignment.assignment_id
            for assignment in assignments
        ]

        assignment_id = (
            IdGenerator.generate_assignment_id(
                existing_ids
            )
        )

        assignment = Assignment(
            assignment_id,
            request_id,
            mechanic_id,
            DateUtil.get_current_date()
        )

        FileHandler.append_line(
            ASSIGNMENT_FILE,
            assignment.to_record()
        )

        ServiceRequestService.update_status(
            request_id,
            REQUEST_ASSIGNED
        )

        return assignment

    @staticmethod
    def get_assignments_by_mechanic(
            mechanic_id
    ):

        mechanic = (
            MechanicService
            .get_mechanic_by_id(
                mechanic_id
            )
        )

        if mechanic is None:
            raise ValueError(
                "Mechanic not found."
            )

        assignments = (
            AssignmentService
            .get_all_assignments()
        )

        return [
            assignment
            for assignment in assignments
            if assignment.mechanic_id
            ==
            mechanic_id
        ]

    @staticmethod
    def get_assignment_by_request(
            request_id
    ):

        assignments = (
            AssignmentService
            .get_all_assignments()
        )

        for assignment in assignments:

            if assignment.request_id == request_id:
                return assignment

        return None
