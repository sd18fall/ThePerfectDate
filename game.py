"""
MetaGame
An interactive video cd ~
game!

Authors: Cynthia Yong, Sabrina Pereira, Sophie Schaffer
"""
import pygame
from Data_Storage import*

pygame.init()



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
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        self.exist = exist
        self.text = text



class State():
    """stores all the information of what has already happened"""
    def __init__(self, level, inventory, location):
        self.level = level
        self.inventory = inventory
        self.location = location

    def __str__(self):
        return "Level: " + str(self.level)+", Inventory: "+ str(self.inventory) + ", Location: "+str(self.location)


class Room():
    """needs to accept name, picture, artifacts"""
    def __init__(self, name, picture, artifacts):
        self.name = name
        self.picture = picture
        self.artifacts = artifacts

class Artifact():
    """needs to accept name, description, picture"""
    def __init__(self, location, name, description, picture):
        self.name = name
        self.description = description
        self.picture = picture

def Quitting():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
           pygame.quit()
           quit()

def newScreen(dictkey,oldScreen = []):
    """clears last display and puts up what should currently be on the screen"""
    win.blit(pygame.transform.scale(pic, (width, height)), (0, 0))
    for item in oldScreen:
        item.exist = False
    newItems = Screens[dictkey]
    buttonList = []
    for item in newItems:
        if type(item) == Button:
            buttonList.append(item)
    buttonPlacement(buttonList)
    for item in newItems:
        item.draw(win,(0,0,0))
        item.exist = True
    return newItems

def isAnythingClick(screenButtons):
    for item in screenButtons:
        if type(item) == Button:
            if item.isClick(pos):
                newButtons = newScreen(item,screenButtons)
                return newButtons
            else:
                return screenButtons

def buttonPlacement(screenButtons):
    totalSpace = width - buttonWidth*len(screenButtons)
    space = totalSpace/(len(screenButtons)+1)

    spacerIndex = space
    for item in screenButtons:
        item.x = spacerIndex
        item.y = buttonY
        spacerIndex += buttonWidth + space


StartDescription = TextBox((255,255,255), text='You wake up and are confused')
Start = Button((255,255,255), text='Get up from the bed',exist = False)
StartBack = BackButton((255,255,255), text='Go Back to Start',exist = False)


BedroomDescription = TextBox((255,255,255), text='The room is very messy and smells funky')
Bedroom = Button((255,255,255), text='Explore the room')

Diary = Button((255,255,255), text='Open up her Diary',exist = False)
DiaryDescription = TextBox((255,255,255), text='The diary appears to be locked.')
DiaryBack = BackButton((255,255,255), text='Diary - Back',exist = False)

Pillow = Button((255,255,255), text='Scream into a pillow',exist = False)
PillowDescription = TextBox((255,255,255), text='The pillow is old and flat',exist = False)
PillowBack = BackButton((255,255,255), text='Pillow - Back',exist = False)

Kitchen = Button((255,255,255), text='Kitchen',exist = False)
KitchenDescription = TextBox((255,255,255), text='The kitchen smells weird',exist = False)

Fork = Button((255,255,255), text='Use the fork as a weapon',exist = False)
ForkDescription = TextBox((255,255,255), text='The fork is oddly sharp',exist = False)
ForkBack = BackButton((255,255,255), text='Fork - Back',exist = False)

Fridge = Button((255,255,255), text='Stick your head in the fridge',exist = False)
FridgeDescription = TextBox((255,255,255), text='There is mold everywhere',exist = False)
FridgeBack = BackButton((255,255,255), text='Fridge - Back',exist = False)



Screens = {Start : [StartDescription, Bedroom, Kitchen], Bedroom : [StartBack, BedroomDescription,Pillow,Diary], Kitchen : [StartBack, KitchenDescription,Fork,Fridge],Pillow : [PillowDescription, PillowBack], Diary : [DiaryDescription, DiaryBack], Fork : [ForkDescription, ForkBack], Fridge : [FridgeDescription,FridgeBack], StartBack : [Kitchen,Bedroom], ForkBack : [Fridge,Fork,StartBack],FridgeBack : [Fridge,Fork,StartBack], DiaryBack: [Pillow,Diary,StartBack],PillowBack: [Pillow,Diary,StartBack]}



if __name__ == '__main__':

##TESTING newScreen(item,screen)
    #
    # a = Button((255,255,255),100,buttonY,buttonWidth,buttonHeight, text='A',exist = False)
    # #b = Button((255,255,255),200,buttonY,buttonWidth,buttonHeight, text='B',exist = False)
    # a = Button((255,255,255), text='A',exist = False)
    # b = Button((255,255,255), text='B',exist = False)
    # d = Button((255,255,255), text='D',exist = False)
    # c = TextBox((255,255,255), text='C')
    #
    # ItemDictionary = {a : [b,a,c,d], b: [a]}
    #
    #
    # newScreen(b)
    # oldScreen = [a]

    # win.blit(pygame.transform.scale(pic, (width, height)), (0, 0))
    newScreen(Start)
    oldScreen = Screens[Start]
    while True:
        pygame.display.update()
        # win.blit(pygame.transform.scale(pic, (width, height)), (0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            pygame.display.update()

            oldScreen = isAnythingClick(oldScreen)







    ##end
