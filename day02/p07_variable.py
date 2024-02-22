# file: p07_variable.py
# desc: 변수란
from copy import copy

a = [1,2,3]
print(id(a)) # 변수 z의 메모리 주소 출력

b = a
print(id(b))

c = 1
d = c # c와 d는 같은 주소를 가짐
print(id(c))
print(id(d))

del b[2]
print(a)

e = copy(a)
print(id(e))
del e[1]
print(a)
print(e)
