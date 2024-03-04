# file : p55_katalkAuto.py
# desc : 카톡 PC에서 자동으로 메시지 보내기
# pyautogui.ImageNotFoundException 예외 자주 발생

import pyautogui as auto
import pyperclip as clip
import os
import time

katalkLoc = auto.locateOnScreen('./day08/kakaoLoc.png')
print(katalkLoc)
clickPos = auto.center(katalkLoc)
auto.click(clickPos)
time.sleep(0.5)

groupLoc = auto.locateOnScreen('./day08/findLoc.png')
print(katalkLoc)


auto.doubleClick(clickPos)

clip.copy('자동으로 보내는 메시지입니다.')
auto.hotkey('ctrl', 'v')
auto.press('\n')