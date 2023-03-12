# Created by Saravanan Krishnarajan at 12-03-2023 using PyCharm

# Python Django
# Module 2: Sequences and File Operations
# Assignment 1

# 1. Correct the program given below.

total = int(input('What is the total amount for your online shopping?'))
country = input('Shipping within the US or Canada?')
if country == "US":
    if total <= 50:
        print("Shipping Costs $6.00")
    elif total <= 100:
        print("Shipping Costs $9.00")
    elif total <= 150:
        print("Shipping Costs $12.00")
    else:
        print("FREE")
if country == "Canada":
    if total <= 50:
        print("Shipping Costs $8.00")
    elif total <= 100:
        print("Shipping Costs $12.00")
    elif total <= 150:
        print("Shipping Costs $15.00")
    else:
        print("FREE")


# 2. Write a program that uses input to prompt a user for their name and then welcomes them

# Example:
# Enter your name: Chuck
# Hello Chuck

name =input("Enter your name")
print(f"Hello {name}")

# 3. Write a program which prompts the user for a Fahrenheit temperature, converts the
# temperature to Celsius and prints out the converted temperature.

farenheit = eval(input("Enter temperature in farenheit"))
celsius = (farenheit - 32)*5/9
print(f"temperature in celsius  is {celsius}")


#4. Write a program to prompt the user for hours and rate per hour to compute gross pay.
#Example: Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
hours = eval(input("Enter number of hours"))
rate = eval(input("Enter rate per hour"))
print(f"your pay is {hours*rate}")


# 5. Write a for loop that prints all elements of a list and their position in the list.
# a = [4,7,3,2,5,9]
a = [4,7,3,2,5,9]
for i in range(0,len(a)):
    print(f"{a[i]} is at {i}")

#6. Write a program which should create a dictionary of key:values.
# 'A':1 'B':2 'C':3 . . . . 'Z':26 [Use dictionary comprehension]

cnt = 1
for i in range(65,91):
    print(f"{chr(i)}:{cnt} ",end='')
    cnt+=1

#7. Write a program to reverse/inverse key:value like below.
# dict1 = {'a': 1, 'b':2}
# Expected result: dict2 = {1: 'a', 2: 'b'}
dict1 = {}
for i in range(97,123):
    dict1[chr(i)]=i
dict2 ={}
for key,value in dict1.items():
    dict2[value]=key
print(dict1)
print(dict2)


#8. Using given list L = ['a', 'b', 'c', 'd'] create a dictionary of key:values.
#Expected result {'a': 1, 'c': 3, 'b': 2, 'd': 4} [Hint: Use Enumerate function]

L = ['a', 'b', 'c', 'd']
result = {}
for i in range(len(L)):
    result[L[i]]=i

print(result)

# 9. Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range,
# print an error. If the score is between 0.0 and 1.0, print a grade using the following table:

class InvalidScoreValue(Exception):
    pass

value = eval(input("Enter value between 0.0 and 1.0"))

try:
    if value >= 0.0 and value <=1.0:
        if value>=0.9:
            print("A")
        elif value>=0.8:
            print("B")
        elif value>=0.7:
            print("C")
        elif value>=0.6:
            print("D")
        else:
            print("FAIL")
    else:
        raise InvalidScoreValue
except InvalidScoreValue:
    print("Bad score")