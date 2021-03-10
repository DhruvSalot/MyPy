# PANIC
noOfTest = int(input())

for testNum in range(noOfTest):
	KadN = [int(i) for i in input().split()]
	matrix = []
	for column in range(KadN[0]):
		matrix.append([int(i) for i in input().split()])

	def fibonacci(f):
		fibs = [0, 1]
		for loopTime in range(2, f + 1):
			fibs.append(fibs[-1] + fibs[-2])
		return(fibs[f])

	def multiplyingNum(i):
		return(KadN[1] + i * KadN[2])


	def matricesMulti(X,Y):
		result = []
		for resultOrder in range(KadN[0]):
			result.append([0] * KadN[0])
		for t in range(len(X)):
			for u in range(len(Y[0])):
				for v in range(len(Y)):
					result[t][u] += X[t][v] * Y[v][u]
		return(result)

	def M(i):
		if i == 0:
			M = []
			for matrixOrder in range(KadN[0]):
				M.append([0]*matrixOrder + [1] + [0]*(KadN[0]-1-matrixOrder))
			return(M)
		else :
			X = matrix.copy()
			Y = matrix.copy()
			for index in range(i-1):
				X = matricesMulti(X,Y)
			return(X)

	def numAndMat(num, matrix):
		return ([[elem*num for elem in row] for row in matrix])

	def addMat(A,B):
		return ([[A[row][col] + B[row][col] for col in range(KadN[0])] for row in range(KadN[0])])

	finalMatrix = numAndMat(fibonacci(multiplyingNum(0)), M(0))
	for N in range(KadN[3]):
		finalMatrix = addMat(finalMatrix, numAndMat(fibonacci(multiplyingNum(N+1)),M(N+1)))

	# Taking modulo of elements in finalMatrix by 998,244,353
	ansMatrix = [[j % 998244353 for j in finalMatrix[i]] for i in range(len(finalMatrix))]

	#Pretty Printing
	print ()
	print ("Test Number: %d".center(len(str(ansMatrix[0][0])),"=") % (testNum + 1))
	for i in range(len(ansMatrix)):
		print(*ansMatrix[i])
	print ()