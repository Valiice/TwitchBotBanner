import pyautogui
import time
import os

fileName = input("Enter the name of the file without the .txt:")
directory = os.getcwd()+"\EndResults"
directory = directory+f"\{fileName}.txt"
def countdown(t): # The program to count down
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("SPAM!")

countdown(4) # The Amount you want o count down
print(directory)

f = open(directory, 'r') # The file where it gets the data from
for name in f:
    pyautogui.typewrite(f"/ban {name}")
    pyautogui.press("enter")