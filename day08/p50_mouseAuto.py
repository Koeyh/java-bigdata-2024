# file : p50_mouseAuto.py
# desc : PyAutoGui로 마우스 제어

'''
파이썬 모듈 설치시는 명령 프롬프트보다 VSCode내 터미널에서 설치를 추천
PyAutoGui 모듈 설치
>pip install pyautogui
'''

import pyautogui as at

print(at.size())  # 메인 모니터 사이즈 Size(width=1920, height=1080)
print(at.position()) # 현재의 마우스 커서 위치

# pyautogui 마우스 설정 창
# pillow 모듈이 같이 설치되어야 색상 표시가 된다

# 마우스 이동(절대좌표)
#at.moveTo(100,51) #(0,0) 이후 이동이 안 됨(Maybe 좌표가 화면 밖으로 인식하는 듯 함)
#at.moveTo(693,53,duration=1) # x축 693, y축 53으로 1초 동안 이동

# # 마우스 이동(상대좌표)
# at.move(505,505,duration=0.5) # 현재 위치에서 x축 500, y축 500으로 0.5 동안 이동

# 마우스 클릭
# at.leftClick(100,100) #해당 위치로 가서 바로 왼쪽버튼 클릭
# at.rightClick(1211,568) # 해당 위치로 가서 바로 오른쪽버튼 클릭
# at.click(x=700,y=300,clicks=4,button='left')

# 마우스 드래그
# at.moveTo(524,300)
# at.dragRel(621,350,button='left',duration=0.5) # 상대 경로
# at.dragTo(621,350,button='left',duration=0.5) # 절대 경로

# 마우스 휠
at.scroll(2000) #양수는 위로
at.scroll(-2000) #음수는 아래로 스크롤

