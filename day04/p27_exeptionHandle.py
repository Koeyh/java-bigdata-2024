# file: p27_exeptionHandle.py
# desc: 예외처리2

# while True:
#     try:
#         select = int(input('메뉴 입력 1.저장, 2.검색, 3.종료 > '))
#     except:
#         print('예외발생, 입력확인.')
#         continue

#     if select == 1:
#         print('입력')
#     elif select == 2:
#         print('검색')
#     elif select == 3:
#         print('프로그램 종료')
#         break
#     else:
#         continue 
import calc
while True:
    select = int(input("메뉴 1.더하기, 2.빼기, 3.곱하기, 4.나누기, 5.종료"))

    

# class Chicken:
#     def fly(self):
#         raise NotImplementedError
    
# koko= Chicken()
# try:
#     koko.fly()
# except Exception as e:
#     print('닭은 못날아 !', e.args)