# file : p04_lst.py
# desc : 리스트

## 파이썬엔 배열이 없다. 리스트로 대신함

even = [2,4,6,8,10]
odd = [1,3,5,7,9]

print(even)
print(even[4]) # 길이가 n일 때 마지막 인덱스는 n-1

even[4] = 20
print(even) # 리스트는 문자열과 달리 인덱스의 값을 변경 가능       

datas = [123, 45.6, True, 'Hello', odd, None] # 형 지정이 없기때문에 어떤 자료형이든 다 리스트에 할당 가능함
print (datas)

print(odd[2])

print(even[0] + odd[0])

cpWords = ['Life', 'is', 'short']
print(cpWords[0] + cpWords[2])

print(even[1:4])

## 2차원 리스트
# 3행 4열
# [[1, 2, 3, 4],
# [5, 6, 7, 8],
# [9, 10, 11, 12]]

d2Datas =  [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]

print(d2Datas)
for i in d2Datas : 
    print(i)

dm1col1 = [1,2,3,4]
dm1col2 = [5,6,7,8]
dm1col3 = [9,10,11,12]

print([dm1col1, dm1col2, dm1col3])

#리스트 연산은 문자열 연산과 동일
print(even + odd)
print(odd * 2)

## 값 변경
even[3] = 10 # even[]의 3번 인덱스 값을 10으로 변경
print(even)

## 값 삭제
del even[2] # del 키워드를 통해 even[]의 2번 인덱스 삭제
print(even)

## 리스트 함수
# append : 리스트 제일 마지막에 추가
even.append(30) # 기존 [2, 4, 10, 20]
print(even) # 매개변수 30이 마지막에 추가된 것 확인 가능

# insert : 원하는 위치에 값 추가
even.insert(2, 6) # 2번 인덱스에 6을 추가
print(even) # [2,4,10,20,30] 에서 [2,4,6,10,20,30] 으로 변경된 것 확인 가능

# 정렬(Sort)
origin = [45, 23, 9, 17, 1, 5, 11, 3, 29, 30]
origin.sort()
print(origin)
origin.sort(reverse=True) # 내림차준(Desc)
print(origin)

# 뒤집기
aa = ['a', 'f', 'e', 'b']
aa.reverse() # 정렬을 떠나 인덱스의 순서를 역순으로 뒤집는 것 1,2,3,4에서 4,3,2,1로 변경
print(aa)

print(aa.count('e'))

# 제거
bb = aa = [1, 3, 5, 6, 8, 3, 1]
bb.remove(3) # 가장 앞에 있는 3만 지움
bb.remove(3) # 두번 실행해야 bb에 있는 3이 모두 삭제됨
print(bb)
print(even)

print(even.pop()) # Push & Pop의 Pop(스택의 기능 pop())
print(even.pop()) # 마지막 값을 빼내는 행위
# append() : 마지막에 할당(추가) / pop() : 마지막 값 꺼내기
print(even)

# 튜플
# 리스트와 동일하나 삭제,편집 불가
tVal = (1, 3, 5, 7, 9)

# tVal[2] = 11 # 튜플은 한 번 생성되면 끝까지 그대로 사용 / 변경 및 삭제 불가능 !
# del tVal[2]
print(tVal)