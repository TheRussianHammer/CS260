#!/usr/bin/python
from cell import Cell

def list_concat( A, B ):
	#Concats two lists without a copy
	result = A
	p = A
	while p.next != None:
		p = p.next
	p.next = B
	return result	
