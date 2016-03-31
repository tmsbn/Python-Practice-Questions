import math, re
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
    print("Enter a bunch of lines")
    while s:
        s = input()
        if s:
            lines.append(s.upper())
    print("\n".join(lines))


# Question 11
# Level 2
#
# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as
# its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
def check_divisibility():
    binary = input("Enter comma separated binary numbers:").split(sep=",")
    div_numbers = [x for x in binary if int(x, 2) % 5 == 0]
    print(",".join(div_numbers))


# Question 10
# Level 2
#
# Question:
# Write a program that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
def remove_duplicate():
    print(" ".join(sorted(set(input("Enter a sentence:").split(" ")))))


# Question 12
# Level 2
#
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such
# that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
def even_digits():
    even_digit = [str(number) for number in range(1000, 3001) if all([int(digit) % 2 == 0 for digit in str(number)])]
    print(",".join(even_digit))


# Question 13
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
def letter_digit_count():
    sentence = input("Enter a sentence of digits and numbers:");
    count = {'letter':0 , 'number':0}
    for letter in sentence:
        if letter.isalpha():
            count['letter'] += 1
        elif letter.isdigit():
            count['number'] += 1
    print("LETTERS:" + str(count['letter']) + "\nNUMBERS:" + str(count['number']))


# Question 14
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
def case_count():
    sentence = input("Enter a sentence of digits and numbers:");
    count = {'upper': 0, 'lower': 0}
    for letter in sentence:
        if letter.isupper():
            count['upper'] += 1
        elif letter.islower():
            count['lower'] += 1
    print("UPPER:" + str(count['upper']) + "\nLOWER:" + str(count['lower']))


# Question 15
# Level 2
#
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
def cumulative_addition():
    n, a = literal_eval(input("Enter n,a ?: "))
    ans = 0
    for i in range(1, n+1):
        ans += (int((((10 ** i) - 1)/9)) * a)
    print(ans)


# Question 16
# Level 2
#
# Question:
# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,9,25,49,81

def square_numbers():
    numbers = literal_eval(input("Enter comma separated list of numbers:"))
    print(",".join([str(n*n) for n in numbers if n % 2 == 1]))


# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
def bank():

    balance = 0
    print("Enter transaction in format - transaction(D/W) amount(100):")
    while True:

        transaction = input()
        if not transaction:
            break
        else:

            if re.match("^[DdWw]\s\d+$", transaction):
                flow, amount = transaction.split(" ")
                if flow.upper() == 'D':
                    balance += int(amount)
                elif flow.upper() == 'W':
                    balance -= int(amount)
            else:
                print("Please enter the correct format")
                continue
    print("The final amount is {}".format(balance))


if __name__ == "__main__":
    bank()
