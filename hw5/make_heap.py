#!/usr/bin/env python

def left(H, i):
	result = (i+1)*2
	if result > len(H):
		return None
	return result - 1

def right(H, i):
	result = (i+1)*2
	if result >= len(H):
		return None
	return result

def parent(H, i):
	if i == 1:
		return None
	result = int((i+1)/2)
	return result - 1

def swap(H, nodeA, nodeB):
	temp = H[nodeA]
	H[nodeA] = H[nodeB]
	H[nodeB] = temp 

def last_in_node(H):
	return len(H)//2 - 1

def down_heap(H, i):
	if H == None:
		return False
	child = left(H, i)
	if child == None:
		return True
	r = right(H, i)
	if r != None and H[r] > H[child]:
		child = r
	if H[i] > H[child]:
		return None
	swap(H, i, child)
	down_heap(H, child)
	
def make_heap(H):
	node = last_in_node(H)
	for i in range(node + 1):
		down_heap(H, node - i)

if __name__ == "__main__":
	import random
	import timeit

	print("n\tT(n)")
	for i in range(1,7):
		n = 10 ** i
		x = [random.randint(0,1000) for i in xrange(n)]
		time = timeit.Timer('make_heap(x)', 'from __main__ import make_heap,x')
		delta = time.timeit(1)
		print str(n) + "\t" + str(delta)
