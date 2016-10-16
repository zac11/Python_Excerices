"""

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

"""

input_string = input()
dict_d ={'LOWECASE':0,'UPPERCASE':0}

for items in input_string:
    if items.isupper():
        dict_d['UPPERCASE']+=1
    elif items.islower():
        dict_d['LOWECASE']+=1
    else:
        pass

print('Lower case is ',dict_d['LOWECASE'])
print('Upper case is ',dict_d['UPPERCASE'])

"""
Harambe is not dead. He is always in our hearts
Lower case is  35
Upper case is  2

"""