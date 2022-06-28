#Variables can be any data type including other variables

from random import randint, random


myName = "Mark" #string
myAge = 36 #integer
employed = True #boolean

#name
#print ("Hello my name is", myName) = 
print (f"Hello my name is {myName}")

#age
#print ("I am " + myAge) #doesnt work for int
print (f"I am {myAge} years old") #preferred format (f strings)

#employed
print (f"I am employed = {employed}")

##all variables on 1 string
print (f"Hello my name is {myName}, I am {myAge} years old, and I am employed = {employed}")

#ARITHMETIC OPERATORS

number1 = randint(0, 10)
number2 = randint(0, 10)

value = random

print (f"number1 = {number1}")
print (f"number2 = {number2}")
print (number1 + number2)

currentBalance = 100
value = 0
newBalance = currentBalance + value
print (newBalance)