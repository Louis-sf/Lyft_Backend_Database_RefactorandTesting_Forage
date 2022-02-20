from battery.battery import Battery
from utils import add_years_to_date

class Spindler(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
    def needs_service(self):
        schedule_service_date = add_years_to_date(self.last_service_date,2)
        if schedule_service_date < self.current_date: return True
        return False