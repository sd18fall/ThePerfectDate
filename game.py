"""
MetaGame
An interactive video game!

Authors: Cynthia Yong, Sabrina Pereira, Sophie Schaffer
"""
import pygame

pygame.init()



#Setting the standard sizes for the text boxes and buttons
textFont = pygame.font.SysFont('comicsans', 30)
width = 800
height = 600
buttonWidth = 200
buttonHeight = 100
buttonY = 400
textBoxWidth = 400
textBoxHeight = 200
textBoxY = 125
textBoxX = (width - textBoxWidth)/2
win = pygame.display.set_mode((width,height))
pic = pygame.image.load("Creepy.jpg") #the background image for our game - there will eventually be different backgrounds as the player progresses




class TextBox():
    """
    This is used to display text on the screen.
    Requires textbox dimensions, color, text, location

    """

    def __init__(self, color, x=textBoxX,y=textBoxY,width=textBoxWidth,height = textBoxHeight, text='', exist = False):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.exist = exist

    def textSpacing(self, font = textFont, color=(0,0,0)):
        """
        Method able to adjust the lines of text to fit in text box.
        """
        words = [word.split(' ') for word in self.text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        pos = self.x + space ,self.y + space
        max_width, max_height = self.width+self.x,self.height+self.y
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                win.blit(word_surface,(x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

        # if self.text != '':
        #     #Set font and size of button text, display centered
        #     font = textFont
        #     text = font.render(self.text, 1, (0,0,0))
        #     win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

        if self.text != '':
            self.textSpacing()



    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text

class Button(TextBox):
    """
    This class inherits from the textbox class to display the buttons and
    allow user interactivity

    """

    def __init__(self, color, x=0,y=buttonY,width=buttonWidth,height=buttonHeight, text='', exist = False):
        # super().__init__(color, x) # we eventually want to use this method instead of writing everything out
        self.color = color
        self.y = buttonY
        self.width = buttonWidth
        self.height = buttonHeight
        self.exist = exist
        self.text = text

    def isOver(self,pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
            return False

    def isClick(self,pos):
        # Will recognize when the user pushes down on the mouse
        if self.exist:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.isOver(pos):
                    return True
            else:
                return False

class BackButton(Button):
    """
    This button allows the user to go back to the previous page
    It has it's own class because it remains static in the corner and
    doesn't need positioning

    """
    def __init__(self, color, x=625,y= 25,width=150,height=100, text='', exist = False):
        # super().__init__(color, x)
        self.color = color
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        self.exist = exist
        self.text = text



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


class Room():
    """
    Stores the information for room

    * Not currently in use
    """
    def __init__(self, name, picture):
        self.name = name
        self.picture = picture

class Artifact():
    """
    Stores information about the items that the user interacts with to help them

    * Not currently in use
    """
    def __init__(self, location, name, description, picture):
        self.name = name
        self.description = description
        self.picture = picture

def Quitting():
    """
    Enables user to click to exit the game
    """
    if event.type == pygame.QUIT:
       run = False
       pygame.quit()
       quit()

def newScreen(dictkey,dictionary,oldScreen = []):
    """
    This function clears the last display and
    puts up a new screen after the user selects an option

    """
    win.blit(pygame.transform.scale(pic, (width, height)), (0, 0)) #photo background for screens
    for item in oldScreen:
        item.exist = False # eliminates the buttons in the previous screen
    newItems = dictionary[dictkey] # gathers values (textboxes & buttons) based on dictionary key
    buttonList = []
    for item in newItems:
        if type(item) == Button:
            buttonList.append(item) # putting the buttons into a separate list
    buttonPlacement(buttonList) # spaces the buttons evenly on the screen
    for item in newItems: #draws the textboxes and buttons
        item.draw(win,(0,0,0))
        item.exist = True
    return newItems

def isAnythingClick(screenButtons,dictionary):
    """
    This function detects if any of the buttons are clicked,
    if a button is clicked, then it will return a new screen

    """
    for item in screenButtons:
        if type(item) == Button or type(item) == BackButton:
            if item.isOver(pos):
                item.draw(win,(255,0,0)) #Red outline if hovering over button
            else:
                item.draw(win,(0,0,0)) #Black outline in normal state
            if item.isClick(pos):
                newButtons = newScreen(item,dictionary,screenButtons)
                return newButtons
    return screenButtons #if nothing is clicked, the screen stays the same

def buttonPlacement(screenButtons):
    """
    This function evenly places the buttons on the screen
    depending on the number of buttons there are

    """
    #Calculates the amount of space that will not be taken up by buttons
    totalSpace = width - buttonWidth*len(screenButtons)
    space = totalSpace/(len(screenButtons)+1)

    spacerIndex = space
    #Goes through and adjusts the x-coordinates for each button placement
    for item in screenButtons:
        item.x = spacerIndex
        item.y = buttonY
        spacerIndex += buttonWidth + space




"""
Here we created the text boxes and buttons that we will display on the screen, and add them to dictionaries in order to establish a mapping for the buttons.
"""
StartDescription = TextBox((255,255,255), text='You wake up in a bathroom and are confused. You do not know where you are')
Start = Button((255,255,255))
StartBack = BackButton((255,255,255), text='Back to Start')

BedroomDescription = TextBox((255,255,255), text='The room is messy and the lights are dim. Did something move in the corner')
Bedroom = Button((255,255,255), text='Go towards the bedroom')

Diary = Button((255,255,255), text='Open up her diary')
DiaryDescription = TextBox((255,255,255), text='The diary appears to be locked, but it feels nice to hold')
DiaryBack = BackButton((255,255,255), text='Go back to exploring the bedroom')

Pillow = Button((255,255,255), text='Scream into the pillow on the bed')
PillowDescription = TextBox((255,255,255), text='The pillow is old and flat')
PillowBack = BackButton((255,255,255), text='Go back to exploring the bedroom')

Kitchen = Button((255,255,255), text='Go towards the weird smelling kitchen')
KitchenDescription = TextBox((255,255,255), text='The kitchen smells weird, just like you expected. There are dirty dishes everywhere')

Fork = Button((255,255,255), text='Use a fork as a weapon')
ForkDescription = TextBox((255,255,255), text='The fork is oddly sharp and you stare at your reflection. You hold it close to your face and then slowly put it back down')
ForkBack = BackButton((255,255,255), text='Go back to exploring the kitchen')

Fridge = Button((255,255,255), text='Put head in fridge, look around')
FridgeDescription = TextBox((255,255,255), text='There is mold everywhere. Uh oh you touched some mold')
FridgeBack = BackButton((255,255,255), text='Go back to exploring the kitchen')


StartRoom = [StartDescription, Bedroom, Kitchen]
KitchenRoom = [StartBack, KitchenDescription,Fork,Fridge]
BedroomRoom = [StartBack, BedroomDescription,Pillow,Diary]

"""
Screens is our initial dictionary with key and buttons/ textboxes as the values
"""

Screens = {Start : StartRoom, Bedroom : BedroomRoom, Kitchen : KitchenRoom, Pillow : [PillowDescription, PillowBack], Diary : [DiaryDescription, DiaryBack], Fork : [ForkDescription, ForkBack], Fridge : [FridgeDescription,FridgeBack], StartBack : StartRoom, ForkBack : KitchenRoom , FridgeBack : KitchenRoom, DiaryBack:BedroomRoom,PillowBack: BedroomRoom}



if __name__ == '__main__':

##    FOR TESTING PURPOSES
#     newScreen(item,screen)
#
    # a = TextBox((255,255,255), text='AAAAAAAA AAAAAAA AAAAAAAA AAAAAA')


#     b = Button((255,255,255), text='B')
#     d = Button((255,255,255), text='D')
#     c = Button((255,255,255), text='C')
#
#     ItemDictionary = {a : [b,c], b: [c,d],c : [d,a], d: [a,b]}
#
#     newScreen(d,ItemDictionary)
#     oldScreen = ItemDictionary[d]


    newScreen(Start, Screens)
    oldScreen = Screens[Start]
    while True:
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            pygame.display.update()


            Quitting()

            oldScreen = isAnythingClick(oldScreen,Screens)







##end
