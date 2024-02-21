# file: p03_string.py
# desc: 문자열 자료형과 연산

a = "Hello World"
print(a)
b = 'Hello World'
print(b)
c = "Hello, 'Ash'" # ''표기를 원할 때 ''를 ""안에 넣는다
print(c)

# 탈출 문자 \n 외의 나머지는 파이썬에서 잘 사용되지 않는다.

# 문장을 여러줄로 입력하고 싶으면 '\'
d = 'Hello\n' \
'I\'m A' \
'Nice to meet you'
print(d)

# 여러줄로 출력하고 싶으면 ''', """"
e = '''Hello
I'm A.
Nice to meet you, too'''
print(e)

## 문자열 연산 +, -
before = '가나다라'
after = "마바사"
print(before + after) # 문자열을 합쳐서 하나의 문자열로 출력
print(before * 3) # 문자열을 곱하는 수만큼 반복

## 문자열 길이 구하기
print('글자 길이', len(before))
print('한글글자길이', len('안녕하세요')) # 5

## 문자열 인덱싱, 슬라이싱
cp = 'Life is too short, You need Python'

## 슬라이싱
print(cp[8])
print(cp[17])

# print(cp[8]) = 'd' # 문자열은 배열이긴 하지만 값을 변경할 수 없다

#문자열 범위 슬라이싱
print(cp[12:16+1]) # : 뒤에 있는 숫자는 항상 +1 / 16번째까지 출력하고 싶으면 :16+1

print(ascii('안'), ascii('녕'), ascii('하'), ascii('세'), ascii('요'),)
print(chr(97))

# 기존 문자열로 새로운 문자열을 만들 때는 슬라이싱, 다른 문자열로 대체 필수
print(cp[0:7], 'long', cp[17:]) # ':'뒤를 생략하면 끝까지 출력

# 다른 언어에는 없는 '-' 슬라이싱
print(cp[-6:]) # 음수는 뒤에서 -1 부터 시작됨(0아님)
print(cp[-11:-7]) # -1로 슬라이싱 할 때도 :뒤에는 +1을 해줘야 함

## 문자열 포맷팅 (format string)
## 파이썬에서는 %d, %s, %c 등 포맷스트링용 연산자의 사용 빈도가 낮음
temp = 21
print('현재 온도는 %d도 입니다.' % temp)
temp = 17
print('현재 온도는 %d도 입니다.' % temp)

## format 함수로 포맷팅(파이썬에서 가장 일반적인 방법)
print('현재 온도는 {0}도 입니다.' .format(temp))

## 날짜를 포맷으로 만들 때
month = 2
day = 21
hour = 15
mins = 18
print('오늘은 {0:02d}-{1:02d}, {2:02d}:{3:02d}입니다.' .format(month, day, hour, mins))

# 숫자 자료형 
income = 6_000_000_000 # 연매출 6억 산정, 가독성 떨어짐
print('올해 매출액은 {0:,d}원'. format(income))
PI = 3.1415926536
print('파이는{0:10.2f}'.format(PI)) # 10.2f 소수점 .까지 다 포함해서 10자리, 소숫점 뒤는 2자리
# print('{0:d}'.format(PI)) # 실수형은 정수형 포맷팅 불가

## f 포맷팅 (3.6버전 이후)
name = '홍길동'
age = 30

cont = f'나는 {name}이고, 나이는 {age}세 입니다.' # f를 빼는 순간 포맷을 넣어야 함
print(cont)
name = '성명건'
age = 47
print(f'나는 {name:>3}이고, 나이는 {age:d}세 입니다.') 
print(f'나는 {name:>3}이고, 나이는 {age:1f}세 입니다.')
# 정수는 f포맷 사용 가능, 실수는 d포맷 사용 불가 

## 문자열 함수
a = 'Life is short, You need Python'

print(a.count('Life'))
print(a.count('o')) # a라는 문장에 o가 몇개인지 찾아줌

print(a.find('sh'))

print(a.index('t')) # 첫 번째 't'의 위치(인덱스) 파악
print(a.count('K')) # index()는 count()로 개수가 0이 아닐 때만 사용 가능, 이외에는 예외 발생
print(','.join('dbcde')) #

print(a.upper())
print(a.lower())
print(a.capitalize()) # 문장이 시작되는 단어의 첫 글자만 대문자로 변환

origin = '          Hi          '
print(f'++{origin}++')
print(f'++{origin.lstrip()}++') # 왼쪽 공백 제거
print(f'++{origin.rstrip()}++') # 오른쪽 공백 제거
print(f'++{origin.strip()}++') # 양쪽 공백 모두 제거, 글자 사이의 공백은 제거 불가능

print(cp.replace('too', '').replace('short', 'long')) # 문자열 대체

## 문자열 자르기 -> 리스트(파이썬에는 배열이 없음)
cpWords = cp.split(' ')
print(cpWords)
