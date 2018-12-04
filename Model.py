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
    def __init__(self, level, inventory = None, location= None):
        self.level = level
        self.inventory = inventory
        self.location = location

    def __str__(self):
        return "Level: " + str(self.level)+", Inventory: "+ str(self.inventory) + ", Location: "+str(self.location)


class Stage():
    """
    Stores all the information that will be used to project onto the screen to help user move
    along in the game

    fix doc strings

    """
    def __init__(self, name, description, picture, buttonmapping = None, back = None, backStep = 1):
        self.name = name
        self.description = description
        self.picture = picture
        self.buttonmapping = buttonmapping
        self.back = back
        self.backStep = backStep


class MappingObject():
    """
    Contains information about text the button displays and what stage is leads
    to
    """
    def __init__(self, stageMapTo, buttontext,levels):
        self.stageMapTo = stageMapTo
        self.buttontext = buttontext
        self.levels = levels



def goBack(stage):
    if stage.backStep == 1:
        return stage.back
    else:
        return goBack(stage.back)

def choiceSelection(stage):
    stage.backStep = 1 #might hardcode
    oldBackStage = goBack(stage)
    for mappingobj in oldBackStage.buttonmapping:
        if mappingobj.stageMapTo = stage:
            stagemappingobj = mappingobj

    stage.backStep = 2 #might hardcode 2
    newBackStage = goBack(stage)

    for mappingobj in newBackStage.buttonmapping:
        if mappingobj.stageMapTo = oldBackStage:
            newBackStage.buttonmapping.remove(mappingobj)
            newBackStage.buttonmapping.append(stagemappingobj)

    stage.back = newBackStage












sdfsds
