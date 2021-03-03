spam = ['apples', 'bananas', 'tofu', 'cats']


# Method 1 :
def ListingEle1(list):
    a = ""
    for i in list :
        if   list.index(i) <  len(list) - 2   :
            a += str(i) + ", "
        elif list.index(i) == len(list) - 2   :
            a += str(i) + " & "
        elif list.index(i) == len(list) - 1   :
            a += str(i) + "."
    print (a)
ListingEle1(spam)

# Method 2 :
def ListingEle2(list):
    a = ""
    for i in range(int(len(list))) :
        if i < int(len(list) - 2):
            a += str(list[i]) + ", "
        elif i == int(len(list) - 2):
            a += str(list[i] + " & ")
        elif i == int(len(list) - 1):
            a += str(list[i]) + "."
    print (a)
ListingEle2(spam)
