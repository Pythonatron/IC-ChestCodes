import ctypes
import os
import sys
import time

import pyperclip
import win32gui
from pynput.mouse import Button, Controller, Listener

awareness = ctypes.c_int()
ctypes.windll.shcore.SetProcessDpiAwareness(2)

mouse = Controller()

def getrekt():
    global x, y
    hwnd = win32gui.FindWindow(None, 'Idle Champions')
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    time.sleep(0.4)

def innerScreen():
    global innerx, innery
    innerx = int(x+9)
    innery = int(y+38)
    mouse.position = innerx, innery
    time.sleep(0.5)

def chestButton():
    global chestbx, chestby
    chestbx = int(innerx+163)
    chestby = int(innery+82)
    mouse.position=chestbx, chestby
    mouse.click(Button.left, 1)
    time.sleep(0.6)

def unlockChest():
    global unlockx, unlocky
    unlockx = int(chestbx-75)
    unlocky = int(chestby+500)
    mouse.position= unlockx, unlocky
    mouse.click(Button.left, 1)
    time.sleep(0.7)
    
def clickpaste():
    global pastex, pastey
    pastex = int(unlockx+88)
    pastey = int(unlocky+85)
    mouse.position = pastex, pastey
    mouse.click(Button.left, 1)
    time.sleep(0.8)
    
def copycode():
    #read stuff from chests.txt
    pyperclip.copy("DIXYHAIRBLOG")
    time.sleep(2)
    
def clickunlock():
    global clicky, clickx
    clickx = int(pastex+455)
    clicky = int(pastey-110)
    mouse.position = clickx, clicky
    mouse.click(Button.left, 1)
    time.sleep(0.9)
    
def error():
    global errorx, errory
    errorx = int(clickx+5)
    errory = int(clicky-160)
    mouse.position = errorx, errory
    mouse.click(Button.left, 1)
    time.sleep(1.0)
    
def clickcard():
    global cardx, cardy
    cardx, cardy = int(errorx+90),int(errory-230)
    mouse.position = cardx, cardy
    mouse.click(Button.left, 1)
    time.sleep(1.1)
    
print("*****************************************************")
print("*  Do not minimize Idle Champions Window            *")
print("*  Do not move 'IC' window once program has started *")
print("*  And sadly it has to be in the foreground         *")
print("*****************************************************")

print("Getting infomation on IC...")
getrekt()
print("Absolute Top-Left of IC Window:        [{}, {}]".format(x, y))
innerScreen()
print("Moving mouse to inner IC top-left..    [{}, {}]".format(innerx, innery))
chestButton()
print("Moving mouse to Chest button in IC..   [{}, {}]".format(chestbx, chestby))
unlockChest()
print("Moving mouse to Unlock Chest button..  [{}, {}]".format(unlockx, unlocky))
copycode()
print("Attempting to paste in code for unlocking.")
clickpaste()
print("Moving mouse to Paste Code button..    [{}, {}]".format(pastex, pastey))
clickunlock()
print("Moving mouse to Unlock button..        [{}, {}]".format(clickx, clicky))
error()
print("Clicking error area just in case..     [{}, {}]".format(errorx, errory))
time.sleep(6)
clickcard()


#roughly 5 seconds for chest open animation
#roughly 5 seconds for chest reset animation

# 9, 38 from top left corner border to screen top left
# 163, 82 from top left corner to chest button
# -75, 500 from chest button to unlock chest button
# 455, -110 from somewhere to unlock button
# 5, -160 from unlock to error ok
# 90, -230 from error to single card
# -40, 275 from single card to potential done button
 




# mouse = Controller()
# mouse.position
# mouse.position = (X, Y)
# mouse.move(X, Y)
# mouse.click(Button.right, 1)