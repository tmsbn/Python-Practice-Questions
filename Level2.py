import math
from ast import literal_eval


# Question 7
# Level 2
#
# Question:
# Write a program which takes 2 digits, X,Y as input and generates
# a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
def matrix():
    x, y = literal_eval(input("Enter two comma separated values:"))
    ans = [[x * y for y in range(0, y)] for x in range(0, x)]
    print(ans)


# Question 6:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
def formula():
    C, H = 50, 30
    d = literal_eval(input("Enter comma separated sequence:"))
    q = [round(math.sqrt((2 * (C * D) / H))) for D in d]
    print(q)


# Question 8
# Level 2
#
# Question:
# Write a program that accepts a comma separated sequence of words as
# input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
def sort_words():
    print(",".join(sorted(input("Enter a bunch of comma separated words:").split(","))))


# Level 2
#
# Question:
# Write a program that accepts sequence of lines as input and prints the lines after
# making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
def capitalize_lines():
    lines = []
    s = " "
    print("Enter a bunch of lines:\n")
    while s:
        s = input()
        if s:
            lines.append(s)
    print("\n".join(lines))


# Question 11
# Level 2
#
# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as
# its input and then check whether they are divisible by 5 or not. The numbers that are
# divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
def check_divisibility():
    binary = input("Enter comma separated binary numbers:").split(sep=",")
    div_numbers = [x for x in binary if int(x, 2) % 5 == 0]
    print(",".join(div_numbers))

if __name__ == "__main__":
    check_divisibility()
