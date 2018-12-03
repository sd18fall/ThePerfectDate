
from Model import*

Cookbook = Stage('Grandma Smith’s CookBook', {0: 'The Grandma Smith CookBook is what you worship religiously. All the dishes are killer, and you cannot wait to begin the preparations. What should you make tonight?'},'kitchen.png')

Garden = Stage('Garden', {0: 'You have a beautiful flower garden in your backyard. You are obsessed with the way they look and have always treated them with tenderness and love. Which flower are you going to chose to use tonight? '},'garden.jpeg')

Trash = Stage('Trash', {0: 'You want to empty out the trash tonight, so everything is absolutely perfect! However, when you look into the trash can, you notice bouquets of flowers in the trash. Suddenly, you hear a noise from upstairs...'},'kitchen.png')

Kitchen = Stage('Kitchen', {0: 'Nothing screams cozy and comfy like a home cooked meal! You have been learning how to cook since you were child and am super eager to wow your date with your deliciously hypnotizing dishes!'},'kitchen.png',[MappingObject(Cookbook, 'Check out your favorite cookbook for a recipe to cook for tonight!', [1,2]), MappingObject(Garden, 'Head to your garden to choose a flower for tonight!', [1,2]), MappingObject(Trash, 'Take out the trash so the kitchen doesn’t smell weird later', [2])])

OutfitMakeup = Stage('Outfit and Makeup', {0: 'You have always loved picking out dresses, ever since you were little and you would dress up your dolls. Well tonight is the real deal and it is time to get serious about fashion. Which dress should you pick out for tonight?'},'bedroom.png')

Diary = Stage('Diary', {0: 'You have already read through this diary so many times you almost have it memorized. Which section do you want to reread?'},'bedroom.png')

Notes = Stage('Notes', {0: 'Have those notes always been there? They are percariously stacked up on the nightstand and are spilling over onto the floor. What do you do with the notes?'},'bedroom.png')

Bedroom = Stage('Bedroom', {0: 'Wow this room is a mess! You better clean up if you want to impress that special someone. Yes you are definitly going to clean. As soon as you are done picking out a dress. And putting on a little more makeup. Oh who are you kidding?'} ,'bedroom.png', [MappingObject(OutfitMakeup, 'Time to choose what to wear for this special Night!', [1,2]), MappingObject(Diary, 'Take a look at the Diary!', [1,2]), MappingObject(Notes, 'You notice a stack of notes on the table', [2])])

Hallway = Stage('Hallway', {0: 'Where do you want to go'},'livingroom.png',[MappingObject(Kitchen, 'Go downstairs to begin your cooking preparations for tonight!', [0]),MappingObject(Bedroom, 'Go upstairs to get ready!', [0])])

StartingPage = Stage('Start', {0 : 'The Perfect Date: Ever wanted to bring your dream date to reality?'},'livingroom.png', [MappingObject(Hallway, 'Start Game', [0])])


Cookbook.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])
Garden.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])
Trash.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])

Kitchen.backbuttonmapping = MappingObject(Hallway, 'Back to Hallway', [0])

OutfitMakeup.backbuttonmapping = MappingObject(Bedroom, 'Back to Bedroom', [0])
Diary.backbuttonmapping = MappingObject(Bedroom, 'Back to Bedroom', [0])
Notes.backbuttonmapping = MappingObject(Bedroom, 'Back to Bedroom', [0])

Bedroom.backbuttonmapping = MappingObject(Hallway, 'Back to Hallway', [0])




# def conditions(state):
#     if:
#         state.level += 1
