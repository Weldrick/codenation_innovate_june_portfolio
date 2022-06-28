#This is now pytyon levelUP
#casting = changing user input from string to int
#int()
#float()
#str()

#converting data types
#print(int(5.6)) #always round down to the nearest whole number
#print(type(int("54"))) #prints type of data NOT THE DATA
#print(int("Seven")) #cannot convert string "seven" to int
#print(int(round(5.6))) #rounds to the nearest whole number

#Cash machine
# balance = 100
# deposit = int(input("How much do you want to deposit")) #wont work without casting
# balance += deposit
# print(f"Your new balance is {balance}")

#TRUTHY AND FALSY
#falsy values are:
#emptyString ""
#integer value 0
#floating value point 0.0
#everything else is TRUTHY

# print("What is your name?")
# name = input() #input can be on a second name

# if name:
#     print(f"Welcome to the jungle {name}")

#print (not True)
#print(not False)

# allowed = ["bot1", "bot2", "bot3", "bot4", "bot5"]
# name = input("What is your name?")
# while name not in allowed: ##in is own keyword

#     print("Sorry! you are not on the list")
#     name = input("What is your name?")
# print("Come on in")


# print("What coat is always wet when you put it on?")
# answer = input("Please type answer")

# if "Paint" in answer:
#     print("Correct answer")
#     ##problem would also accept shed and paint

#TRY & Except
#E.G
# def AddUp():
#     num1 = (input("Enter 1st number \n"))
#     num2 = (input("Enter 2nd number \n"))

#     try:
#         print(int(num1) + int(num2))
#     except:
#         print("Please use whole numbers only")
#         AddUp() #gives the user another chance
# AddUp()
#there are no erros even though the function is concantinating strings
#NOT adding two integers

#self recursive functions