# file : p54_captWeather.py
# desc : 네이버 날씨 화면 캡쳐

import pyautogui as auto # pyautogui 라이브러리를 auto라는 이름으로 참조하겠다 선언
import pyperclip as clip # pyperclip 라이브러리는 clip으로 선언
import time

# auto.mouseInfo()

auto.click(88, 154,duration=0.5) # pyautogui.click과 동일한 문장. (88, 154)의 좌표 위치를 클릭하는 동작 수행, duration은 클릭 동작의 지속 시간 설정
auto.hotkey('ctrl','a') # 키보드의 여러키를 동시에 누르거나 뗄 때 사용되는 기능, ctrl과 a를 함께 누름으로 전체 선택 기능을 수행
time.sleep(0.05)

regions = ['서울','강원','대구','부산','대전']  # 지역 배열 선언 / 정의

for region in regions:
    auto.moveTo(90, 154,duration=0.5)
    auto.hotkey('ctrl','a')
    time.sleep(0.2)
    clip.copy(f'{region} 날씨')
    auto.hotkey('ctrl','v')
    time.sleep(0.2)

    auto.press('enter')
    time.sleep(1.0)

    startX, startY = 31,272
    endX,endY = 694,906
    auto.screenshot(f'day08/{region}날씨.png',region=(startX,startY,endX-startX,endY-startY))
clip.copy('부산 용당동 날씨')

auto.hotkey('ctrl','v')
time.sleep(0.05)

auto.press('enter')
time.sleep(1.0)

startX, startY = 31,272
endX,endY = 694,906

# auto.screenshot만 사용하면 macOS에서 동작X
# im = auto.screenshot(region=(startX, startY, endX-startX, endY-startY))
# im.save(f'./day08/{region}날씨.png')

auto.screenshot('./day08/todayWeather.png',region=(startX,startY,endX-startX,endY-startY))

print('저장완료')
