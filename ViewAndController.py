"""
MetaGame
An interactive video game! #name files differently

Authors: Cynthia Yong, Sabrina Pereira, Sophie Schaffer
"""
import pygame
import time
from Model import *
from stageobject_mappings import *
#from stageobject_mappings import StartingPage


pygame.init() #add it in the main or write game function that init the pygame


#doesn't need to be here, create dictionary: default settings - refer to it
#Setting the standard sizes for the text boxes and buttons
textFont = pygame.font.SysFont('comicsans', 40)
width = 1200
height = 800
buttonWidth = 300
buttonHeight = 75
buttonY = 550
textBoxWidth = 800
textBoxHeight = 300
textBoxY = 500
textBoxX = (width - textBoxWidth)/2
win = pygame.display.set_mode((width,height))
#the background image for our game - there will eventually be different backgrounds as the player progresses
# currentScreen = Screen()



class TextBox(): #scatter and gather : what does user need at minimum to display textbox; what is actually mandatory: gather optionals into dictionary and call it: dictionary update method
    """
    This is used to display text on the screen.
    Requires textbox dimensions, color, text, location

    """

    def __init__(self, text='', color = (255,222,222)):
        self.color = color
        self.x = 300
        self.y = 150
        self.width = 600
        self.height = 300
        self.text = text

    # the codes below handle how the text is able to stay in the textbox rather than going off
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
        position = self.x + space + 15,self.y + space + 25
        max_width, max_height = self.width+self.x-15,self.height+self.y
        x, y = position
        for line in words:
            for word in line:
                word_surface = font.render(word,0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = position[0]  # Reset the x.
                    y += word_height  # Start on new row.
                for letter in word:
                    letter_surface = font.render(letter, 0, color)
                    letter_width, letter_height = letter_surface.get_size()
                    win.blit(letter_surface,(x, y))
                    x+=letter_width
                    self.typePause(.01)
                x += space
            x = position[0]  # Reset the x.
            y += word_height  # Start on new row.
            self.typePause(.3)

    def typePause(self,pause):
        if type(self) == Button:
            pass
        elif type(self) == TextBox:
            pygame.display.update()
            time.sleep(pause)

    def draw(self,win= win,outline=None):
        """
        This function will draw each button onto the screen
        """
        if outline:
            # pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            win.blit(pygame.transform.scale(pygame.image.load('ButtonOutline.png'),(self.width, self.height)),(self.x, self.y))
        # pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        win.blit(pygame.transform.scale(pygame.image.load('Button.png'),(self.width, self.height)),(self.x, self.y))

        if self.text != '':
            self.textSpacing()

    def __repr__(self):
        """
        This function prints the textbox with self.text
        """
        return self.text

class Button(TextBox):
    """
    This class inherits from the textbox class and displays the buttons onto the screen

    """
    def __init__(self, stage = None, text='',color = (255,222,222),backButton = False):
        super(Button,self).__init__(text,color)
        self.y = 450 # the same
        self.x = 0 # changes
        self.width = 300
        self.height = 175
        self.stage = stage
        self.backButton = backButton

class Screen():
    """
    takes information from Stage and displays everything
    """
    def __init__(self,stage,state):
        self.stage = stage
        self.state = state

    def buttonDecider(self):

        if self.stage.buttonMapping != None:
            screenButtons = []
            for buttonMapping in self.stage.buttonMapping:
                for level in buttonMapping.levels:
                    if level == self.state.level or level == 0:
                        screenButtons.append(Button(buttonMapping.stageMapTo, buttonMapping.buttontext,backButton = buttonMapping.backButton))
            buttonPlacement(screenButtons)
            self.screenButtons = screenButtons
        else:
            self.screenButtons = None

    def textboxDecider(self):
        if self.stage.description.get(self.state.level) == None:
            text = self.stage.description[0]
        else:
            text = self.stage.description[self.state.level]

        if self.state.decisions != None:
            for key in self.state.decisions:
                if str(key) in text:
                    text = text.replace(str(key), str(self.state.decisions[key]))


        self.screenBox = TextBox(text)

    def inventoryDecide(self):
        spacer = 10
        if self.state.inventory != []:
            for picture in self.state.inventory:
                win.blit(pygame.transform.scale(pygame.image.load(picture), (60, 60)), (spacer, 10))
                spacer += 70


    def draw(self):
        self.buttonDecider()
        self.textboxDecider()
        win.blit(pygame.transform.scale(pygame.image.load(self.stage.picture), (width, height)), (0, 0))
        self.inventoryDecide()
        self.screenBox.draw()
        time.sleep(.1)
        if self.screenButtons != None:
            for button in self.screenButtons:
                button.draw()


def buttonPlacement(screenButtons):
    """
    This function evenly places the buttons on the screen
    depending on the number of buttons there are

    """
    #Calculates the amount of space that will not be taken up by buttons
    for item in screenButtons:
        if item.backButton:
            back = item
            screenButtons.remove(item)
            item.y = 50
            item.x = 950
            item.width = 200
            item.height = 150
        else:
            back = None

    totalSpace = width - buttonWidth*len(screenButtons)
    space = totalSpace/(len(screenButtons)+1)

    spacerIndex = space
    #Goes through and adjusts the x-coordinates for each button placement
    for item in screenButtons:
        item.x = spacerIndex
        item.y = buttonY
        spacerIndex += buttonWidth + space
    if back != None:
        screenButtons.append(back)

#To Fix and implement
def drawScreen(stage, state, oldScreen = None): #old screen = none; change dictkey and dictionary
    """
    This function clears the last display and
    puts up a new screen after the user selects an option

    """

    currentScreen = Screen(stage,state)
    currentScreen.draw()

    if currentScreen.screenButtons != None:
        for object in currentScreen.screenButtons:
            object.exist = True

    return currentScreen

    #take out none

    #view class has update
    #active list of items that you can interact with and move things out of it

#################Controller Stuff

def isOver(button,pos):
    if button != None:
    # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > button.x and pos[0] < button.x + button.width:
            if pos[1] > button.y and pos[1] < button.y + button.height:
                return True
        return False

def isClick(button,pos):
    # Will recognize when the user pushes down on the mouse
    if button != None:
        if event.type == pygame.MOUSEBUTTONDOWN: #download pygame in other file
            if isOver(button,pos):
                return True
        else:
            return False

def whatTyping(button):
        if event.type == pygame.KEYDOWN:
            if event.key == 8: #delete
                button.pop()
            else:
                button.append(event.unicode)

def monitor(buttonList,pos):
    if buttonList != None and buttonList != [None]:
        for button in buttonList:
            if isOver(button,pos):
                win.blit(pygame.transform.scale(pygame.image.load('ButtonOutline.png'),(button.width, button.height)),(button.x, button.y))
            else:
                win.blit(pygame.transform.scale(pygame.image.load('ButtonOutlineCover.png'),(button.width, button.height)),(button.x, button.y))


if __name__ == '__main__':


    state = State(level=1)

    currentScreen = Screen(StartingPage, state)

    currentScreen = drawScreen(currentScreen.stage, state)

    while True:
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            pygame.display.update()

            checkStageConditions(currentScreen.stage, currentScreen.state)
            checkInventory(currentScreen.stage,currentScreen.state)


            if currentScreen.screenButtons != None:
                for button in currentScreen.screenButtons:
                    if isClick(button,pos):
                        currentScreen = drawScreen(button.stage, state, currentScreen)

            currentScreen.inventoryDecide()

            monitor(currentScreen.screenButtons,pos)

            if event.type == pygame.QUIT:
               run = False
               pygame.quit()
               quit()

            levelConditions(state,currentScreen.stage)



##end
