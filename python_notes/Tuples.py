#global and local variables
#to reference a variable within a function variable needs to be global
# light = False

# def LightSwitch():
#     global light #global reference needed so function can access/modify it
#     if light:
#         print("Light is on")
#         light = False #pyton makes a new variable instead of referencing the global variable

#     else:
#         print("Light is off")
#         light = True

# LightSwitch()
# LightSwitch()

#LIST VS TUPLE
#both are a collection of values
#list can be changed tuple cannot

# evenNumbers = [2, 4, 6, 8, 10] #list
# #list can be changed

# oddNumbers = (1, 3, 5, 7, 9) #tuple
# print(f"even numbers list = {evenNumbers}")
# print(f"odd numbers tuple = {oddNumbers}")
# #tuple cannot be changed
# evenNumbers.append(12)
# evenNumbers.insert(0, 0) # enables us to place a new item at a specific index number
# #
# print(evenNumbers)

#Slice notation
#start - stop - step

# evenNumbers = [2, 4, 6, 8, 10]
# print (evenNumbers[1]) #index position of list
# print (evenNumbers[1:5:1]) #starts at 1 - stops at 2 - steps at 1

# pallondrome = "hannah"
# if pallondrome == pallondrome[::-1]: #slice notation
#     print(f"Yes {pallondrome} is a palindrome")
# else:
#     print("no")

#WHILE LOOPS

# loopRun = True
# while loopRun == True:
#     print("Run forever")
#     loopRun = False

#from random import randint


# num = randint(1, 51)

# while num%2 == 0:
#     print(f"{num} = Even")

# print(f"{num} = Odd")

while True:
    num=randint(1, 51)
    print(num)
    if num % 2 == 0:
        print("We like even numbers")
        continue
    else:
        print("An odd number")
        break