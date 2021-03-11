# DEFEAT
# https://www.codechef.com/UNCO2021/problems/DEFEAT

NMK = [int(i) for i  in input().split()]

matrix = []
for column in range(NMK[1]):
	matrix.append([0]* NMK[0])

enemyLoc = []
for enemy in range(NMK[2]):
	enemyLoc.append([i for i in input().split()])

for enemy in range(NMK[2]):
	for enemyRow in enemyLoc[enemy][0]:
		for enemyCol in enemyLoc[enemy][1]:
			matrix[int(enemyRow)-1][int(enemyCol)-1] += 1

def noOfenemies(rowNo, colNo, matrix):
	rowEnemy = 0
	for col in range(len(matrix)):
		rowEnemy += matrix[rowNo][col]

	colEnemy = 0
	for row in range(len(matrix[0])):
		colEnemy += matrix[row][colNo]
	
	if matrix[rowNo][colNo] == 1 :
		return(rowEnemy + colEnemy - 1)
	else :
		return(rowEnemy + colEnemy)

totalEnemy = []
for r in range(len(matrix)):
	for c in range(len(matrix[0])):
		totalEnemy.append(noOfenemies(r, c, matrix))

totalEnemy.sort()
print(totalEnemy[-1])





