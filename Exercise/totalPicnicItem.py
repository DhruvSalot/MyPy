import pprint

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
            'Bob': {'ham sandwiches': 3, 'apples': 2},
            'Carol': {'cups': 3, 'apple pies': 1},
            'Dhruv': {'coke': 5, 'cups': 20, 'cakes': 2}}

def totalitems(guest, item):
    ItemTotal = 0
    for v in guest.values():
        ItemTotal += int(v.get(item, 0))
    return ItemTotal

def printingTotal(guest):
    newdict = {}
    for v in guest.values():
        for item in v.keys():
            newdict[item] = str(totalitems(guest, item))
    for key, value in newdict.items():
        print ("- " + key + " " + value)

print()
printingTotal(allGuests)
print()
