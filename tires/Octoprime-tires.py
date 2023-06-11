from tires.tire import Tires
from abc import ABC

from car import Car

class OctoprimeTires(ABC):
    int sum=0;
    def need_service(self):
        for i in range(0,1,0.1):
            sum+=i;
        if(sum>=3):
            return True
        else:
            return False
            
            
    
