"""

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

"""

str_input = input()
dimensions = [int(x) for x in str_input.split(',')]
rowNum = dimensions[0]
columnNum = dimensions[1]

multilist = [[0 for col in range(columnNum)] for row in range(rowNum)]

"""
This creates a 4X6 dimensional array of 0's

0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

"""

print(multilist)


for row in range(rowNum):
    for col in range(columnNum):
        multilist[row][col]= row*col

print(multilist)

"""

------------------Row 1----------------------

for row in range(0):
	for col in range(6):
			multilist[0][0]= 1*0 = 0

for row in range(0):
	for col in range(6):
			multilist[0][1]= 0*1 = 0


for row in range(0):
	for col in range(6):
			multilist[0][2]= 0*2 = 0


for row in range(0):
	for col in range(6):
			multilist[0][3]= 0*3 = 0


for row in range(0):
	for col in range(6):
			multilist[0][4]= 0*4 = 0


for row in range(0):
	for col in range(6):
			multilist[0][5]= 0*5 = 0


for row in range(0):
	for col in range(6):
			multilist[0][6]= 0*6 = 0

------------------Row 2-------------------------

for row in range(1):
	for col in range(6):
			multilist[1][0]= 1*0 = 0

for row in range(1):
	for col in range(6):
			multilist[1][1]= 1*1 = 1


for row in range(1):
	for col in range(6):
			multilist[1][2]= 1*2 = 2


for row in range(1):
	for col in range(6):
			multilist[1][3]= 1*3 = 3



for row in range(1):
	for col in range(6):
			multilist[1][4]= 1*4 = 4


for row in range(1):
	for col in range(6):
			multilist[1][5]= 1*5 = 5


for row in range(1):
	for col in range(6):
			multilist[1][6]= 1*6 = 6


------------------Row 3---------------------------

for row in range(2):
	for col in range(6):
			multilist[2][0]= 2*0 = 0


for row in range(2):
	for col in range(6):
			multilist[2][1]= 2*1 = 2


for row in range(2):
	for col in range(6):
			multilist[2][2]= 2*2 = 4


for row in range(2):
	for col in range(6):
			multilist[2][3]= 2*3 = 6


for row in range(2):
	for col in range(6):
			multilist[2][4]= 2*4 = 8


for row in range(2):
	for col in range(6):
			multilist[2][5]= 2*5 = 10


for row in range(2):
	for col in range(6):
			multilist[2][6]= 2*6 = 12




------------------Row 4---------------------------------

for row in range(3):
	for col in range(6):
			multilist[3][0]= 3*0 = 0


for row in range(3):
	for col in range(6):
			multilist[3][1]= 3*1 = 3


for row in range(3):
	for col in range(6):
			multilist[3][2]= 3*2 = 6


for row in range(3):
	for col in range(6):
			multilist[3][3]= 3*3 = 9


for row in range(3):
	for col in range(6):
			multilist[3][4]= 3*4 = 12


for row in range(3):
	for col in range(6):
			multilist[3][5]= 3*5 = 15

"""