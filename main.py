import pyautogui
import keyboard
import pyperclip
import time


settings_button = [1775,60]
service_button = [500,635]
coupon_button = [1260,550]
coupon_input = [967,558]
enter_button = [853,667]
exit_button = [977,768]

# coupon_number_list = [
#                  "LUCKYSEVEN05","LUCKYSEVEN06","LUCKYSEVEN07","ERSTEAM30000",
#                  "ERTOTHEMOON","ERPLAYTOWIN","ERPLAYFORFUN","ERHAPPYTIME",
#                  "ERPLAYSQUAD","TGSWITHER1","TGSWITHER2","TGSWITHER3",
#                  "TGSWITHER4"]

coupon_list = ["LUCKYSEVEN01","LUCKYSEVEN02","LUCKYSEVEN03","LUCKYSEVEN04",
                 "LUCKYSEVEN05","LUCKYSEVEN06","LUCKYSEVEN07","ERSTEAM30000",
                 "ERTOTHEMOON","ERPLAYTOWIN","ERPLAYFORFUN","ERHAPPYTIME",
                 "ERPLAYSQUAD","TGSWITHER1","TGSWITHER2","TGSWITHER3",
                 "TGSWITHER4"]


# test code
# while 1:
#     position = pyautogui.position()
#     if keyboard.is_pressed('enter'):
#         print(position)
#         time.sleep(0.2)


time.sleep(1)
pyautogui.click(x=settings_button[0],y=settings_button[1])      # 설정 버튼 클릭
time.sleep(0.5)
pyautogui.click(x=service_button[0],y=service_button[1])        # 서비스 버튼 클릭
time.sleep(0.5)
pyautogui.click(x=coupon_button[0],y=coupon_button[1])          # 쿠폰 버튼 클릭
time.sleep(0.5)
pyautogui.click(x=coupon_input[0],y=coupon_input[1])            # 쿠폰 입력창 클릭

# 쿠폰 입력 루프
for i in coupon_list:
    pyperclip.copy(i)               # 클립보드에 텍스트를 복사합니다.
    pyautogui.hotkey('ctrl', 'v')   # 붙여넣기

    pyautogui.click(x=enter_button[0],y=enter_button[1])        # 쿠폰 입력 확인버튼
    time.sleep(2)
    pyautogui.click(x=exit_button[0], y=exit_button[1])         # 쿠폰 입력후 확인버튼(쿠폰 보상 확인버튼)
    time.sleep(1)
    pyautogui.click(x=coupon_button[0], y=coupon_button[1])     # 쿠폰 버튼 클릭
    time.sleep(0.5)
    pyautogui.click(x=coupon_input[0], y=coupon_input[1])       # 쿠폰 입력창 클릭
