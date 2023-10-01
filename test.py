import keyboard
import pyautogui
import time



#test code
def get_coordinates():
    while 1:
        position = pyautogui.position()
        if keyboard.is_pressed('enter'):
            print(position)
            time.sleep(0.2)



# auto click
def click(x, y):
    pyautogui.click(x=x, y=y)
    time.sleep(0.5)

def start_autoplay():
    while 1:
        time.sleep(2)
        click(259, 272)  # 게임 시작 클릭
        click(1362, 562)  # 훈련 버튼 클릭
        click(1087, 562)  # Ai 상대대전 클릭
        click(1230, 544)  # 어려움 버튼 클릭
        click(1419, 971)  # 바로 시작 버튼 클릭
        time.sleep(7)  # 바로시작 딜레이 5초

        # 게임 시작후
        time.sleep(13)  # 게임 로딩 딜레이
        pyautogui.press('esc')
        time.sleep(0.2)
        pyautogui.press('esc')
        click(530, 816)  # esc 전투포기 버튼
        click(854, 640)  # 전투포기 확인 버튼
        time.sleep(11)  # 전투포기 딜레이
        click(959, 936)  # 1차 나가기 버튼
        time.sleep(15)  # 결과창 딜레이
        click(958, 1005)  # 마지막 나가기 버튼
