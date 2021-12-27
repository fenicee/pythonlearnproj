import time
import pyautogui
import schedule

#定位坐标
def locateButton():
    buttonlocation = pyautogui.locateOnScreen('test.png', grayscale=True)
    return  buttonlocation

def clickbtn():
    buttonpoint = pyautogui.center(locateButton())
    pyautogui.doubleClick(buttonpoint.x,buttonpoint.y)

pyautogui.doubleClick('test.png')
