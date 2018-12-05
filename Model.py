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
    def __init__(self, level, flower = None):
        self.level = level
        self.flower = flower

    def __str__(self):
        return "Level: " + str(self.level)+", Inventory: "+ str(self.inventory) + ", Location: "+str(self.location)


class Stage():
    """
    Stores all the information that will be used to project onto the screen to help user move
    along in the game

    fix doc strings

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
    Contains information about text the button displays and what stage is leads
    to
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

def goBack(stage):
    if stage.backStep == 1:
        return stage.back
    else:
        return goBack(stage.back)

def choiceSelection(stage):
    #finds mapping object that represents the object chosen
    oldBackStage = stage.back
    for mappingobj in oldBackStage.buttonMapping:
        if mappingobj.stageMapTo == stage:
            stagemappingobj = mappingobj

    newBackStage = goBack(stage)

    #replaces options with the option that was chosen
    for mappingobj in newBackStage.buttonMapping:
        if mappingobj.stageMapTo == oldBackStage:
            for n, i in enumerate(newBackStage.buttonMapping):
                if i == mappingobj:
                    newBackStage.buttonMapping[n].stageMapTo = stagemappingobj.stageMapTo


def checkStageConditions(stage):
    """marks current stage as having been seen and checks if any choice is a permanent change"""
    stage.clicked = True
    if stage.backStep == 2:
        choiceSelection(stage)












#end
