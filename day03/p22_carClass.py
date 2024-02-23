# file: p22_carClass.py
# desc: 객체지향 클래스 학습

class Car:
    carNum = ''
    company = ''
    releaseYear = 1960
    color = 'white'
    carType = ''
    fuelType = "Gasoline"

    def start(self):
        print('시동을 겁니다.')

    def accel(self):
        print('엑셀을 밟습니다.')

    def brake(self):
        print('브레이크를 밟습니다.')

    def turnLeft(self):
        print('좌회전')
    
    def turnRight(right):
        print('우회전')
    
