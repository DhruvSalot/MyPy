Inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']

def TotalInInventory(dict, list):
    for item in list:
        dict.setdefault(item, 0)
    for k in dict.keys():
        for i in list:
            if i == k:
                dict[k] += 1
    return (dict)

def displayInventory(dict):
    print ("Inventory:".center(30, '-'))
    ItemTotal = 0
    for k, v in dict.items():
        print (k.ljust(20, ".") + str(v).rjust(10, "."))
        ItemTotal += v
    print ()
    print ("Total number of items: %d" % (ItemTotal))

print ()
displayInventory(TotalInInventory(Inventory, dragonLoot))
print ()
