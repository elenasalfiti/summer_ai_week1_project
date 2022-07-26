# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. Block a Friend")
    print("4. View all my friends")
    print("5. Send a message")
    print("6. View all my messages")
    print("7. <- Go back ")
    return input("Please Choose a number: ")