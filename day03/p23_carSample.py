# file: p22_carClass.py
# desc : 객체지향 클래스 학습

class Car:
    carNum = '33가3333'
    company = '현대'
    releaseYear = 1960
    color = '흰색'
    carType = '세단'
    fuelType = '가솔린'

    def getCarColor(self):
        print(f'{self.carNum}은(는) {self.color}입니다.')
    def start(self):
       print(f'{self.carNum}, 시동을 겁니다.')

    def accel(self):
        print(f'{self.carNum}, 밟습니다.')
    
    def brake(self):
        print(f'{self.carNum}, 브레이크를 밟습니다.')

    def turnLeft(self):
        print(f'{self.carNum}, 좌회전합니다.') 

    def turnRight(self):
        print(f'{self.carNum}, 우회전합니다.')

    def __init__(self) -> None: # None : 리턴값이 없다는 뜻(void)
        print('Car 객체를 생성합니다.')
    
    def __str__(self) -> str: # 객체변수를 print()할 때 출력 커스터마이징 함수
        return f'내 차는 {self.company}, {self.carNum} 입니다.'