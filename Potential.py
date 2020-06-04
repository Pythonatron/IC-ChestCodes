import ctypes
import sys
import time

import pyperclip
import win32gui
from pynput.mouse import Button, Controller, Listener

awareness = ctypes.c_int()
ctypes.windll.shcore.SetProcessDpiAwareness(2)

mouse = Controller()

def getRekt():
    global x, y
    hwnd = win32gui.FindWindow(None, 'Idle Champions')
    rect = win32gui.GetWindowRect(hwnd)
    x, y = rect[0], rect[1]
    time.sleep(0.4)

def innerScreen():
    global innerx, innery
    innerx, innery = int(x+9), int(y+38)
    mouse.position = innerx, innery
    time.sleep(0.5)

def chestButton():
    global chestbx, chestby
    chestbx, chestby = int(innerx+163), int(innery+82)
    mouse.position = chestbx, chestby
    mouse.click(Button.left, 1)
    time.sleep(0.6)

def unlockChest():
    global unlockx, unlocky
    unlockx, unlocky = int(chestbx-75), int(chestby+500)
    mouse.position = unlockx, unlocky
    mouse.click(Button.left, 1)
    time.sleep(0.7)
    
def clickPaste():
    global pastex, pastey
    pastex, pastey = int(unlockx+88), int(unlocky+85)
    mouse.position = pastex, pastey
    mouse.click(Button.left, 1)
    time.sleep(0.8)
    
def copyCode():
    global chestcode
    #read stuff from chests.txt
    chestcode = code
    pyperclip.copy(chestcode)
    time.sleep(2)
    
def clickUnlock():
    global clicky, clickx
    clickx, clicky = int(pastex+455), int(pastey-110)
    mouse.position = clickx, clicky
    mouse.click(Button.left, 1)
    time.sleep(0.9)
    
def error():
    global errorx, errory
    errorx, errory = int(clickx+5), int(clicky-160)
    mouse.position = errorx, errory
    mouse.click(Button.left, 1)
    time.sleep(6.0)
    
def clickCard():
    global cardx, cardy
    cardx, cardy = int(errorx+90), int(errory-230)
    mouse.position = cardx, cardy
    mouse.click(Button.left, 1)
    time.sleep(1.1)

def doneButton():
    global donex, doney
    donex, doney = int(cardx), int(cardy+195)
    mouse.position = donex, doney
    mouse.click(Button.left, 1)
    time.sleep(1.2)
    
def Startup():
    print("*****************************************************")
    print("*  Do not minimize Idle Champions Window            *")
    print("*  Do not move 'IC' window once program has started *")
    print("*  And sadly it has to be in the foreground         *")
    print("*****************************************************")
    print("Getting infomation on IC...")
    getRekt()

def mainLoop():
    Startup()
    print("Absolute Top-Left of IC Window:        [{}, {}]".format(x, y))
    innerScreen()
    print("Moving mouse to inner IC top-left..    [{}, {}]".format(innerx, innery))
    chestButton()
    print("Moving mouse to Chest button in IC..   [{}, {}]".format(chestbx, chestby))
    unlockChest()
    print("Moving mouse to Unlock Chest button..  [{}, {}]".format(unlockx, unlocky))
    copyCode()
    print("Pasting code..               [{}]".format(chestcode))
    clickPaste()
    print("Moving mouse to Paste Code button..    [{}, {}]".format(pastex, pastey))
    clickUnlock()
    print("Moving mouse to Unlock button..        [{}, {}]".format(clickx, clicky))
    error()
    print("Clicking error area just in case..     [{}, {}]".format(errorx, errory))
    clickCard()
    doneButton()

def noteslul():
    print("Animations--")
    print("\tRoughly 5 seconds for chest open animation")
    print("\tRoughly 5 seconds for chest reset animation")
    print("Coordinates--")
    print("\t9, 38 from top left corner border to screen top left")
    print("\t163, 82 from top left corner to chest button")
    print("\t-75, 500 from chest button to unlock chest button")
    print("\t455, -110 from somewhere to unlock button")
    print("\t5, -160 from unlock to error ok")
    print("\t90, -230 from error to single card")
    print("\t0, 195 from single card to done button")
    print("Notes on Mouse Controlling--")
    print("\tmouse = Controller()")
    print("\tmouse.position")
    print("\tmouse.position = (X, Y)")
    print("\tmouse.move(X, Y)")
    print("\tmouse.click(Button.right, 1)")