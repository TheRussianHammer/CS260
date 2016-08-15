#!/usr/bin/env python

class Node:
	def __init__(self, rank = 0, data = None, parent = None):
		self.rank = rank
		self.data = data
		self.parent = parent

def Initialize( n ):
	result = {}
	for i in n:
		result.update( { i : Node( 0, i ) } )
	return result

def Find(my_set, val):
	parent = my_set[val].parent 
	count = 1
	while parent != None:
		val = parent.data
		parent = parent.parent 
		count += 1
		if count > len(my_set):
			break
	return my_set[val].data

def Merge( my_set, val_1, val_2 ):
	if val_1 == val_2:
		return False

	set_1 = my_set[ Find( my_set, val_1 ) ]
	set_2 = my_set[ Find( my_set, val_2 ) ]

	if set_1.rank == set_2.rank:
		set_2.parent = set_1
		set_1.rank += 1
	elif set_1.rank > set_2.rank:
		set_2.parent = set_1
	else:
		set_1.parent = set_2
				 	
	return True
