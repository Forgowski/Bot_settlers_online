import pyautogui
import time


time.sleep(2)
pyautogui.keyDown('f2')
while True:
    time.sleep(1)
    print(pyautogui.position())



# need_wait_more = True
# while need_wait_more:
#     if pyautogui.locateOnScreen('oboz.jpg', confidence=0.8):
#         time.sleep(1)
#         print("x")
#         need_wait_more = False