"""
MetaGame
An interactive video game! #name files differently

Authors: Cynthia Yong, Sabrina Pereira, Sophie Schaffer
"""
import pygame
import time
from Model import *
from stageobject_mappings import *
# from stageobject_mappings import StartingPage

pygame.init() # Included at top such that we can generate fonts with pygame
pygame.mixer.init()
textFont = pygame.font.SysFont('comicsans', 40) #Setting the standard sizes for the text boxes and buttons

# Initializing screen size
screenWidth = 1200
screenHeight = 800
win = pygame.display.set_mode((screenWidth,screenHeight))


# =========================================================================================
#                                VIEWER CODE
# =========================================================================================

class TextBox():
    """
    Used to display text on the screen. Size and placement of text boxes are set.

    text: String to be displayed as text on screen. Will be taken from description of a stage object.

    color: Hex code that corresponds to color textbox should be. Default is a pink (255,222,222) used throughout our game.

    x, y, width, height: In pixels. Pre-set.

    """

    def __init__(self, text='', color = (255,222,222)):
        self.text = text
        self.color = color
        self.x = 300
        self.y = 150
        self.width = 600
        self.height = 300

    """The methods below handle how the text is able to stay in the textbox rather than running off the page."""
    # ASK SOPHIEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEe
    #
    def append(self,text):
        """
        Method that adds text to the preexisting text
        """
        self.text += text

    def pop(self):
        """
        Method that removes the last letter of the text
        """
        self.text = self.text[0:len(self.text)-1]

    def textSpacing(self, font = textFont, color=(0,0,0)):
        """
        Method able to adjust the lines of text to fit in text box.

        font: the font th text should be written in
        Color: the color of the text
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
            self.typePause(.01)

    def typePause(self,pause):
        """
        Allows small pause between putting letters on screen to simulate typing effect.
        """
        if type(self) == Button:
            pass
        elif type(self) == TextBox:
            pygame.display.update()
            time.sleep(pause)

    def draw(self,win= win,outline=None):
        """
        This function will draw each button onto the screen.
        """
        # ASK SOPHIEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEeeeeeee
        if self.text != '' or type(self) == Button:

            win.blit(pygame.transform.scale(pygame.image.load('Button.png'),(self.width, self.height)),(self.x, self.y))

            self.textSpacing()

    def __repr__(self):
        """
        This function prints the textbox with self.text
        """
        return self.text

class Button(TextBox):
    """
    This class inherits from the textbox class, used to display interactive buttons on screen.
    Size is set, placement of text boxes must be

    text: String to be displayed as text on screen. Will be taken from description of a stage object.

    color: Hex code that corresponds to color textbox should be. Default is a pink (255,222,222) used throughout our game.

    x, y, width, height: In pixels. Pre-set.

    backButton: Indicates whether the Button object will be a backButton or not.

    responseButton: Indicates whether the Button object will be a responseButton or not.(a button that can be typed in but not clicked)
    """
    def __init__(self, stage = None, text='',color = (255,222,222),backButton = False,responseButton = False):
        super(Button,self).__init__(text,color)
        self.y = 450 # stays the same
        self.x = 0 # changes
        self.width = 300
        self.height = 175
        self.stage = stage
        self.backButton = backButton
        self.responseButton = responseButton

class Screen():
    """
    This class takes information from a stage and state, then turns the information from these into textboxes,
    buttons and the background to be displayed.

    stage: Current Stage object that should be represented graphically on screen.

    state: State object that influences what will be shown on the screen.

    """
    def __init__(self,stage,state):
        self.stage = stage
        self.state = state

    def buttonPlacement(self, screenButtons, buttonWidth = 300, buttonY = 550):
        """
        This function evenly places the buttons onto the screen
        depending on the number of buttons in the screenButtons list.
        """

        # Removes backButton from screenButton list and sets specific position for the backButton to be displayed
        for button in screenButtons:
            if button.backButton:
                back = button
                screenButtons.remove(button)
                button.y = 50
                button.x = 950
                button.width = 200
                button.height = 150
            else:
                back = None

        # Calculates the amount of space that will not be taken up by buttons
        totalSpace = screenWidth - buttonWidth*len(screenButtons)
        space = totalSpace/(len(screenButtons)+1)

        # Adjusts the x-coordinates for each button placement
        spacerIndex = space

        for button in screenButtons:
            button.x = spacerIndex
            button.y = buttonY
            spacerIndex += buttonWidth + space
        if back != None:
            screenButtons.append(back)

    def buttonDecider(self):
        """
        This function checks the level the user is on and generates a list of buttons (screenButtons)
        that goes on the screen.
        """
        if self.stage.buttonMapping != None:
            screenButtons = []
            for buttonMapping in self.stage.buttonMapping:
                for level in buttonMapping.levels:
                    if level == self.state.level or level == 0:
                            screenButtons.append(Button(buttonMapping.stageMapTo, buttonMapping.buttontext,backButton = buttonMapping.backButton,responseButton = buttonMapping.responseButton))
            self.buttonPlacement(screenButtons)
            self.screenButtons = screenButtons
        else:
            self.screenButtons = None

    def textboxDecider(self):
        """
        This function checks the level the user is currently on and creates a TextBox object
        with the correct text description. It searches through the text description
        and replaces the state.decisions key with the value.
        """
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
        """
        This function takes the pictures in the state.inventory list and displays them on
        the top left hand corner of the screen after the user has selected an option.
        """
        spacer = 10
        if self.state.inventory != []:
            for picture in self.state.inventory:
                win.blit(pygame.transform.scale(pygame.image.load(picture), (60, 60)), (spacer, 10))
                spacer += 70


    def draw(self):
        """
        This function draws the entire screen complete with text, buttons, and background.
        """
        self.buttonDecider()
        self.textboxDecider()
        win.blit(pygame.transform.scale(pygame.image.load(self.stage.picture), (screenWidth, screenHeight)), (0, 0))
        self.inventoryDecide()
        self.screenBox.draw()
        time.sleep(.1)
        if self.screenButtons != None:
            for button in self.screenButtons:
                button.draw()

def nextScreen(stage, state, oldScreen = None):
    """
    This function clears the last screen and uses the draw function in Screen class
    to generate the new screen.
    """
    currentScreen = Screen(stage,state)
    currentScreen.draw()

    return currentScreen


# =========================================================================================
#                                CONTROLLER CODE
# =========================================================================================

def isOver(button,pos):
    """
    This function determines if the user mouse is over a button.
    """
    if button != None:
    # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > button.x and pos[0] < button.x + button.width:
            if pos[1] > button.y and pos[1] < button.y + button.height:
                return True
        return False

def isClick(button,pos):
    """
    This function will recognize when the user pushes down on the mouse.
    """
    if button != None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if isOver(button,pos):
                return True
        else:
            return False

def whatTyping(button,stage):
    """
    This function detects if the user is typing and appends the button description and stage name to match what is being typed.
    """
    if event.type == pygame.KEYDOWN:
        if event.key == 8: #delete
            button.pop()
        else:
            button.append(event.unicode)
        stage.name = button.text

def enter():
    """
    This function checks if a key was pressed and if it was enter, and if it was it returns true
    """
    if event.type == pygame.KEYDOWN:
        if event.key == 13:
            return True

def monitor(buttonList,stage,pos):
    """
    This function will generate a white outline when the user hovers the mouse over a button and update the text on a button if it is a response button
    """
    if buttonList != None and buttonList != [None]: #ASK SOPHIE
        for button in buttonList:
            if button.responseButton:
                whatTyping(button,stage)
                button.draw()
            elif isOver(button,pos):
                win.blit(pygame.transform.scale(pygame.image.load('ButtonOutline.png'),(button.width, button.height)),(button.x, button.y))
            else:
                win.blit(pygame.transform.scale(pygame.image.load('ButtonOutlineCover.png'),(button.width, button.height)),(button.x, button.y))

def playMusic(song):
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(-1)
# =========================================================================================
#                                RUNNING THE GAME
# =========================================================================================

if __name__ == '__main__':

    # Indicates what level to start at. Level 1 will start at the beginning.
    state = State(level=4)

    playMusic(state.music)

    # Initializes starting screen
    currentScreen = Screen(Name, state)
    currentScreen = nextScreen(currentScreen.stage, state)

    while True:
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            pygame.display.update()

            # Runs through various functions to check conditions
            checkStageConditions(currentScreen.stage, currentScreen.state)

            if state.level == 3:
                levelConditions(state,currentScreen.stage)
                if state.level == 4:
                    pygame.mixer.Channel(3).play(pygame.mixer.Sound('crash.aiff'))
                    playMusic(state.music)

            if currentScreen.stage == NotOver:
                playMusic('happy.mp3')

            if currentScreen.stage == TryAgain:
                playMusic('happy.mp3')

            levelConditions(state,currentScreen.stage)

            checkInventory(currentScreen.stage,currentScreen.state)



            currentScreen.inventoryDecide()
            monitor(currentScreen.screenButtons,currentScreen.stage,pos)

            # Check to see if a button is clicked, show the next approprate screen
            if currentScreen.screenButtons != None:
                for button in currentScreen.screenButtons:
                    if button.responseButton:
                        if enter():
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('click.wav'))
                            time.sleep(.19)
                            currentScreen = nextScreen(button.stage, state, currentScreen)
                    elif isClick(button,pos):
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('click.wav'))
                        time.sleep(.19)
                        currentScreen = nextScreen(button.stage, state, currentScreen)

            if event.type == pygame.QUIT:
               run = False
               pygame.quit()
               quit()



##end
