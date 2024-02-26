# file: p29_builtinFunc.py
# desc: 내장 함수

## abs 절대값
print(abs(-5))

## all 현재 컬렉션 데이터의 조건, 값이 참인 값만 있는지
print(all([1,2,3,4 < 2,5]))

## chr() ASCII나 유니코드의 값을 받아서 글자로 변환
print(chr(97))
print(chr(44032))

## ascii() 영문자, 문자를 ASCII코드와 유니코드의 숫자로 변경
print(ascii('가'))
print(ascii('a'))

## dir() 객체가 지닌 변수나 함수를 알려주는 함수
print('list에 내장된 함수 : \n',dir(list()))
print('dict에 내장된 함수 : \n',dir(dict))


## divmod() 나누기의 몫, 나머지를 한번에 구해주는 함수
print(divmod(7, 2))

## ★중요★ enumarate() : '열거하다'라는 뜻, 데이터 포함 인덱스를 같이 생성해주는 역할
for i in enumerate(['Hello', 'World', 'Python']):
    print(i)

for (i, data) in enumerate(['Hello', 'World', 'Python']):
    print(f'{i}번째 값은 {data}입니다.')

## eval() 실행 함수, 문자열로 된 수식, 함수를 실행해 주는 역할
print(eval('1+3'))

## hex() 10진수를 16진수로 변환
print(hex(255).upper())

## ★map()★ 여러 값을 한번에 같은 조건으로 변경할 때 
def ttime(x):
    return x*2

print(list(map(ttime, [1,3,5,7,9])))

print(list(map(int, [1.0,2.0,3.0, 4.4])))

## max()
print(max([3, 9, 99]))
print(min([3, 9, 99]))

## oct() 10진수를 8진수로 변환
print(oct(34))

## ord() ascii()
print(ord('A'))
print(ord('가'))

## round() 반올림 함수
print(round(4.5))

## sum() 반복되는 컬렉션 자료
print(sum(range(1, 101)))

## tuple() 다른 컬렉션을 튜플자료형으로 변경
print(tuple([1,2,3,4,5]))

## type() 변수, 데이터의 타입 리턴
print(type('Hello'))
aa = [1,2,3,4]
print('aa의 타입 : ',type(aa))

## zip() 동일한 개수로 데이터를 묶어서 리턴
odd = [1,3,5,7,9]
even = [2,4,6,8,10]
normal = [1,2,3,4,5]

total = list(zip(odd, even, normal))
print(total)