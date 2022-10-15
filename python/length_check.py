#To check the lenght of a given input
def hint_username(username):
    if len(username) < 5: #we are checking for the input username lenght.
        print("Invalid username. Name must be at least 5 characher long")
    elif len(username) > 15:
        Print("Invalid username. Name must be at most 15 character long")
    else:
        print("bigo!! username valid")
        print("You just entered a valid user name " + username)
hint_username("Emmanuel")
