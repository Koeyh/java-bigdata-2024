# file : calc.py
# desc : 모듈 만들어 사용해보기

# 무조건 모듈을 클래스로 만들 필요는 없음, 함수들만 모아도 상관없음

def add(a, b):
    res = a + b
    return res

def mul(a, b):
    res = a * b
    return res

print(__name__) # __main__ => 메인 엔트리라는 뜻