"""
MetaGame
An interactive video cd ~
game!

Authors: Cynthia Yong, Sabrina Pereira, Sophie Schaffer
"""
import pygame

class State():
    """
    Stores all the information of what has already happened

    * Not currently in use
    """
    def __init__(self, level, inventory, location):
        self.level = level
        self.inventory = inventory
        self.location = location

    def __str__(self):
        return "Level: " + str(self.level)+", Inventory: "+ str(self.inventory) + ", Location: "+str(self.location)




#map of entire space, and update
class Room(): #screen? has information about what to do next
    """
    Stores the information for room

    * Not currently in use
    """
    def __init__(self, name, description, picture, artifacts):
        self.name = name
        self.picture = picture
        self.description = description
        self.artifacts = artifacts




class Artifact():
    """
    Stores information about the items that the user interacts with to help them

    * Not currently in use
    """
    def __init__(self, name, description, picture):
        self.name = name
        self.description = description
        self.picture = picture
        # self.choices = choices #TO implement




#button color default, what is minimum you need to make story work, need: rooms with text and buttons to other screens
"""
Here we created the text boxes and buttons that we will display on the screen, and add them to dictionaries in order to establish a mapping for the buttons.
"""
StartDescription = TextBox(text='You wake up in a bathroom and are confused. You do not know where you are')
Start = Button()
StartBack = BackButton(text='Back to Start')

BedroomDescription = TextBox(text='The room is messy and the lights are dim. Did something move in the corner')
Bedroom = Button(text='Go towards the bedroom')

Diary = Button(text='Open up her diary')
DiaryDescription = TextBox(text='The diary appears to be locked, but it feels nice to hold')
DiaryBack = BackButton(text='Go back to exploring the bedroom')

Pillow = Button(text='Scream into the pillow on the bed')
PillowDescription = TextBox(text='The pillow is old and flat')
PillowBack = BackButton(text='Go back to exploring the bedroom')

Kitchen = Button(text='Go towards the weird smelling kitchen')
KitchenDescription = TextBox(text='The kitchen smells weird, just like you expected. There are dirty dishes everywhere')

Fork = Button(text='Use a fork as a weapon')
ForkDescription = TextBox(text='The fork is oddly sharp and you stare at your reflection. You hold it close to your face and then slowly put it back down')
ForkBack = BackButton(text='Go back to exploring the kitchen')

Fridge = Button(text='Put head in fridge, look around')
FridgeDescription = TextBox(text='There is mold everywhere. Uh oh you touched some mold')
FridgeBack = BackButton(text='Go back to exploring the kitchen')


StartRoom = [StartDescription, Bedroom, Kitchen]
KitchenRoom = [StartBack, KitchenDescription,Fork,Fridge]
BedroomRoom = [StartBack, BedroomDescription,Pillow,Diary]

"""
Screens is our initial dictionary with key and buttons/ textboxes as the values
"""

Screens = {Start : StartRoom, Bedroom : BedroomRoom, Kitchen : KitchenRoom, Pillow : [PillowDescription, PillowBack], Diary : [DiaryDescription, DiaryBack], Fork : [ForkDescription, ForkBack], Fridge : [FridgeDescription,FridgeBack], StartBack : StartRoom, ForkBack : KitchenRoom , FridgeBack : KitchenRoom, DiaryBack:BedroomRoom,PillowBack: BedroomRoom}




# class Room():
#     """needs to accept name, picture, """
#     def __init__(self, name = "room", picture = "picture"):
#         self.name = name
#         self.picture = picture
#     def __str__(self):
#         return self.name
#     def __repr__(self):
#         return self.name
#
# class Artifact():
#     """needs to accept name, description, picture"""
#     def __init__(self, location="location", name="name", description="description", picture="picture"):
#         self.location = location
#         self.name = name
#         self.description = description
#         self.picture = picture
#     def __str__(self):
#         return self.name
#     def __repr__(self):
#         return self.name
#
# Room1 = Room()
# A1R1 = Artifact()
# A2R1 = Artifact()
# A3R1 = Artifact()
#
# RoomScreens = { Room1 : [A1R1, A2R1, A3R1]
# }
#
# print(RoomScreens[Room1])
