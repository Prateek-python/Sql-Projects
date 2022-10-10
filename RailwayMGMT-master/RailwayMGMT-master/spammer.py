import random
# import webbrowser
import pyautogui
print(pyautogui.position())
import pyautogui as pg
import time
# webbrowser.open('https://web.whatsapp.com/')
animal=('#930🤣Prakhar','#930🤣🤣Prakhar','#930🤣🤣Prakhar',)
pyautogui.click(906,949)
# time.sleep(10)
#
for i in range(500):
    a=random.choice(animal)
    pyautogui.typewrite(a)
    pg.press('enter')