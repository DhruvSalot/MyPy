# Qn]Assume the dictionaries in the Blocks' list to be a row of building on land.
# if requirments like gym in the building is present, the dictionary reflects its value to be true.
# make a program which finds the best building to live in to have every requirements near by
# in the below example block no 2 is the answer as for:
# gym one need to go 1 block up,
# school already present
# store and clubhouse unblock below
# If you consider the fifth block tho it has every req except gym in itself 
# one need to traverse a distance of 4 blocks above to get to gym.
# (even if for some case for 5th blockn one need to travel 2 block up thn to 2nd block is prefered
# (as to reach at any req one needs to only travers a distance in range 1 or 0.)

Blocks = [{"gym"       :"true",
           "school"    :"true" ,
           "store"     :"false",
           "clubhouse" :"false"},

          {"gym"       :"false",
           "school"    :"true",
           "store"     :"false",
           "clubhouse" :"false"},

          {"gym"       :"false",
           "school"    :"false",
           "store"     :"true",
           "clubhouse" :"true"},

          {"gym"       :"false",
           "school"    :"true",
           "store"     :"false",
           "clubhouse" :"true"}]


Reqs = ["gym", "school", "store", "clubhouse"]

print()

lengthOfBlocks = len(Blocks)

extraDict = {}
for req in Reqs:
  extraDict[req] = "end"

ascendingBlocks  = []
for i in range(len(Blocks)):
  ascendingBlocks.append(Blocks[i])
ascendingBlocks.append(extraDict)


descendingBlocks = []
while Blocks :
  descendingBlocks.append(Blocks[-1])
  del Blocks[-1]
descendingBlocks.append(extraDict)


def nearestValue(Reqs, Blocks) :
  nearestList = []
  for req in Reqs:
    for blockNo in range(len(Blocks)):
      if Blocks[blockNo][req] == "true":
        nearestList.append(blockNo)
        break
      elif Blocks[blockNo][req] == "end" :
        nearestList.append(lengthOfBlocks + 1)
        break
  return (nearestList)
  

ascendingList = []
for blockNo in range(len(ascendingBlocks)):
  ascendingList.append(nearestValue(Reqs, ascendingBlocks))
  del ascendingBlocks[0]
del ascendingList[-1]

descendingList = []
for blockNo in range(len(descendingBlocks)):
  descendingList.append(nearestValue(Reqs, descendingBlocks))
  del descendingBlocks[0]
del descendingList[-1]

descendingListInverse = []
while descendingList :
  descendingListInverse.append(descendingList[-1])
  del descendingList[-1]

finalNearestValueList = []
for blockNo in range(lengthOfBlocks):
  tempNearBlockList = []
  for nearestCount in range(len(Reqs)):
    if ascendingList[blockNo][nearestCount] <= \
    descendingListInverse[blockNo][nearestCount]:
      tempNearBlockList.append(ascendingList[blockNo][nearestCount])
    else :
      tempNearBlockList.append(descendingListInverse[blockNo][nearestCount])
  finalNearestValueList.append(tempNearBlockList)

neededDict = {}
for steps in range(lengthOfBlocks):
  if len(neededDict) > 0 : break
  else:
    for blockNo in range(len(finalNearestValueList)):
      if all (finalNearestValueList[blockNo][i] in range(0,steps + 1) \
      for i in range(len(Reqs))):
        neededDict[blockNo + 1] = finalNearestValueList[blockNo]

def finalLooping(finalDict, neededDict, i, l):
  for k, v in neededDict.items():
    if v.count(l) == i :
      finalDict[k] = v

finalDict = {}
for l in range(len(neededDict)):
  for i in range(len(Reqs) + 1):
    finalLooping(finalDict, neededDict, i, l)
  if len(finalDict) > 0 :
    break

for key, value in finalDict.items():
  print ("Building No: %d".center(20, "=") % (key))
  for i in range(len(Reqs)):
    print (str(Reqs[i]).ljust(10,"-")  + str(value[i]).rjust(9,"-"))
print()
