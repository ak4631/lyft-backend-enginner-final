from battery.battery import battery

class SpinlderBattery(Battery):
    def __init__(self,current_date,last_service_date):
        self.current_date=current_date
        self.last_service_date=last_service_date
        self.spindler_year_need_service=3

    def needs_service(self):
        if self.current_date - self.last_service_date >= spindler_year_need_service:
            return True
        else:
            return False
