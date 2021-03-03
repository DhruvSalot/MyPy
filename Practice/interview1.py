cal1 = [['9:00','10:30'], ['12:00','13:00'], ['16:00','18:00']]
bound1 = ['9:00','20:00']
cal2 =[['10:00','11:30'], ['12:30','14:30'], ['14:30','15:00'], ['16:00','17:00']]
bound2 = ['10:00','18:30']

# making viable time list
newCal1 = []
for i in range(len(cal1)-1):
    newCal1 += [[cal1[i][1],cal1[i+1][0]]]
newCal1 += [[cal1[len(cal1)-1][1],bound1[1]]]

newCal2 = []
for i in range(len(cal2)-1):
    newCal2 += [[cal2[i][1],cal2[i+1][0]]]
newCal2 += [[cal2[len(cal2)-1][1],bound2[1]]]

# newCal1 = [['10:30', '12:00'], ['13:00', '16:00'], ['18:00', '20:00']]
# newCal2 = [['11:30', '12:30'], ['14:30', '14:30'], ['15:00', '16:00'], ['17:00', '18:30']]

# removing unwanted time for example in newCal2 ['14:30', '14:30'] and ['16:00', '16:00']
i = 0
while i < len(new_cal1):
    if newCal1[i][0] == newCal1[i][1]:
        del newCal1[i]
        i -= 1
    else :
        i += 1


i = 0
while i < len(newCal2):
    if newCal2[i][0] == new_cal2[i][1]:
        del newCal2[i]
        i -= 1
    else :
        i += 1

# newCal1 = [['10:30', '12:00'], ['13:00', '16:00'], ['18:00', '20:00']]
# newCal2 = [['11:30', '12:30'],['15:00', '16:00'], ['17:00', '18:30']]

# defining a compare function to compare between times
def compare(a, b):
    a1 = a.split(":")
    b1 = b.split(":")
    if   int(a1[0])*60 + int(a1[1]) >= int(b1[0])*60 + int(b1[1]):
         return (True)
    else :
         return (False)

# Concising the list to minimum list
if len(newCal1) >= len(newCal2):
    noOfLoop = len(newCal2)
else:
    noOfLoop = len(newCal1)

# Making List for from time to to time
# fromList = from time
# toList   = to   time
fromList = []
for i in range(noOfLoop):
    if compare(newCal1[i][0], newCal2[i][0]) == True:
        fromList += [newCal1[i][0]]
    else:
        fromList += [newCal2[i][0]]

toList = []
for i in range(noOfLoop):
    if compare(newCal1[i][1], newCal2[i][1]) == False:
        toList += [newCal1[i][1]]
    else:
        toList += [newCal2[i][1]]

# fromList = ['11:30', '15:00', '18:00']
# toList = ['12:00', '16:00','18:30']


# Making final list
# i.e of form [from time, to time]
finalList = []
for i in range(len(fromList)):
    finalList += [[fromList[i], toList[i]]]

print (finalList)
