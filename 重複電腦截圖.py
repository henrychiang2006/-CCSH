import pyautogui
import time
pyautogui.click(10,10)
time.sleep(0.5)
im2 = pyautogui.screenshot('1.png',region=(556,131,891,697))
for i in range(2,5):
    pyautogui.click(755,123)
    im = pyautogui.screenshot(f"{i}.png",region=(556,131,891,697))
    time.sleep(2)