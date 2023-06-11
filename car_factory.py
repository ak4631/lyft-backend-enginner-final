from car import Car
from battery import Battery
from tires import tire as te
from engine.model.capulet_engine import CapuletEngine
from engine.model.sternman_engine import SternmanEngine
from engine.model.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.Carrigan_tires import CarriganTires
from tires.Octoprime_tires import OctoprimeTires


class CarFactory:
    
    @staticmethod
    def create_calliope(current_date,last_service_date,current_mileage,last_service_mileage,tires):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        te=CarriganTires(tires)
        car = Car(engine, battery,tires)
        
        return car
    @staticmethod
    def create_glissade(current_date,last_service_date,current_mileage,last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        te=CarriganTires(tires)
        car = Car(engine, battery,tires)
        return car

    def create_palindrome(current_date,last_service_date,warning_light_on):
        engine=StermanEngine(warning_light_on)
        battery=SpindlerBattery(current_date,last_service_date)
        te=CarriganTires(tires)
        car=Car(engine,battery,tires)
        return car

    def create_roschach(current_date,last_service_date,current_mileage,last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        te=OctoprimeTires(tires)
        car = Car(engine, battery,tires)
        return car
    
    def create_thovex(current_date,last_service_date,current_mileage,last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        te=OctoprimeTires(tires)
        car = Car(engine, battery,tires)
        return car
