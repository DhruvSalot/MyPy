# ZUBSPOIL
# https://www.codechef.com/problems/ZUBSPOIL

def valueOfArray(listOfInt):
	value = 0
	for i in range(len(listOfInt)-1): 
		value += abs(listOfInt[i]-listOfInt[i+1])    
	return(value)

def repList(listToRep, repWhat):
	return ([repWhat[1] if l == repWhat[0] else l for l in listToRep])
    
testCase = input()

line2 = [int(i) for i in input().split()]

array = [int(i) for i in input().split()]

testList = []
for noOfTest in range(line2[1]):
	testList.append([int(i) for i in input().split()])

print ("Case: " + testCase)

for k in range(len(testList)):
	print(valueOfArray(repList(array, testList[k])))
	array = repList(array, testList[k])