import pyautogui, time
time.sleep(5)
f = open("eminem", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.typewrite("enter")
