"""

Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

"""

input_string = input()
dict_d ={'DIGITS':0,'LETTERS':0}

for items in input_string:
    if items.isdigit():
        dict_d['DIGITS']+=1
    elif items.isalpha():
        dict_d['LETTERS']+=1
    else:
        pass

print('LETTERS are ',dict_d['LETTERS'])
print('DIGITS are ', dict_d['DIGITS'])


"""

Harambe is dead. Please shout 12#4

Output is :
LETTERS are  24
DIGITS are  3

"""


