#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. Block a Friend")
    print("4. View all my friends")
    print("5. View all my messages")
    print("6. <- Go back ")
    return input("Please Choose a number: ")


#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True:        

        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()

            current_user = None
            user_choice = input("Enter the username of the account you want to manage:")

            for user in ai_social_network.list_of_people:
                if user.id == user_choice:
                    current_user = user 

            if inner_menu_choice == "1": 
                current_user.edit_details() 
                    
            elif inner_menu_choice == "2":
                new_friend = input("Username of new friend: ")
                for friend in ai_social_network.list_of_people:
                    if friend.id == new_friend:
                        new_friend = friend 
                
                current_user.add_friend(new_friend) 
            
            elif inner_menu_choice == "3":
                blocked_friend = input("Username of friend to block: ")
                for blocked in ai_social_network.list_of_people:
                    if blocked.id == blocked_friend:
                        blocked_friend = blocked 
                current_user.block_friend(blocked_friend)
                    
                
            elif inner_menu_choice == "4":
                current_user.view_friends() 
            
            elif inner_menu_choice == "5":
                current_user.view_messages() 
                option = input("if you would like to send a message press y")
                if option == "y":
                    current_user.send_message()


                
                while True:
                    if inner_menu_choice == "6":
                        break
                    else:
                        inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()


