# file : p51_keyboardAuto.py
# desc : pyautogui로 키보드 제어

import pyautogui as auto
import pyperclip as clip
'''
한글 입력은 pyperlclip
> pip install pyperclip
'''

auto.press('\n')
auto.write("print('Hello Python!!')",interval=0.02)
auto.write("\n", interval=0.01)

auto.write(['H','e','l','l','o','!','!'],interval=0.02)
auto.press('hangul')
auto.write('dkssudgktpdy',interval=0.02)

# 키보드 프레스 기능
auto.press('enter')
auto.press('hanguel')
auto.press('A')


# 키보드 핫키

#
print('Hello Python!!')
# auto.hotkey('ctrl','a')
# auto.hotkey('ctrl','c') #복사
# auto.press('esc') #선택 해제
# auto.press('enter')
# auto.press('enter')
# auto.press('enter')
# auto.hotkey('ctrl','v')
# print('Hello Python!!')


# 한글은 pyautogui에서 입력할 수 없음
clip.copy('반갑습니다.') # 클립보드에 한글 내용을 저장
auto.hotkey('ctrl','v')

