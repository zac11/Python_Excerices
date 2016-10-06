"""

Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a
comma separated sequence.

Example:
0100,0011,1010,1001
Then the output should be:
1010
"""
string_val =input()
val =[]

items =[x for x in string_val.split(',')]

for p in items:
    div5 = int(p,2)    #converts the binary to a decimal
    if not div5%5:
        val.append(p)


print(','.join(val))