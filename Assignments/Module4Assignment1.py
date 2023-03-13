# Created by Saravanan Krishnarajan at 13-03-2023 using PyCharm

# Django Assignment
# Module 4 Assignment 1

import re
#1. Write a Regular Expression that will match a date that follows the following standard
#“YYYY-MM-DD.”
print(re.match("[0-9]{4}(-)[0-9]{2}(-)[0-9]{2}","2023-03-13").group())
print(re.match("\d{4}(-)\d{2}(-)\d{2}","2023-03-13").group())

# 2. Write a Regular Expression that will match a traditional SSN.
print(re.match("[0-9]{8}(-)[0-9]{4}","20230313-1212"))
print(re.match("[0-9]{8}(-)[0-9]{4}","2023031A-1212"))

# 3. Write a Regular Expression that will match an IPv4 address
print(re.match("[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}","192.168.1.2"))
print(re.match("[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}","192.16*.1.2"))

# 4. Write a Regular Expression that will match an email address.
print(re.match("[a-zA-Z0-9._]{1,40}@[a-zA-Z0-9.-]{1,50}.[a-zA-Z0-9._]{2,10}","test.test@gmail.com").group())
print(re.match("[a-zA-Z0-9._]{1,40}@[a-zA-Z0-9.-]{1,50}.[a-zA-Z0-9._]{2,10}","test@gmail.com").group())

#5. Below is the program to calculate the area of a box. Check how it is working. Correct the
#program (if required).
class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


#Create an instance of Box.
x = Box(10, 2)
print(x.area())



# 6. Write a program to calculate distance so that it takes two Points (x1, y1) and (x2, y2) as
# arguments and displays the calculated distance using Class.

import math
def find_distance(x1,y1,x2,y2):
    dist = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
    return dist

x1,y1 = 4,2
x2,y2 = 7,5
print(f"distance between x1,y1 and x2,y2 is: {find_distance(x1, y1, x2, y2)}")


#7. Correct the below program so that the output should appear like this.
#• [Expected output: x-value: 5 y-value: 7]

Program:

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "x-value: " + str(self.x) + " y-value: " + str(self.y)
    def __add__(self,other):
        p = Point()
        p.x = self.x+other.x
        p.y = self.y+other.y
        return p

p1 = Point(3,4)
p2 = Point(2,3)
print(p1.__add__(p2))