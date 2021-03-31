import os

def hmm(fileName):
    readfile = open(fileName, "r")
    allNames = []
    str1 = ""
    for line in readfile:
        str1 +=line
        
    test = str1.split()
    for i in range(len(test)):
        if test[i] == "0:10" or test[i] == "0:09":
            allNames.append(test[i+1][:-1]) # Appends with i+ and then removes last letter

    for name in allNames:
        print(name)

def GiveAllNames(fileName):
    spl_word = "0:10 "
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    test = []
    for i in range(len(words)):
        x = words[i].partition(spl_word)[2]
        x = x.partition(":")[0]
        test.append(x)
        print(x)

fileName = input("Enter the name of the file without the .txt:")
directory = os.getcwd()+"\EndResults"
directory = directory+f"\{fileName}.txt"
# print(GiveAllNames("Bots.txt"))
print(hmm("allNames.txt"))
print(directory)