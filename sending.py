import pyautogui
import time
import keyboard
import numpy
import random
import win32api
import win32con

time.sleep(2)
def sendGhost():
    pyautogui.click(953, 883)
    time.sleep(1)
    pyautogui.click(1015, 473, clicks=2)
    time.sleep(1)
    spellGhost()
    for i in range(6):
        time.sleep(1)
        pyautogui.click(726 + i * 58, 526) #choose general
        time.sleep(1)
        pyautogui.click(809, 589)
        time.sleep(1)
        pyautogui.click(920, 600)
        pyautogui.click(953, 883)


def spellGhost():
    pyautogui.keyDown('backspace')
    pyautogui.keyDown('d')
    time.sleep(random.uniform(0.2, 0.35))
    pyautogui.keyDown('u')
    time.sleep(random.uniform(0.2, 0.35))
    pyautogui.keyDown('c')
    time.sleep(random.uniform(0.2, 0.35))
    pyautogui.keyDown('h')

def startAdventure():    #spelling and starting adventure
    pyautogui.keyDown('backspace')
    pyautogui.keyDown('a')
    time.sleep(random.uniform(0.2, 0.35))
    pyautogui.keyDown('r')
    time.sleep(random.uniform(0.2, 0.35))
    pyautogui.keyDown('k')
    time.sleep(1)
    pyautogui.click(784, 526)
    time.sleep(1)
    pyautogui.click(878, 767)   # start
    time.sleep(1)
    pyautogui.click(917, 568)  #confirm start
def ghostService():
    for i in range(6):
        time.sleep(1)
        pyautogui.click(726 + i * 58, 526) #choose general
        time.sleep(1)
        pyautogui.click(1174, 694)  #clear military
        time.sleep(1)
        pyautogui.click(1178, 585, clicks=2) #choose which military you want
        time.sleep(random.uniform(0.2, 0.35))
        pyautogui.keyDown('2')
        time.sleep(random.uniform(0.2, 0.35))
        pyautogui.keyDown('3')
        time.sleep(random.uniform(0.2, 0.35))
        pyautogui.keyDown('0')
        time.sleep(1)
        pyautogui.click(1001, 695)
        time.sleep(1)
        pyautogui.click(1227, 366)
        time.sleep(1)
        pyautogui.click(953, 883)
#while True:
pyautogui.click(953, 883)
time.sleep(1)
pyautogui.click(1015, 473, clicks=2)
time.sleep(0.5)
spellGhost()
time.sleep(1)
ghostService()
pyautogui.click(1015, 473, clicks=2)
startAdventure()
need_wait_more = True
while need_wait_more:
    if pyautogui.locateOnScreen('pole przygody.jpg', confidence=0.8):
        time.sleep(1)
        print("x")
        need_wait_more = False
time.sleep(1)
sendGhost()


