PYTHON = python
VIEWER = less

.PHONY: clean run view

problem1: problem1.py

problem2: problem2.py

problem3: problem3.py

run : problem1 problem2 problem3 view 

view : problem1.py problem2.py problem3.py cell.py
	- $(VIEWER) problem1.py
	- $(VIEWER) problem2.py
	- $(VIEWER) problem3.py


clean :
	- \rm $(outFile) > /dev/null 2>&1
	- \rm *.pyc > /dev/null 2>&1
