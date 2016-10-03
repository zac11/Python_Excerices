"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""

def factorial(x):
    if x==0:
        return 1
    return x*factorial(x-1)


x=int(input())
print(factorial(x))



"""
Output :

8
=8*7*6*5*4*3*2*1 = 40320

10
=10*9*8*7*6*5*4*3*2*1 = 3628800
"""