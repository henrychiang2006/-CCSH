import pyperclip as pc
import keyboard
import pyautogui
while True:
    if keyboard.read_key() == "p":
        x,y=pyautogui.position()
    a1 = (f"{x},{y}")
    pc.copy(a1)
    a2 = pc.paste()
    print(a2)
    print(type(a2))



#while True:
    #if keyboard.read_key() == "p":
        #x,y=pyautogui.position()
        #print(f"{x},{y}")
        