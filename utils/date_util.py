from datetime import datetime
from config.constants import DATE_FORMAT

class DateUtil:

    @staticmethod
    def get_current_date():
        return datetime.now().strftime(DATE_FORMAT)

    @staticmethod
    def format_date(date_obj):
        return date_obj.strftime(DATE_FORMAT)

    @staticmethod
    def parse_date(date_string):
        return datetime.strptime(date_string,DATE_FORMAT)