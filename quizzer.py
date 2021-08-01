import sys
import io
import os
import random
from termcolor import colored

# Quizzer
# Usage: python quizzer.py dictionary_filename

dictionary = {}
errorRate = []
quadraticError = []
lastDictIndex = -1
saveDir = ""
saveFilename = ""

def getRandomDictIndex():
    global lastDictIndex
    
    totalWeight = sum(quadraticError)
    if lastDictIndex != -1:
        totalWeight = totalWeight - quadraticError[lastDictIndex]
    randomPoint = random.random() * totalWeight
    
    for i in range(len(quadraticError)):
        if i == lastDictIndex:
            continue
        randomPoint = randomPoint - quadraticError[i]
        if randomPoint <= 0:
            lastDictIndex = i
            return i
    
    raise RuntimeError("Failed to generate random dict index")

def giveRandomQuestion():
    global errorRate
    global quadraticError

    dictIndex = getRandomDictIndex()
    
    print("Sum = " + str(round(sum(errorRate), 2)))
    print("Max = " + str(round(max(errorRate), 2)))
    print("\n" * 1)
    print("Current = " + str(round(errorRate[dictIndex], 2)))
    print(dictionary[dictIndex][1])
    print("\n" * 2)
    
    answer = input()
    if answer == dictionary[dictIndex][0]:
        errorRate[dictIndex] = errorRate[dictIndex] * 0.6;
    else:
        errorRate[dictIndex] = errorRate[dictIndex] * 1.7 + 0.3;
    quadraticError[dictIndex] = errorRate[dictIndex] * errorRate[dictIndex];
    
    #clear screen
    print("\n" * 100)
    
    print(dictionary[dictIndex][1])
    print(dictionary[dictIndex][0])
    print("")
    print(answer)
    if answer == dictionary[dictIndex][0]:
        print(colored("Correct", "green"))
    else:
        print(colored("Incorrect", "red"))
    print("\n" * 1)


def loadProgress():
    global dictionary
    global errorRate
    global quadraticError
    global saveDir
    global saveFilename
    
    dictFileFullPath = sys.argv[1]
    baseFolder = os.path.dirname(dictFileFullPath)
    dictFilename = os.path.basename(dictFileFullPath)
    saveDir = os.path.join(baseFolder, "saved")
    saveFilename = os.path.join(saveDir, dictFilename + ".saved")
    
    try:
        with open(saveFilename, "r") as inputFile:
            errorRateTemp = eval(inputFile.read())
            if len(errorRateTemp) != len(dictionary):
                return
            errorRate = errorRateTemp
            quadraticError = [x*x for x in errorRate]
    except FileNotFoundError:
        pass
        
def saveProgress():
    global errorRate
    
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)
    with open(saveFilename, "w") as outputFile:
        outputFile.write(repr(errorRate))
        
def loadDictionary():
    global dictionary
    global errorRate
    
    file = io.open(sys.argv[1], mode = "r", encoding="utf-8")
    fileData = file.read().split('\n')
    dictionary = [[x.strip() for x in line.split('-')] for line in fileData if line != ""]
    for x in dictionary:
        if (len(x) != 2):
            print("Error parsing dictinary")
            print("Incorrect line")
            print(x)
            raise RuntimeError("Incorrect argument")
    
    
def initState():
    global errorRate
    global quadraticError
    errorRate = [1.0 for x in dictionary]
    quadraticError = [1.0 for x in dictionary]
    print(quadraticError)
    
def main():
    if len(sys.argv) != 2:
        print("Error expected at least 1 argument: source data filename")
        return
    
    loadDictionary()
    initState()
    loadProgress()
    
    #clear screen
    print("\n" * 100)
    
    try:
        while True:
            giveRandomQuestion()
    except KeyboardInterrupt:
        saveProgress()
        print("Exiting")

if __name__ == "__main__":
    main()