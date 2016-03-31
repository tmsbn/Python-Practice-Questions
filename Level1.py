# Question 2
# Level 1
#
# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


# Question 3
# Level 1
#
# Question:
# With a given integral number n, write a program to generate a dictionary
# that contains (i, i*i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Consider use dict()


def dictionary(n):

    dict = {}
    for i in range(1,n+1):
        dict[i] = i*i
    print(dict)


# Question 4
# Level 1
#
# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple


def list_tuple():
    numbers = input("Enter a set of comma separated numbers:")
    num = numbers.split(",")
    print(num)
    print(tuple(num))


# Question 1
# Level 1
#
# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# Consider use range(#begin, #end) method


def divisibility():

    num = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            num.append(str(i))
    print(",".join(num))


# Question 5
# Level 1
#
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class InputTest:

    def __init__(self):
        self.text = ""

    def get_string(self):
        self.text = input("Enter a string:")

    def print_string(self):
        print(self.text.upper())

# MAIN function

if __name__ == "__main__":
    a = InputTest()
    a.get_string()
    a.print_string()
