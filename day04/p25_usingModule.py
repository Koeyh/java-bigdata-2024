# file : p25_usingModule.py
# desc : 모듈 사용

#import calc as c # calc.py를 사용한다는 선언문, calc를 이하 c로 명칭 변경(as)
from calc import mul #=> calc라는 파일 속 mul이라는 함수만 사용

#import Math # class를 import
from Math import Math # from의 Math는 파일명(py), import의 Math는 클래스명
if __name__ == '__main__':    ## java의 void main()과 동일

#from day03.p22_carClass import Car # 디렉토리(모듈 묶음:패키지).모듈명

#result = c.add(10, 7) # calc.py의 함수 add에 매개변수를 전달 해 값 받아오기
    result = mul(10, 3) 
    print(result)

    print(__name__)

    #myMath = Math.Math() # Math라는 파일 내의 Math 클래스 # import Math
    myMath = Math() # 클래스명
    print(myMath.solv(10))