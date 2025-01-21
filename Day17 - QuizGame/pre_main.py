"""Creating my very first class"""
class User:
    #here the details of the Class (blueprint)
    pass

#for now the class is empty, but we can anyway use it...
user_1 = User()

#Now, to add attributes, we can use the new object (user_1) to make them exist
user_1.id = '001'
user_1.username = 'luis'
#etc...
"""
But isnt that too manual and prone to error?
We better use a Constructor! or to intialize the objects from the Class...
this function is the INIT function! 
"""

class Perro:
    def __init__(self):
        #inside here we put the starting values of the Class to new Objects
        #This init function will be called everytime the Class is called
        print('perrito is being created')
        #Attributes are the things that the Class will have \ hold

class Cat:
    def __init__(self, meows):   #here you prepare to receive the parameters and data
        self.meows = meows  #once received, you can use it to set the objects attribute

gatito = Cat(5)  #in here, gatito.meows  = 5
#so now we do not need to set all attributes manually..!

class Player:
    def __init__(self, health, attack, defense):     #here only things that will ALWAYS be needed
        self.health = 0
        self.attack = 0
        self.defense = 0   #convention is that the name of the parameter == name of the attribute
        self.critical = 0   #not all attributes will be mandatory from the beginning

player_lvl1 = Player(10, 5, 4)
#Now its muck quicker
enemy_lvl1 = Player(15,7,1)
#Danger of this, now all Objects created from this class NEED the attributes to be added..!

#Methods!
class User:
    #Attributes:
    def __init__(self, user):
        self.followers = 0
        self.following = 0
        self.user = user

    def follow(self, user):
        user.followers += 1
        self.following += 1