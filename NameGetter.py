import os
from datetime import datetime
import sys
import BanBots


def GetAllNamesJustCopy(fileName):
    str1 = ""
    try:
        readfile = open(fileName, "r")
        for line in readfile:
            str1 += line
    except FileNotFoundError:
        sys.exit("File name was wrong or doesn't exist")

    stringSplit = str1.split()
    if not stringSplit:
        sys.exit('There are no words in the given file')

    # Get's all the names for bots who are following or talking.
    follow_or_talking = FollowOrTalking(stringSplit)

    # Checks all the names for duplicates and if there is one then remove it
    no_double_names = RemovingDuplicateNames(follow_or_talking)

    # Starts banning all the bots
    BanBots.BanBots(PrintingToTxt(no_double_names))


def FollowOrTalking(stringSplit):
    all_names = []
    is_true = True
    print("following = 1")
    print("timestamp = 2")
    wordOrTimestamp = input()
    if wordOrTimestamp == '2':
        # Gives per timestamp
        timestamps = []
        while is_true:
            print("\nSay stop if you want to stop the input for timestamps:")
            x = input(f"Give the timestamp of the names you want to get: ")
            if x == "stop" or x == "Stop":
                is_true = False
            else:
                timestamps.append(x)
        for i in range(len(stringSplit)):
            for j in range(len(timestamps)):
                if stringSplit[i] == timestamps[j]:
                    all_names.append(stringSplit[i + 1][:-1])
        print("Got all the spamming bots\n")
        return all_names
    else:
        # Gives for following
        for i in range(len(stringSplit)):
            if stringSplit[i] == "following":
                all_names.append(stringSplit[i + 1])
        print("Got all the following bots\n")
        return all_names


def RemovingDuplicateNames(all_names):
    no_double_names = []
    print("Removing duplicates...")
    for name in all_names:
        is_the_same = False
        # If the name has a double add it here
        for double in no_double_names:
            if double == name:
                is_the_same = True
        # If the name is not in there already add it here
        if not is_the_same:
            no_double_names.append(name)
            print(name)
    return no_double_names


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
    return directory


def DirectoryGetter():
    file_name = input("Enter the name of the file without the .txt:")
    directory = os.getcwd() + "\InputNames"
    directory = directory + f"\{file_name}.txt"
    return directory


print(GetAllNamesJustCopy(DirectoryGetter()))
