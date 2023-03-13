# Created by Saravanan Krishnarajan at 12-03-2023 using PyCharm

# Django
# Module 3 Assignment 1


#1. Build an interactive application which should simulate a Quiz contest. The following
#questions might be asked as input from the user:
#Choose the level (easy, intermediate, and hard): → 3 modes of difficulty and user should
#input one of these choices.
#Please give us the number of questions you want to attempt: → Number of questions
#thrown should be entered through this prompt.
#Specify the question type (multiplication:M, addition:A, subtraction:S, division:D): → One
#of these operations to be performed.
#If the answer is right or wrong, appropriate messages should be printed. Move to the next
#question if the attempt count is not exceeded.
#Hint: Random utility can be used to change the complexity of questions.
#The program should ask if the user wants to continue even after attempting the number
#of questions specified and should loop or terminate.
#Sample:
#Choose the level (easy, intermediate, and hard): easy
#Please give us the number of questions you want to attempt: 3
#Specify the question type (multiplication:M, addition:A, subtraction:S, division:D):D
#What's 6 divided by 3?
#2
#That's right -- well done
#What's 10 divided by 2?
#5
#That's right -- well done
#What's 18 divided by 3?
#6
#That's right -- well done
#Continue or exit (Continue:C, Exit: E): E

import random

# Find the matching operand for  x
def find_operand(x,divider):
    lst = []
    for i in range(1,divider):
        if(x%i == 0):
            lst.append(i)
    return random.choice(lst)

# Set the max numbers based on difficulty
def set_maxs(choice):

    A_max = 0
    B_max = 0
    if choice == "easy":
        A_max=10
        B_max=5
    elif choice == "intermediate":
        A_max=40
        B_max=10
    elif choice == "hard":
        A_max=100
        B_max=20
    return (A_max, B_max)

cont = 'C'
while cont == 'C':

    choice =  input("Choose the level (easy, intermediate, and hard): ")
    number_q = eval(input("Please give us the number of questions you want to attempt: "))
    type_q = input("Specify the question type (multiplication:M, addition:A, subtraction:S, division:D): ")

    op_dict = {'M':'multiplication', 'A':'addition', 'S':'subtraction', 'D':'division'}

    for l in range(number_q):
        num_A = 0
        num_B = 0
        x_max, y_max = set_maxs(choice)

        if type_q in ('M','A','S'):
            num_A = random.choice(range(1,x_max))
            num_B = random.choice(range(1,y_max))
        elif type_q == 'D':
            num_A = random.choice(range(1,x_max))
            num_B =find_operand(num_A,y_max)

        print(f"What is the {op_dict[type_q]} of {num_A} and {num_B}?")
        ans = eval(input("Enter your answer"))

        if type_q=='M' and (num_A*num_B)==ans:
            print("Correct!")
        elif type_q=='A' and (num_A+num_B)==ans:
            print("Correct!")
        elif type_q == 'S' and (num_A - num_B) == ans:
            print("Correct!")
        elif type_q == 'D' and (num_A / num_B) == ans:
            print("Correct!")
        else:
            print("Wrong")

    cont = input("Continue or exit (Continue:C, Exit: E):").upper()


#2. Write a recursive function to compute x raised to the power of n

def recursive(x,n):
    if n==0:
        return 1

    return x*recursive(x,n-1)

print(recursive(5,5))


# 3. Sort the list using lambda function mylist = [["john", 1, "a"], ["larry", 0, "b"]]. Sort the list
# by second item 1 and 0.

mylist = [["john", 1, "a"], ["larry", 0, "b"]]
mylist
mylist.sort(key = lambda x: x[1])
mylist

#4. Sort the list using operator.itemgetter function mylist = [["john", 1, "a"], ["larry", 0, "b"]].
#Sort the list by second item 1 and 0
from operator import itemgetter
mylist = [["john", 1, "a"], ["larry", 0, "b"]]
sorted(mylist,key=itemgetter(1))