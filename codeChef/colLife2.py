noOfSsn = int(input())

introTime = [int(i) for i in input().split()]

noOfEpAndEptime = []
for season in range(noOfSsn):
	noOfEpAndEptime.append([int(i) for i in input().split()])

timeWatched = 0
for season in range(noOfSsn):
	for episode in range(1, len(noOfEpAndEptime[season])):
		if episode == 1:
			timeWatched += noOfEpAndEptime[season][episode]
		else : timeWatched += noOfEpAndEptime[season][episode] - introTime[season]
print(timeWatched)

