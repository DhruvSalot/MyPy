Birthday = {"Dhruv" : "28/05/2002", "Diya" : "26/01/2004"}

while True :
    print ("Enter a name to search for in birthay dictionary.")
    name = input ("> ")

    if name == "":
        break

    if name in Birthday:
        print (name + "'s birthday is on " + Birthday[name])

    else :
        print ("I don't know when %s's birthday is on." % name)
        print ("When is their birthday? ")
        bday = input(">")
        Birthday[name] = bday
        print ("Birthday data base updated.")
