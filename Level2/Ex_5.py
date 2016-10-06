"""

Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all
duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

"""

string_input = input()
words =[word for word in string_input.split(" ")]
print(" ".join(sorted(list(set(words)))))


"""
Let's break it down now


print(set(words))


This will print a set of the words, with all the unique values

print(list(set(words)))


Create a list out of the values of words

print(sorted(list(set(words))))


This will sort the list

print(" ".join(sorted(list(set(words)))))


This is join the sorted list items with a whitespace


For this input :

I like to yawn and I also like to make a music and a car

Now output will be :

I a also and car like make music to yawn

Notice that the uppercase I is sorted at first position
"""

