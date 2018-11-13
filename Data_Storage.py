"""
MetaGame
An interactive video cd ~
game!

Authors: Cynthia Yong, Sabrina Pereira, Sophie Schaffer
"""
import pygame


#Setting the standars sizes for the text boxes and buttons
width = 800
height = 600
buttonWidth = 200
buttonHeight = 100
buttonY = 400
textBoxWidth = 400
textBoxHeight = 200
textBoxY = 100
textBoxX = (width - textBoxWidth)/2
win = pygame.display.set_mode((width,height))
pic = pygame.image.load("Creepy.jpg")


class TextBox():
    """needs to accept dimensions, color, text, location """

    def __init__(self, color, x=textBoxX,y=textBoxY,width=textBoxWidth,height = textBoxHeight, text='', exist = False):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.exist = exist

    def draw(self,win,outline=None):
        #Call tButtonshis method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            #Set font and size of button text, display centered
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text

class Button(TextBox):
    """Child to text box,
    on screen and where it leads"""

    def __init__(self, color, x=0,y=buttonY,width=buttonWidth,height=buttonHeight, text='', exist = False):
        # super().__init__(color, x)
        self.color = color
        self.y = buttonY
        self.width = buttonWidth
        self.height = buttonHeight
        self.exist = exist
        self.text = text

    def isOver(self,pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
            return False

    def isClick(self,pos):
        if self.exist:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.isOver(pos):
                    return True
            else:
                return False

class BackButton(Button):
    def __init__(self, color, x=600,y=50,width=150,height=100, text='', exist = False):
        # super().__init__(color, x)
        self.color = color
        self.y = buttonY
        self.width = buttonWidth
        self.height = buttonHeight
        self.exist = exist
        self.text = text

    pass


class State():
    """stores all the information of what has already happened"""
    def __init__(self, level, inventory, location):
        self.level = level
        self.inventory = inventory
        self.location = location

    def __str__(self):
        return "Level: " + str(self.level)+", Inventory: "+ str(self.inventory) + ", Location: "+str(self.location)


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
