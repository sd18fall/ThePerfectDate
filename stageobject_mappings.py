
from Model import*

Cookbook = Stage('Grandma Smith’s CookBook', {0: 'The Grandma Smith CookBook is what you worship religiously. All the dishes are killer, and you cannot wait to begin the preparations. What should you make tonight?'},'kitchen.png')

Garden = Stage('Garden', {0: 'You have a beautiful flower garden in your backyard. You are obsessed with the way they look and have always treated them with tenderness and love. Which flower are you going to chose to use tonight? '},'garden.jpeg')

Trash = Stage('Trash', {0: 'You want to empty out the trash tonight, so everything is absolutely perfect! However, when you look into the trash can, you notice bouquets of flowers in the trash. Suddenly, you hear a noise from upstairs...'},'kitchen.png')

Kitchen = Stage('Kitchen', {0: 'Nothing screams cozy and comfy like a home cooked meal! You have been learning how to cook since you were child and am super eager to wow your date with your deliciously hypnotizing dishes!'},'kitchen.png',[MappingObject(Cookbook, 'Check out your favorite cookbook for a recipe to cook for tonight!', [1,2]), MappingObject(Garden, 'Head to your garden to choose a flower for tonight!', [1,2]), MappingObject(Trash, 'Take out the trash so the kitchen doesn’t smell weird later', [2])])

Hallway = Stage('Hallway', {0: 'Where do you want to go'},'livingroom.png',[MappingObject(Kitchen, 'Go downstairs to begin preparations for tonight!', [0])])

StartingPage = Stage('Start', {0 : 'The Perfect Date: Ever wanted to bring your dream date to reality?'},'livingroom.png', [MappingObject(Hallway, 'Start Game', [0])])


Cookbook.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])
Garden.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])
Trash.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])

















#
# Bedroom = Stage('Bedroom', 'The room is messy and the lights are dim.', [DairyObject, OutfitMakeupObject], backbutton)
#
#
# Diary = Stage()
# DiaryObject = MappingObject()
#
# OutfitMakeup = Stage()
# OutfitMakeupObject = MappingObject()
#
# Notes = Stage()
# NotesObject = MappingObject()
#
# Kitchen = Stage()
#
#
#
# BedroomObject = MappingObject()s
#
# BackButton = MappingObject()
