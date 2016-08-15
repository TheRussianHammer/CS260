#!/usr/bin/env python
import sys
INF = 99999999

def parseInput( lines ):
	result = {}
	for i in lines:
		num = ""
		nums = []
		weights = []
		isWeight = False
		count = 1
		for s in i:
			if s == " " or count == len(i):
				if not isWeight:
					nums.append(num)
					isWeight = False
				else:
					weights.append(num)
			elif s == ",":
				isWeight = True
			else:
				num += s
		localDict = {}
		for z in range(1,len(nums)):
			localDict.update({int(nums[z]):int(weights[z])})
		result.update({int(nums[0]):localDict})	
	return result
				 

def Floyd(graph):
	nodes = graph.keys()

	distance = {}

	for n in nodes:
		distance[n] = {}

		for k in nodes:
			distance[n][k] = graph[n][k]

	for k in nodes:
		for i in nodes:
			for j in nodes:
				distance[i][j] = min (distance[i][j], \
					distance[i][k] + distance[k][j])
	return distance




if __name__ == '__main__':

	lines = []

	while 1:
		try:
			line = sys.stdin.readline()
			lines.append(line)
		except KeyboardInterrupt:
			break
		if not line:
			break
	print Floyd(parseInput(lines))
