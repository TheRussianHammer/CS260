#!/usr/bin/python
from cell import Cell

def list_concat_copy( A, B ):
	result = Cell(A.data)
	p = A.next
	current = result
	while p != None:
		current.next = Cell(p.data)
		p = p.next
	
	current.next = B
	p = B.next
	while p != None:
		current.next = Cell(p.data)
		p = p.next

	return result

