picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

def BetterAllignWithJust(dict, lwidth, rwidth):
    print ("PICNIC ITEMS".center(lwidth + rwidth, "-"))

    for k,v in picnicItems.items():
        print (k.upper().ljust(lwidth, ".") + str(v).rjust(rwidth, "."))

print()
BetterAllignWithJust(picnicItems, 20, 5)
print()
