# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        

    def create_account(self):
        print("Creating ...")
        name = input("Insert your username:" )
        age = (input("Insert your age:"))
        created_account = Person (name,age)
        self.list_of_people.append(created_account)

       
    

class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.messages = []

    def edit_details(self):
        new_age =(input("Insert your new age:"))
        new_name = input("Insert your new username:" )
        self.id = new_name 
        self.year = new_age 

    def add_friend(self, person_object):
        self.friendlist.append(person_object)

    def block_friend(self, person_object):
        self.friendlist.remove(person_object)
    
    def view_friends(self):
        for people in self.friendlist:
            print(people.id)

    def send_message(self, message, name_of_friend, social_network):
        friend_object = input("name of friend you want to send message to:")
        message = input("write your message to your friend")


        #implement sending message to friend here
        #find friend's object by looping through list_of_people list in social network class
        #add message to friend's messgaes_list
        #friend_object.messages.append(message)
        pass
