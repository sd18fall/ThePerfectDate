"""
MetaGame: Model Code

This part of the code contains the classes that
provide the major information for the other two documents.

Authors: Cynthia Yong, Sabrina Pereira, Sophie Schaffer
"""
import pygame
import time
pygame.init()
pygame.mixer.init()

class State():
    """
    Stores the information of what has already happened, so the game will
    know when to move forward in the game.

    level: Keeps track of the level the user is on to advance the game.

    decisions: Decisions are made when the user chooses certain answers when prompted.
    Their answer will be stored as a string in a dictionary in this class. The dictionary is also
    used to replace certain words in the displayed text with the user's choices.

    inventory: Stores the .png files for the icons related to the options the user selects.

    """
    def __init__(self, level, decisions = None, inventory = None,music = 'happy.mp3'):
        self.level = level

        if decisions == None:
            self.decisions = {}

        if inventory == None:
            self.inventory = []

        self.music = music

    def __str__(self):
        return "Level: " + str(self.level)+", Inventory: "+ str(self.inventory) + ", Location: "+str(self.location)


class Stage():
    """
    Stores all the information that is needed to create the game screens

    name: Refers to the stage

    description: Dictionary containing strings of text, where the level the player is on is the key, and the text
    to be displayed is the value. The "0" key indicates the text should remain the same regardless of level. Since
    the game is mainly textbased, the description is what the users read to understand the game plot. It is displayed
    as a textbox onto the screens.

    picture: File name for screen background, either a jpg. or png.

    buttonMapping: This is a list that contains objects of the MappingObject class. Will be used to
    generate buttons that lead the user to the next screen.

    backStep: Signals the number of screens back the back button should take you. Default is 1.

    clicked: Will check if stage attached to the button has been clicked on. Used to keep track of which
    stages/screens have already been viewed.

    backStage: This is used to generate the back button and direct the user from the current
    screen to the previous screen.

    inventorypic: Stores the image corresponding the option the user selects.

    """
    def __init__(self, name, description, picture, buttonMapping = None, backStep = 1, inventoryPic = None, clicked = False, backStage = None):
        self.name = name
        self.description = description
        self.picture = picture
        self.buttonMapping = buttonMapping
        self.backStep = backStep
        self.clicked = clicked
        self.backStage = backStage
        self.inventoryPic = inventoryPic

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class MappingObject():
    """
    This class connects Stages to each other - each contains the text that the screen buttons display and what stage it leads to.
    Each object corresponds to a button generated. For example, if the user is in the HALLWAY (stage),
    the MappingObjects will correspond to buttons leading to the KITCHEN and BEDROOM stages.

    stageMapTo: What stage the button leads to (KITCHEN, BEDROOM)

    levels: A list specifying which levels the button should appear in. Buttons shown will vary depending on level. A 0 indicates the
    Button will display in the appropriate screen regardless of level.

    backButton: Indicates whether the Button object created from the MappingObject will be a backButton or not.

    responseButton: Indicates whether the Button object created from the MappingObject will be a responseButton or not.

    """
    def __init__(self, stageMapTo, buttontext,levels,backButton = False, responseButton = False, dimensions = 1):
        self.stageMapTo = stageMapTo
        self.buttontext = buttontext
        self.levels = levels
        self.backButton = backButton
        self.responseButton = responseButton
        self.dimensions = dimensions

    def __str__(self):
        return str(self.stageMapTo)
    def __repr__(self):
        return str(self.stageMapTo)

def goBack(stage):
    """
    This function returns the stage that the user will go back to, depending on the backStep number associated with the input stage.

    For example:

    1 = returns previous stage (DIARY -> BEDROOM)

    2 = returns the stage two stages prior (LASAGNA -> KITCHEN, skips COOKBOOK)

    """
    if stage.backStep == 1:
        return stage.backStage
    else:
        return goBack(stage.backStage)


def storeDecision(stage,state):
    """
    This function takes the input selected by the user and stores it in
    the decisions dictionary, using the stage.name of the .

    For example, after the user chooses a FLOWER, a new screen will pop up
    with a description of the flower they chose. This will add to the state.decisions
    dictionary to allow any occurrences of the previous screen's name ("FLOWER") in text
    descriptions with the selected user input ("Daisy")

    For example:
    {"FLOWER" : "Daisy"} will allow any text descriptions to have the word FLOWER replaced with their input, "Daisy".

    """
    state.decisions[stage.backStage.name] = stage.name


def choiceSelection(stage,state):
    """
    Once the user selects a choice, the screen where they selected the choice will be replaced with the description
    of the choice they selected. The mappings between the stages then change such that the intermediary stage no longer exists.

    For example:
    Beginning mapping: (KITCHEN -> COOKBOOK -> LASAGNA or PIZZA or SALAD)
        Choice selection: (LASAGNA)
    After choice selection: (KITCHEN -> LASAGNA)
    """
    storeDecision(stage,state) #stores choice made by user

    #Store the MappingObject from previous stage associated with the button linked to current stage
    stagemappingobj = None
    oldBackStage = stage.backStage
    for mappingobj in oldBackStage.buttonMapping:
        if mappingobj.stageMapTo == stage:
            stagemappingobj = mappingobj

    #Look to see which stage the back button in current stage belongs to
    newBackStage = goBack(stage)

    #Changes the target stage mapping with the stage related to the user's selected option
    if stagemappingobj != None:
        for mappingobj in newBackStage.buttonMapping:
            if mappingobj.stageMapTo == oldBackStage:
                for index, newBackStageMappingObj in enumerate(newBackStage.buttonMapping):
                    if newBackStageMappingObj == mappingobj:
                        newBackStage.buttonMapping[index].stageMapTo = stagemappingobj.stageMapTo



def checkStageConditions(stage,state):
    """
    This function marks current stage as having been seen, calls the choiceSelection function if the stage is
    indicated to be a choice selction stage. Choice selection stages are marked by having a stage.backStep value > 1.
    """
    stage.clicked = True
    if stage.backStep > 1 :
        choiceSelection(stage, state)

def checkInventory(stage,state):
    """
    Once the user selects an option, it will add the photo of the option to state.inventory (if applicable).
    """
    if stage.clicked and stage.inventoryPic != None and stage.inventoryPic not in state.inventory:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('item.wav'))
        time.sleep(.2)
        state.inventory.append(stage.inventoryPic)













#end
