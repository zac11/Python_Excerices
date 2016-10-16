"""
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The
transaction log format is shown as following:
D 100
W 200
¡­
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""

import sys
netAccountAmount=0
while True:
    entry =input()
    if not entry:
        break
    values = entry.split(',')
    op = values[0]
    newAmount = int(values[1])
    if op =='D':
        netAccountAmount+=newAmount
    elif op =='W':
        netAccountAmount-=newAmount
    else:
        pass

print(netAccountAmount)
