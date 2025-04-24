import pyautogui
import time

def send_message():
    time.sleep(2)
    for i in range(1, 1000001):
        pyautogui.typewrite(f"{i}. Bhaijain.....")
        # pyautogui.typewrite(f"{i}. Hi, I am Muhammad Hassan. Nice to meet you.")
        pyautogui.press('enter')
send_message()