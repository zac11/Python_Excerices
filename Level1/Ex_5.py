"""

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

"""

class InputOutString(object):
    def __init__(self):
        self.s=''

    def getString(self):
        self.s=input()


    def printString(self):
        print(self.s.upper())


strObj = InputOutString()
strObj.getString()
strObj.printString()

"""
Output :

lionel messi is god
LIONEL MESSI IS GOD

"""