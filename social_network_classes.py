# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        

    def  create_account(self):
        new_account = input("Insert your username:" )
        if new_account in self.list_of_people: 
            print("This username is not available")
        else:
            age = int(input("Insert your age:"))
            self.list_of_people.append(new_account)
        print("Creating ...")
        pass


class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []

    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        pass

    def send_message(self):
        #implement sending message to friend here
        pass
