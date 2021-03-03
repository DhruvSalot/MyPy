tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def LongestStringFinder(list):
    x = 0
    for i in list:
        if len(i) > x:
            x = len(i)
    return x




def TableMaker(list):
    a = ""
    for m in range(len(list[0])):
        b = ""
        for n in range(len(list)):
            b += list[n][m].rjust(LongestStringFinder(list[n])) + " "
        a += b + "\n"
    print (a)

print()
TableMaker(tableData)
