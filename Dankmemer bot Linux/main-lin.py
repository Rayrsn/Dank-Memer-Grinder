import pynput
import random
import time
import os
import termcolor
import colorama
#linux dependencies
import gi
gi.require_version("Wnck", "3.0")
from gi.repository import Wnck

from pynput import keyboard
from pynput.keyboard import Key, Controller
memetypes = ["f" , "r" , "i" , "c", "k"]
searchtypes = ["sink" , "air" , "tree" , "glovebox" , "bed" , "sewer" , "attic" , "dumpster" , "discord" , "mailbox"]
randcmd = ["pls profile" , "pls inv 1" , "pls inv 2" , "pls inv 3" , "pls inv 4" , "pls shop 1" , "pls shop 2" , "pls shop 3" , "pls shop 4" , "pls rich" , "pls ping"]
randtime = ["31" , "32" , "33" , "34" , "35" , "36"]
randnum = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8", "9", "10"]
trivtypes = ["a", "b", "c", "d"]
highlowtypes = ["low", "high"]

colorama.init()
y = 0
os.system('clear')
print('Type the name of the window')
u = input()

def pm():
    print('Executing "pls pm"')
    keyboard = Controller()
    keyboard.type('pls pm')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(1, 2))
    keyboard.type(random.choice(memetypes))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(2, 3))

def hunt():
    print('Executing "pls hunt"')
    keyboard = Controller()
    keyboard.type('pls hunt')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(5, 7))

def fish():
    print('Executing "pls fish"')
    keyboard = Controller()
    keyboard.type('pls fish')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(5, 7))

def beg():
    print('Executing "pls beg"')
    keyboard = Controller()
    keyboard.type('pls beg')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(1, 3))

def rand1():
    print('Executing "rand"')
    keyboard = Controller()
    keyboard.type(random.choice(randcmd))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(5, 7))

def rand2():
    print('Executing "rand"')
    keyboard = Controller()
    keyboard.type(random.choice(randcmd))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(5, 7))

def guess():
    print('Executing "pls guess"')
    keyboard = Controller()
    keyboard.type('pls guess')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(1, 2))
    keyboard.type(random.choice(randnum))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(1, 2))
    keyboard.type('hint')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(1, 2))
    keyboard.type(random.choice(randnum))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(1, 2))
    keyboard.type(random.choice(randnum))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(2, 3))

def triv():
    print('Executing "pls triv"')
    keyboard = Controller()
    keyboard.type('pls triv')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(1, 2))
    keyboard.type(random.choice(trivtypes))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(2, 3))

def meme1():
    print('Executing "pls meme1"')
    keyboard = Controller()
    keyboard.type('pls meme')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(5, 6))

def meme2():
    print('Executing "pls meme2"')
    keyboard = Controller()
    keyboard.type('pls meme')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(5, 6))

def meme3():
    print('Executing "pls meme3"')
    keyboard = Controller()
    keyboard.type('pls meme')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(5, 6))

def dep():
    print('Executing "pls dep all"')
    keyboard = Controller()
    keyboard.type('pls dep all')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(5, 6))

def hl():
    print('Executing "pls hl"')
    keyboard = Controller()
    keyboard.type('pls hl')
    keyboard.press(Key.enter)
    time.sleep(random.randint(1, 2))
    keyboard.type(random.choice(highlowtypes))
    keyboard.press(Key.enter)
    time.sleep(random.randint(2, 3))

import time
import termcolor
#from win32gui import GetWindowText, GetForegroundWindow
print('Waiting... 5 seconds ', end='')
print(termcolor.colored('Please click on Discord', 'green',))
time.sleep(5)
scr = Wnck.Screen.get_default()
scr.force_update()
x = scr.get_active_window().get_name()
os.system('clear')

p = 0

if x == u:
    print(termcolor.colored('Active Window: ', 'green') + x)
else:
    print(termcolor.colored('Active Window: ', 'white', 'on_red') + x)
    p = 2

if x == u:
    print(termcolor.colored('Focused on Discord', 'green'))

#ENTER THE FUNCTION NAMES HERE (AFTER DEFINING THEM OF COURSE)

def theloop():
    functions = [pm, hunt, fish, beg, rand1, rand2, triv, meme1, meme2, meme3, hl]
    random.shuffle(functions)
    os.system('clear')
    global x
    if x == u:
        print(termcolor.colored('Active Window: ', 'green') + x)
        print(termcolor.colored('Focused on Discord', 'green'))

    for functions in functions:
        scr = Wnck.Screen.get_default()
        scr.force_update()
        x = scr.get_active_window().get_name()
        if x != u:
            os.system('clear')
            print(termcolor.colored('Lost focus of Discord, exiting the script...', 'white', 'on_red'))
            time.sleep(5)
            exit()
        functions()
    scr = Wnck.Screen.get_default()
    scr.force_update()
    x = scr.get_active_window().get_name()
    if x != u:
        os.system('clear')
        print(termcolor.colored('Lost focus of Discord, exiting the script...', 'white', 'on_red'))
        time.sleep(5)
        exit()
    dep()
    print('Waiting... 11-16 seconds')
    time.sleep(random.randint(11, 16))

while p < 1:
    if x == u:
        theloop()
        
else:
    os.system('clear')
    print(termcolor.colored('Please click on Discord immediately after running the script', 'grey', 'on_red'))
