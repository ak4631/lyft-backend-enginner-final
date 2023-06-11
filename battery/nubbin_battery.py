from battery.battery import battery

class NubbinBattery(Battery):
    def __init__(self,current_date,last_service_date):
        self.current_date=current_date
        self.last_service_date=last_service_date
        self.nubbin_year_need_service=4

    def needs_service(self):
        if self.current_date - self.last_service_date >= nubbin_year_need_service:
            return True
        else:
            return False
