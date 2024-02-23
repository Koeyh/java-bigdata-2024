# file: f24_ionic.py
# desc: 클래스 상속

from p22_carClass import Car

class Ionic(Car): # 상속, Car 클래스를 상속받아서 Ionic
    __fuelRate = 0.0

    def setFuelRate(self, rate):
        self.__fuelRate = rate

    def getFuelRate(self) -> float:
        return self.__fuelRate
    
myCar = Ionic('33가 3333')
myCar.company = ('현대자동차')
myCar.setFuelRate(23.5)
print(myCar)
print(f'내 차의 연비는 {myCar.getFuelRate()} km/l 입니다.')