users = {"test":9}

class User:
    
    def __init__(self, name, count):
        self.name = name
        self.count = count
        
    def add():
        count += 1
        
    def subtract():
        count -= 1
        
    def reset():
        count = 0


def ask_name():
    name = input("enter name:")
    if name in users:
        print(users[name])
        User(name, users[name])
    else:
        users[name] = 0
        
ask_name()
        



    #asks the user for name:
    #look for the name on the database
    #gets the number associated with the name
    #continues counting game
