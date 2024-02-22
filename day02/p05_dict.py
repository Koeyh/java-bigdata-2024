# file: p05_dict.dy
# desc: 딕셔너리 자료형, 집합 학습

## 딕셔너리 구성
spiderMan = {'name' : 'Peter Parker', 'age' : 18, 'weapon' : 'Web shooter', 'freinds' : ['ironMan', 'Thor', 'Captain America']}

print(spiderMan)

## 출력
# 딕셔너리 spiderMan의 key name의 값 출력
print(spiderMan['name'])

## 값 추가
spiderMan['job'] = 'CameraMan'
print(spiderMan)

## 값 삭제
del spiderMan['freinds']
print(spiderMan)

## 딕셔너리 함수
print(spiderMan.keys()) # spiderMan 딕셔너리에 존재하는 키 값만 출력
print(list(spiderMan.keys())) # 키 목록을 리스트 형태로 형 변환
print(spiderMan.items()) # 딕셔너리 모든 아이템 출력
print(spiderMan.get('job')) # 딕셔너리의 값 가져오기

print('friends' in spiderMan) # 딕셔너리 안에 in 앞에 위치한 키가 있는지 확인
print(spiderMan.values()) # 값만 출력

res = spiderMan.pop('job') # 딕셔너리에서 지정한 키 값을 꺼냄
print(res)
print(spiderMan) # pop을 통해 빠져나간 값은 전체 목록에서 사라짐

## 데이터 삭제
spiderMan.clear()
print(spiderMan)

del spiderMan # 완전 삭제 / 딕셔너리 자체를 지워버림
print(spiderMan)

## 집합 : 중복허용X, 순서X
# set([1, 2, 3, 4, 3, 4, 2, 1]) = 중복 제거 후 {1, 2, 3, 4} -> {3, 1, 2, 4}등 순서 상관없이 출력