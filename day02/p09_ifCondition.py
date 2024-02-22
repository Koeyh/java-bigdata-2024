# flie : p09_ifCondition.py
# desc: if 제어문

money = 2800

if money >= 5000:
    #indentation(들여쓰기), if문 내의 들여쓰기 간격으로 중괄호를 대체(간격 유지 필수 !)
    print("택시타고 가")
    print("ㅎㅎ")
elif money >= 2500 and money<5000:
    print("저 앞에서 세워주세요")
else:
    print("걸어가")
    print("ㅎㅎㅎㅎ")

##print() end
print(1 in [1,3,5,7,9], end= ', ')
print(6 in [1,3,5,7,9])