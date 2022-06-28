message = "Welcome to Code Nation" #variable that holds the text codenation
#messageLength = len(message) %2 #variable that checks if message can be divided by 2

def CheckLength(message):
    print(message)

    messageLength = len(message) %2
    print(messageLength)

    if messageLength == 0:

        print("Message is even")

    else:
        print("Message = odd")

CheckLength("Welcome to codenation")