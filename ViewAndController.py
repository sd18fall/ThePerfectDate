"""
MetaGame
An interactive video game! #name files differently

Authors: Cynthia Yong, Sabrina Pereira, Sophie Schaffer
"""
import pygame
import time
from Model import *


pygame.init() #add it in the main or write game function that init the pygame


#doesn't need to be here, create dictionary: default settings - refer to it
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
# currentScreen = Screen()



class TextBox(): #scatter and gather : what does user need at minimum to display textbox; what is actually mandatory: gather optionals into dictionary and call it: dictionary update method
    """
    This is used to display text on the screen.
    Requires textbox dimensions, color, text, location

    """

    def __init__(self, text='', exist = False, color = (255,255,255)):
        self.color = color
        self.x = 200
        self.y = 125
        self.width = 400
        self.height = 200
        self.text = text
        self.exist = exist

    def append(self,text):
        self.text += text

    def pop(self):
        self.text = self.text[0:len(self.text)-1]

    def textSpacing(self, font = textFont, color=(0,0,0)):
        """
        Method able to adjust the lines of text to fit in text box.
        """
        words = [word.split(' ') for word in self.text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        position = self.x + space ,self.y + space
        max_width, max_height = self.width+self.x,self.height+self.y
        x, y = position
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = position[0]  # Reset the x.
                    y += word_height  # Start on new row.
                for letter in word:
                    letter_surface = font.render(letter, 0, color)
                    letter_width, letter_height = letter_surface.get_size()
                    win.blit(letter_surface,(x, y))
                    x+=letter_width
                    self.typePause(.05)
                x += space
            x = position[0]  # Reset the x.
            y += word_height  # Start on new row.
            self.typePause(.5)

    def typePause(self,pause):
        if type(self) == Button:
            pass
        elif type(self) == BackButton:
            pass
        elif type(self) == TextBox:
            pygame.display.update()
            time.sleep(pause)

    def draw(self,win= win,outline=None): #each button is responsible for drawing itself
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

    def __repr__(self): #print textbox with self.text
        return self.text

class Button(TextBox):
    """
    This class inherits from the textbox class to display the buttons and
    allow user interactivity

    """

    def __init__(self, stage = None, text='', exist = False, color = (255,255,255)):
        # super(Button,self).__init__(**kw)
        self.color = color
        self.text = text
        self.exist = exist
        self.y = 400
        self.x = 0
        self.width = 200
        self.height = 100
        self.stage = stage



class BackButton(Button):
    """
    This button allows the user to go back to the previous page
    It has it's own class because it remains static in the corner and
    doesn't need positioning

    """
    def __init__(self,stage= None, text='', exist = False, color = (255,255,255)):   #**kw):
        #super(BackButton,self).__init__(**kw)#, text, exist, color)
        #shouldn't have optional arguments, just call button with fixed position
        self.color = color
        self.text = text
        self.exist = exist
        self.y = 25
        self.x = 625
        self.width = 150
        self.height = 100
        self.stage = stage
        # self.exist = exist
        # self.text = text


class Screen():
    """
    takes information from Stage and displays everything
    """
    def __init__(self,stage,state):
        self.stage = stage
        self.state = state
        self.screenBox = TextBox(self.stage.description)

    def buttonDecider(self):
        if self.stage.buttonmapping != None:
            screenButtons = []
            for mappingObj in self.stage.buttonmapping:
                screenButtons.append(Button(mappingObj.stageMapTo, mappingObj.buttontext))

            buttonPlacement(screenButtons)
            self.screenButtons = screenButtons
        else:
            self.screenButtons = None

        if self.stage.backbuttonmapping != None:
            self.backButton = BackButton(self.stage.backbuttonmapping.stageMapTo, self.stage.backbuttonmapping.buttontext)

        else:
            self.backButton = None

    def draw(self):
        self.buttonDecider()
        win.blit(pygame.transform.scale(pygame.image.load(self.stage.picture), (width, height)), (0, 0))
        self.screenBox.draw()
        time.sleep(.1)
        if self.screenButtons != None:
            for button in self.screenButtons:
                button.draw()
        if self.backButton != None:
            self.backButton.draw()


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

#To Fix and implement
def drawScreen(stage, state, oldScreen = None): #old screen = none; change dictkey and dictionary
    """
    This function clears the last display and
    puts up a new screen after the user selects an option

    """
    if oldScreen != None and oldScreen.screenButtons != None:
        for object in oldScreen.screenButtons:
            object.exist = False
    if oldScreen != None and oldScreen.backButton != None:
        oldScreen.backButton.exist = False

    currentScreen = Screen(stage,state)
    currentScreen.draw()

    if currentScreen.screenButtons != None:
        for object in currentScreen.screenButtons:
            object.exist = True
    if currentScreen.backButton != None:
        currentScreen.backButton.exist = True

    return currentScreen

    # currentScreen.draw()






    # newItems = dictionary[dictkey] # gathers values (textboxes & buttons) based on dictionary key
    # buttonList = []
    # for item in newItems:
    #     if type(item) == Button:
    #         buttonList.append(item) # putting the buttons into a separate list
    # buttonPlacement(buttonList) # spaces the buttons evenly on the screen
    # for item in newItems: #draws the textboxes and buttons
    #     item.draw(win,(0,0,0))
    #     item.exist = True
    # return newItems







#################Controller Stuff

def isOver(button,pos):
    # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > button.x and pos[0] < button.x + button.width:
            if pos[1] > button.y and pos[1] < button.y + button.height:
                return True
        return False

def isClick(button,pos):
    # Will recognize when the user pushes down on the mouse
    if button != None and button.exist:
        if event.type == pygame.MOUSEBUTTONDOWN: #download pygame in other file
            if isOver(button,pos):
                return True
        else:
            return False

# def ifButtonClicked():


# def isAnythingClick(screenButtons,dictionary):
#     """
#     This function detects if any of the buttons are clicked,
#     if a button is clicked, then it will return a new screen
#
#     """
#     for item in screenButtons:
#         if type(item) == Button or type(item) == BackButton:
#             if item.isOver(pos):
#                 item.draw(win,(255,0,0)) #Red outline if hovering over button
#             else:
#                 item.draw(win,(0,0,0)) #Black outline in normal state
#             if item.isClick(pos):
#                 newButtons = newScreen(item,dictionary,screenButtons)
#                 return newButtons
#     return screenButtons #if nothing is clicked, the screen stays the same




if __name__ == '__main__':


    Diary = Stage('Diary', 'Her diary', 'Creepy.jpg')

    DiaryObject = MappingObject(Diary, 'Check out the Diary')

    Bedroom = Stage('Bedroom', 'The room is messy and the lights are dim.', 'Creepy.jpg', [DiaryObject])

    diarybackbutton = MappingObject(Bedroom, 'back')

    Diary.backbuttonmapping = diarybackbutton

    state = None
    currentScreen = Screen(Diary, state)

    currentScreen = drawScreen(currentScreen.stage, state)

    while True:
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            pygame.display.update()


            if currentScreen.screenButtons != None:
                for button in currentScreen.screenButtons:
                    if isClick(button,pos):
                        currentScreen = drawScreen(button.stage, state, currentScreen)

            if isClick(currentScreen.backButton,pos):
                currentScreen = drawScreen(currentScreen.backButton.stage, state, currentScreen)


            if event.type == pygame.QUIT:
               run = False
               pygame.quit()
               quit()







            # oldScreen = isAnythingClick(oldScreen,Screens)







##end
