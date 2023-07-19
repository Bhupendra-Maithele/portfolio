
import pyautogui
import time

t = 1

def handle_change():
    pyautogui.hotkey('ctrl', 'pgup')
time.sleep(t)

def handle_update(lines):
    for _ in range(lines):
        pyautogui.press('up')
    time.sleep(t)

def handle_delete(lines):
    for _ in range(lines):
        pyautogui.press('down')
    time.sleep(t + 4)

while True:
    handle_change()          
    handle_update(25)          
    handle_delete(25)