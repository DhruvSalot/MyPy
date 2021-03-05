#making program that converts given number to roman number form (numbers in range(1000))

keyNum = [1, 4, 5, 9, 10, 40, 50, 90, 100,
           400, 500, 900, 1000]

roNumDict = {1   : "I",
             4   : "IV",
             5   : "V",
             9   : "IX",
             10  : "X",
             40  : "XL",
             50  : "L",
             90  : "XC",
             100 : "C",
             400 : "CD",
             500 : "D",
             900 : "CM",
             1000 : "M" }

inputNum = (input("> "))

def romanNum(str, list, dict):
    for i in range(len(list)):
        if list[i] - int(str) > 0:
             return(list[i-1])
             break

myList = []
number = int(inputNum)
while number > 0 :
    myList +=[romanNum(number, keyNum, roNumDict)]
    number -= romanNum(number, keyNum, roNumDict)

finalStr = ""
for i in range(len(myList)):
    for k, v in roNumDict.items():
        if k == myList[i]:
            finalStr += v
        continue

print(finalStr)
