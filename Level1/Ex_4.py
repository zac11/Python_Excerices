"""

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

"""


raw_values = (input())

l = raw_values.split(',')

t= tuple(l)

print(t)

print(l)

"""
Output :

34,22,33,44,44,55,66,33,65,78
('34', '22', '33', '44', '44', '55', '66', '33', '65', '78')
['34', '22', '33', '44', '44', '55', '66', '33', '65', '78']


"""