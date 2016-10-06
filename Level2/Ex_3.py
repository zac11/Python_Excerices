"""

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence
after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

"""
enter_string = input()

items = [x for x in enter_string.split(',')]

items.sort()

print(','.join(items))


"""
Input : lionel, christiano, diego, aguero
Output : aguero, christiano, diego,lionel

"""