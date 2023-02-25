import win32process
import time 
import csv
import pandas as pd
import pymouse,pykeyboard,os,sys
from pymouse import *
import pyautogui
from pykeyboard import PyKeyboard
import pyperclip

m = PyMouse()
k = PyKeyboard()

handle = win32process.CreateProcess("C:\\Users\student\\AppData\\Local\Programs\\Cisco Spark\\CiscoCollabHost.exe",'', None , None , 0 ,win32process. CREATE_NO_WINDOW , None , None ,win32process.STARTUPINFO())
time.sleep(2)
m.click(1000,504,1,1)
time.sleep(0.5)
k.type_string("26427466208")

k.press_key(k.tab_key)
time.sleep(0.5)
k.press_key(k.tab_key)

time.sleep(0.5)

k.type_string("Liao Bo Hao") # 目前只能輸入英文 需要中文再調整
k.press_key(k.tab_key)
time.sleep(0.5)
k.press_key(k.tab_key)
time.sleep(0.5)
k.type_string("請輸入自己的email")
k.press_key(k.enter_key)
time.sleep(2)
k.press_key(k.enter_key)
time.sleep(2)
k.press_key(k.enter_key)
time.sleep(4)
k.type_string("BDSE28@iSpan")
k.press_key(k.enter_key)
k.press_key(k.enter_key)
k.press_key(k.enter_key)

