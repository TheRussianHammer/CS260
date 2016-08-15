#!/usr/bin/python
from bNode import bNode
from lexer import *

def generate_parse_tree():
	t = get_next_token()
	stack = []
	while t:
		if str.isdigit( t[0] ) :
			stack.append( bNode( t + " " ) )
		else:
			right = stack.pop() 
			left = stack.pop() 
			stack.append( bNode( t + " ", left, right ) )
		t = get_next_token()

	return stack.pop()

def prefix( T ):
	if T == None:
		return ""
	return T.val + prefix( T.left ) + prefix( T.right )

def infix( T ):
	if T == None:
		return ""
	return infix( T.left ) + T.val + infix( T.right )

def postfix( T ):
	if T == None:
		return ""
	return postfix( T.left ) + postfix( T.right) + T.val

if __name__ == "__main__" :
	while get_expression():
		tree = generate_parse_tree()
		print("pre: " + prefix( tree ) )
		print("in: " + infix( tree ) )
		print("post: " + postfix( tree ) )
		print("eval: " + str(eval(infix( tree ) ) ) )
