# Created by Saravanan Krishnarajan at 12-03-2023 using PyCharm

# Python Django
# Python Django Module 1 Case study 1

#1. Write a program to print the:
#a. Number of lowercase “a” and “o” in the following sentence
#b. Number of uppercase “L” and “N” in the following sentence
#‘Discover, Learning, with, Edureka’

sentence = "Discover, Learning, with, Edureka"

#ao_counts=sentence.count('a')+sentence.count('o')
#LN_counts=sentence.count('L')+sentence.count('N')
#for character in sentence:
#    if(character =='a' or character=='o'):
#        ao_counts+=1
#    elif(character=='L' or character=='N'):
#        LN_counts+=1
#    print(character)
#
print(f"count of characters a and o in sentence is: {ao_counts}")
print(f"count of characters L and N in sentence is: {LN_counts}")

#2. Write a program to remove the following from:
#www.edureka.in

name= "www.edureka.in"
# a. Remove all w’s before and after .edureka.
print(name.replace('www','').replace('in',''))

# b. Remove all lowercase letter before and after .edureka.
first_index = name.index('.')
last_index = name.index('.',first_index+1)
new_name=""
print(first_index,last_index)
index =0
for i in name:
    #print(i, end='')
    if i.islower() and (index<first_index or index>last_index):
        pass
    else:
        print(i, end='')
    index+=1

# c. Remove all printable characters

for i in name:
    if ord(i)<32 and ord(i)>160:
        print(ord(i),'',sep=',',end='')