import pyperclip

x = pyperclip.paste()

def AddingBulletsToClipList(string):
    y = string.split("\n")
    for i in y :
        if i == "":
            continue
        else :
            print ("* ".ljust(3) + i.rjust(10) )

AddingBulletsToClipList(x)
