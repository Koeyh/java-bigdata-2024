# file: p30_standardLib.py
# desc: 표준 라이브러리(빌트인) 학습

import datetime
import time
import random
import pip

print(datetime.date(2024, 2, 26)) # 현재 OS에 맞춰서 날짜형으로 변경

## ★datetime.datetime.now()★ 사용 빈도 잦음
curr = datetime.datetime.now() # 현재의 년/월/일/시/분/초 알려줌
print(curr)

print(curr.weekday()) # 0 : 월요일 ~ 6 : 일요일
print(curr.month) # 월 출력
print(curr.day)
print(curr.hour)

print(f'{curr.year}년 {curr.month:02d}월 {curr.day}일 {curr.hour}시 {curr.minute}분')

curr2 = time.localtime()
print(curr2)


# ## timesleep 많이 쓰임. 알아두면 유용할 것.
# for i in range(5):
#     print(f'{i} 출력')
#     time.sleep(2) #2초씩 잠시 멈춤

## random()
print(random.random()) # 0~1 사이 소수점 랜덤 수 
print(random.randint(1, 45)) # 로또번호 만들기 ? / 1~45 사이의 랜덤 정수

## 로또
result = []
total = []

for i in range(5):
    while True:
        val = random.randint(1, 45)
        while val not in result:
            result.append(val) # append() : 리스트의 끝에 새로운 요소 추가하는 함수
        if len(result) == 6:
            break

    result.sort()
    total.append(result)
    result = []


print(total)


