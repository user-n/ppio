import pyautogui
import time
import math
scrWidth, scrHeight=pyautogui.size()
xcenter=math.ceil(scrWidth/2)-50
ycenter=math.ceil(scrHeight/2)-50
time.sleep(5)
x,y=700,700
pyautogui.moveTo(x, y)
for i in range(x,801):
    pyautogui.click(x,y)
# for first time only 1 line)
pyautogui.alert('done')
time.sleep(5)
