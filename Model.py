"""
MetaGame: Model Code

This part of the code contains the classes that
provide the major information for the other two documents.

Authors: Cynthia Yong, Sabrina Pereira, Sophie Schaffer
"""
import pygame

class State():
    """
    Stores the information of what has already happened, so the game will
    know when to move forward in the game.

    level: There are multiple levels in the game because different things happen in each level
    in order to move the game along.

    decisions: Decisions are made when the user chooses certain answers when prompted.
    Their answer will be stored in a dictionary in this class.

    """
    def __init__(self, level, decisions = None):
        self.level = level

        if decisions == None:
            self.decisions = {}

    def __str__(self):
        return "Level: " + str(self.level)+", Inventory: "+ str(self.inventory) + ", Location: "+str(self.location)


class Stage():
    """
    Stores all the information that is needed to create the game screens

    name: name of the stage

    description: since the game is mainly textbased, the description is what the users
    read to understand the game plot. It is displayed as a textbox onto the screens

    picture: screen background

    buttonMapping: this is a list that contains the button text and is used to
    generate buttons that lead the user to the next screen.

    backStep:

    clicked: will check if stage attached to the button is clicked because it will
    draw the next stage

    back: this is used to generate the back button and direct the user from the current
    screen to the previous screen.

    """
    def __init__(self, name, description, picture, buttonMapping = None, backStep = 1, clicked = False, back = None):
        self.name = name
        self.description = description
        self.picture = picture
        self.buttonMapping = buttonMapping
        self.backStep = backStep
        self.clicked = clicked
        self.back = back

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class MappingObject():
    """
    As mentioned previously, this class contains the text that the screen buttons display
    and what stage it leads to. For example, if the user is in the HALLWAY (stage),
    the MappingObjects will be KITCHEN and BEDROOM.

    stageMapTo: what stages the buttons lead to (KITCHEN, BEDROOM)

    levels: levels contain different buttons, so we need to specify which level
    we want the buttons to appear atself.

    backButton:

    """
    def __init__(self, stageMapTo, buttontext,levels,backButton = False):
        self.stageMapTo = stageMapTo
        self.buttontext = buttontext
        self.levels = levels
        self.backButton = backButton

    def __str__(self):
        return str(self.stageMapTo)
    def __repr__(self):
        return str(self.stageMapTo)

def goBack(stage): #do we need this still?
    """
    Most stages have a back button attached to it, which means when it is clicked,
    it will bring the user to the previous screen they were at. This function
    is used to indicate how many screens to go backself.

    For example:

    1 = go back one screens

    2 = go back two screens

    """
    if stage.backStep == 1:
        return stage.back
    else:
        return goBack(stage.back)

def choiceSelection(stage,state):
    """
    Once the user selects an input and goes back to the screen where they
    selected the input, it will replace that screen with the description
    of the input they selected.
    """

    storeDecision(stage,state) #finds mapping object that represents the input chosen

    oldBackStage = stage.back
    for mappingobj in oldBackStage.buttonMapping: #checks each mappingobject in the buttonMapping list of the previous stage with the input options
        if mappingobj.stageMapTo == stage: #if one of the mappingobject inputs is equal to the current stage, then
            stagemappingobj = mappingobj #???? ask about this part

    newBackStage = goBack(stage)

    #replaces the screen with the input that was chosen
    for mappingobj in newBackStage.buttonMapping:
        if mappingobj.stageMapTo == oldBackStage:
            for n, i in enumerate(newBackStage.buttonMapping):
                if i == mappingobj:
                    newBackStage.buttonMapping[n].stageMapTo = stagemappingobj.stageMapTo

def storeDecision(stage,state):
    """
    This function takes the input selected by the user and stores it in
    the decisions dictionary in the state class as the value.

    For example, after the user chooses a FLOWER, a new screen will pop up
    with a description of the flower they chose. Then this code will replace
    the name of the previous screen (FLOWER) with the current stage name (Daisy)

    For example:
    {FLOWER : Daisy}

    """
    state.decisions[stage.back.name] = stage.name

def checkStageConditions(stage,state):
    """
    This function marks current stage as having been seen
    and checks if any choice is a permanent change
    """
    stage.clicked = True
    if stage.backStep == 2:
        choiceSelection(stage, state)












#end
