import re
import operator

# Question 18
# Level 3
#
# Question:
# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and check them
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
def password_check():
    passwords = input("Enter comma separated passwords:").split(",")
    verified_pass = [password for password in passwords if
                     re.match("(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[$#@])(?=.{8,16})", password)]
    print("The verified passwords are:" + ",".join(verified_pass))


# Question 19
# Level 3
#
# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
def sort_attributes():
    print("Enter people data in format 'name,age,score':")
    persons = []
    while True:
        person = input()
        if not person:
            break
        elif re.match("\w+,\d+,\d+", person):
            persons.append(tuple(person.split(",")))
        else:
            print("Please check format")
    print(sorted(persons, key=operator.itemgetter(0, 1, 2)))


# Question 20
# Level 3
#
# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
#
# Hints:
# Consider use yield
class YieldTest:

    def __init__(self):
        self.n = None

    def numbers_generator(self, n):
        self.n = n
        for i in range(0,n):
            if i % 7 == 0:
                yield i

    def print_numbers(self, n=20):
        generator = self.numbers_generator(n)
        for i in generator:
            print(i)


# Question 21
# Level 3
#
# Question:
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
#
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2
def robot():
    print("Enter movement instruction in format 'direction(UP/DOWN/LEFT/RIGHT) distance(xx)':")

    position = {'x': 0, 'y': 0}

    while True:
        instruction = input()
        if re.match(r'(?i)^(UP|DOWN|LEFT|RIGHT)\s\d+$', instruction):
            instruction = instruction.split(" ")
            mov, direction = instruction[0].upper(), int(instruction[1])
            if mov == 'UP':
                position['y'] += direction
            elif mov == 'DOWN':
                position['y'] -= direction
            elif mov == 'LEFT':
                position['x'] -= direction
            elif mov == 'RIGHT':
                position['x'] += direction
        elif not instruction:
            break
        else:
            print("Please enter correct format")
    print("The distance from starting position is " + str(round((position['x'] ** 2 + position['y'] ** 2) ** 0.5)))


# Question 22
# Level 3
#
# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
def frequency_of_words():
    words = input("Enter a sentence:").split(" ")
    words.sort()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    keys = sorted(frequency.keys())
    for key in keys:
        print("{}:{}".format(key, frequency[key]))

# MAIN FUNCTION
if __name__ == "__main__":
    frequency_of_words()
