import pyautogui
import time
import os


def BanBots():
    print("Now to ban the bots!!")
    file_name = input("\nEnter the name of the file without the .txt:")
    directory = os.getcwd() + "\EndResults"
    directory = directory + f"\{file_name}.txt"

    t = int(input("\nGive the amount of time I should wait: "))

    def countdown(t):  # The program to count down
        while t > 0:
            print(t)
            t -= 1
            time.sleep(1)
        print("SPAM!")

    countdown(t)  # The Amount you want o count down
    # print(directory)
    try:
        f = open(directory, 'r')  # The file where it gets the data from
        for name in f:
            pyautogui.typewrite(f"/ban {name}")
            time.sleep(0.1)
            pyautogui.press("enter")
    except FileNotFoundError:
        print("File name was wrong or doesn't exist")

