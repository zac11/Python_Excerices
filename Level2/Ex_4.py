"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

"""
lines =[]
input_string = input()
while True:
    if input_string:
        lines.append(input_string.upper())
    else:
        break

for sent in lines:
    print(sent)

