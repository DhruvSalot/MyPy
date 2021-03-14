# CU4STORE
# https://www.codechef.com/UNCO2021/problems/CU4STORE

noOfRooms = int(input())

storageCap = ["x"] + [int(i) for i in input().split()] + ["x"]

def nearLessWeigh(roomNo, storageCap):
	i = roomNo - 1
	while True:
		if storageCap[i] == "x":
			return(0)
		elif storageCap[i] < storageCap[roomNo]:
			return(i)
		else :
			i -= 1

ansList = []
for roomNo in range(1, noOfRooms + 1):
	ansList.append(nearLessWeigh(roomNo, storageCap))

print(*ansList)

