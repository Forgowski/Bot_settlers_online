import pyautogui
import time
import keyboard
import numpy
import random
import win32api
import win32con


quest_counter = 0
time.sleep(2)

def cords(x, y):
    pyautogui.moveTo(x ,y)
    time.sleep(1.3)
    pyautogui.click(x, y)
    time.sleep(1)
def collects():
    cords(x=665, y=689)
    cords(x=801, y=736)
    cords(x=946, y=762)
    cords(x=1112, y=720)
    cords(x=1028, y=554)
    cords(x=1108, y=475)
    cords(x=1250, y=515)
    cords(x=900, y=383)
    cords(x=1040, y=270)
    cords(x=643, y=239)
    cords(x=750, y=78)
    cords(x=807, y=300)

def attack(gx ,gy ,ex ,ey):
    time.sleep(random.uniform(0.8, 1.2))  # 1
    pyautogui.moveTo(gx, gy)  # set mouse position
    time.sleep(random.uniform(0.8, 1.2))
    pyautogui.click(gx, gy)  # choosing ghost
    while True:
        time.sleep(random.uniform(0.8, 1.2))
        if pyautogui.locateOnScreen('gotowy5.jpg', confidence=0.7):
            break;
        else:
            pyautogui.click(gx, gy)
    time.sleep(random.uniform(0.8, 1.2))
    pyautogui.click(x=811, y=420)  # press attack
    time.sleep(random.uniform(0.8, 1.2))
    pyautogui.moveTo(ex, ey)
    time.sleep(random.uniform(0.8, 1.2))
    pyautogui.click(ex, ey)  # choose enemy

def sendAttack():
    attack(617, 248, 546, 193)

    attack(650, 257, 876, 222)

    attack(677, 270, 1002, 257)

    attack(629, 272, 1188, 518)

    attack(651, 286, 837, 488)

    attack(674, 301, 957, 746)



def pressStar():
    pyautogui.click(953, 883)


def sendGhost():
    pressStar()
    time.sleep(random.uniform(0.8, 1.2))
    pyautogui.click(1015, 473, clicks=2)
    time.sleep(random.uniform(0.8, 1.2))
    spellGhost()
    for i in range(6):
        time.sleep(1)
        pyautogui.click(726 + i * 58, 526) #choose general
        time.sleep(1)
        pyautogui.click(809, 589)
        time.sleep(1)
        pyautogui.click(920, 600)
        time.sleep(0.3)
        pressStar()
    time.sleep(15)


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
    need_wait_more = True
    while need_wait_more:
        if pyautogui.locateOnScreen('gotowe duchy.jpg', confidence=0.95) or pyautogui.locateOnScreen('gotowe duchy2.jpg', confidence=0.95):
            need_wait_more = False
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
        pressStar()

def confirmQuest():
    global quest_counter
    quest_counter += 1
    time.sleep(random.uniform(0.8, 1.2))
    pyautogui.click(1029, 760)
    time.sleep(random.uniform(0.8, 1.2))

def acceptQuest():
    if pyautogui.locateOnScreen('misja1.jpg', confidence=0.9):
        pyautogui.click(pyautogui.locateOnScreen('misja1.jpg', confidence=0.9))
        confirmQuest()

    elif pyautogui.locateOnScreen('misja2.jpg', confidence=0.9):
         pyautogui.click(pyautogui.locateOnScreen('misja2.jpg', confidence=0.9))
         confirmQuest()

    elif pyautogui.locateOnScreen('misja3.jpg', confidence=0.9):
         pyautogui.click(pyautogui.locateOnScreen('misja3.jpg', confidence=0.9))
         confirmQuest()

    elif pyautogui.locateOnScreen('misja4.jpg', confidence=0.9):
         pyautogui.click(pyautogui.locateOnScreen('misja4.jpg', confidence=0.9))
         confirmQuest()

    elif pyautogui.locateOnScreen('misja5.jpg', confidence=0.9):
         pyautogui.click(pyautogui.locateOnScreen('misja5.jpg', confidence=0.9))
         confirmQuest()
    elif pyautogui.locateOnScreen('ukonczone zadanie.jpg', confidence=0.6):
         pyautogui.keyDown('f2')
         time.sleep(4)
    time.sleep(3)


while True:
    time.sleep(4)
    pressStar()
    while True:
        time.sleep(random.uniform(0.3, 0.5))
        if pyautogui.locateOnScreen('openstar.jpg', confidence=0.6):
            break
        else:
            pressStar()


    time.sleep(random.uniform(0.8, 1.2))
    pyautogui.click(1015, 473, clicks=2)
    time.sleep(0.5)
    spellGhost()
    time.sleep(random.uniform(0.8, 1.2))
    ghostService()
    pyautogui.click(1015, 473, clicks=2)
    startAdventure()
    need_wait_more = True
    while need_wait_more:
        if pyautogui.locateOnScreen('pole przygody.jpg', confidence=0.8):
            time.sleep(1)
            print("x")
            need_wait_more = False
    time.sleep(random.uniform(0.8, 1.2))
    sendGhost()
    time.sleep(random.uniform(0.8, 1.2))
    pyautogui.click(1829, 445)
    time.sleep(random.uniform(0.8, 1.2))
    pyautogui.click(1829, 455)
    time.sleep(random.uniform(0.8, 1.2))
    need_wait_more = True
    while need_wait_more:
        if pyautogui.locateOnScreen('oboz.jpg', confidence=0.8):
            for i in range(10):
                pyautogui.scroll(-1600)
            time.sleep(random.uniform(0.8, 1.2))
            centre_cords = pyautogui.locateOnScreen('oboz.jpg', confidence=0.8)
            print(centre_cords)
            pyautogui.moveTo(centre_cords)
            time.sleep(random.uniform(0.8, 1.2))
            pyautogui.mouseDown()
            time.sleep(random.uniform(0.8, 1.2))
            pyautogui.moveTo(960, 400)
            pyautogui.mouseUp()
            need_wait_more = False
    pressStar()
    time.sleep(random.uniform(0.8, 1.2))
    pyautogui.click(1015, 473, clicks=2)
    time.sleep(random.uniform(0.8, 1.2))
    spellGhost()
    need_wait_more = True
    while need_wait_more:
        if pyautogui.locateOnScreen('gotowe duchy.jpg', confidence=0.95) or pyautogui.locateOnScreen('gotowe duchy2.jpg', confidence=0.95):
            time.sleep(random.uniform(0.8, 1.2))
            need_wait_more = False
            pressStar()
            time.sleep(random.uniform(0.8, 1.2))
            sendAttack()

    time.sleep(random.uniform(0.8, 1.2))  # 1
    pyautogui.moveTo(651, 286)  # set mouse position
    time.sleep(random.uniform(0.8, 1.2))
    pyautogui.click(651, 286)  # choosing ghost

    need_wait_more = True
    while need_wait_more:
        time.sleep(2)
        if pyautogui.locateOnScreen('zajety.jpg', confidence=0.9):
            time.sleep(random.uniform(0.8, 1.2))
        else:
            need_wait_more = False
            pyautogui.click(1226, 366)
            attack(617, 248,957, 401)


    time.sleep(30)
    pyautogui.moveTo(126, 222, 0.3)
    pyautogui.click(126, 222)

    quest_counter = 0
    while quest_counter < 2:
        acceptQuest()

    pyautogui.click(x=1372, y=312)
    time.sleep(10)
    collects()
    time.sleep(5)
    pyautogui.moveTo(126, 222, 0.3)
    pyautogui.click(126, 222)
    quest_counter = 0
    while quest_counter < 3:
        acceptQuest()
    time.sleep(5)
    pyautogui.click(1029, 760)
    time.sleep(5)
    pyautogui.click(919, 592)
    time.sleep(15)
    pyautogui.click(960, 769)
    time.sleep(5)


