"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""

number = input()

n1 = int('%s'%number)
print(n1)
n2 = int('%s%s'%(number,number))
print(n2)
n3= int('%s%s%s'%(number,number,number))
print(n3)
n4= int('%s%s%s%s'%(number,number,number,number))
print(n4)

print(n1+n2+n3+n4)

"""

9
99
999
9999
11106

"""
