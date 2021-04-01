import os
from datetime import datetime
import sys
import BanBots


def GetAllNamesJustCopy(fileName):
    all_names = []
    str1 = ""
    try:
        readfile = open(fileName, "r")
        for line in readfile:
            str1 += line
    except FileNotFoundError:
        print("File name was wrong or doesn't exist")

    timestamps = []
    is_true = True
    while is_true:
        print("\nSay stop if you want to stop the input for timestamps:")
        x = input(f"Give the timestamp of the names you want to get: ")
        if x == "stop" or x == "Stop":
            is_true = False
        else:
            timestamps.append(x)
    test = str1.split()
    for i in range(len(test)):
        for j in range(len(timestamps)):
            if test[i] == timestamps[j]:
                all_names.append(test[i + 1])
                # all_names.append(test[i + 1][:-1])  # Appends with i+ and then removes last letter
                # TODO MAKE A SEARCH ON SPAMMER OR FOLLOWBOT
        # if test[i] == "0:10" or test[i] == "0:09":

    no_double_names = []

    for name in all_names:
        # print(name)
        if not no_double_names:
            no_double_names.append(name)
        is_the_same = False
        for double in no_double_names:
            if double == name:  # Checker if the name isn't the same
                # print("FOUND NAME THAT WAS THE SAME")
                is_the_same = True

        if not is_the_same:  # Name gets added here
            # print("Name Added")
            no_double_names.append(name)
    for name in no_double_names:
        print(name)

    PrintingToTxt(no_double_names)


def DirectoryGetter():
    file_name = input("Enter the name of the file without the .txt:")
    directory = os.getcwd() + "\InputNames"
    directory = directory + f"\{file_name}.txt"
    return directory


def PrintingToTxt(printedToTxt):
    directory = os.getcwd() + "\EndResults"
    now = datetime.now()
    today = now.strftime("%d-%m-%Y %H-%M")
    directory = directory + f"\{today}.txt"
    # f = open(directory, 'w')
    original_stdout = sys.stdout
    with open(directory, 'w') as f:
        sys.stdout = f
        for name in printedToTxt:
            print(name)
        sys.stdout = original_stdout


print(GetAllNamesJustCopy(DirectoryGetter()))
BanBots.BanBots()