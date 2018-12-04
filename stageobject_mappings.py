
from Model import*

Lasagna = Stage('Lasagna', {0: 'Making the Lovers Lasagna takes a biiit longer than you expected, but once it is in the oven the room immediatly smells delicious'},'kitchen.png')

Pizza = Stage('Pizza', {0: 'Oof, there may or may not be some tomato sauce in your hair. You had better go clean up, but it is going to be totally worth it when the Platonic Pizza is done it will be totally worth it!'},'kitchen.png')

Salad = Stage('Salad', {0: 'Well you made a salad. Even with a cool name like Sweetheart Cesear Salad it is still just a salad, so congrats I guess?'},'kitchen.png')

Cookbook = Stage('Grandma Smith’s CookBook', {0: 'The Grandma Smith CookBook is what you worship religiously. All the dishes are killer, and you cannot wait to begin the preparations. What should you make tonight?'},'kitchen.png',[MappingObject(Lasagna, 'Makes some delicious homemade Lovers Lasagna!', [1]), MappingObject(Pizza, 'Break out the dough and make some savory Platonic Pizza!', [1]), MappingObject(Salad, 'Keep it light and whip out a Sweetheart Ceaser Salad', [1])])

Rose = Stage('Rose', {0: 'You prick your fingers trying to pick the Rose, but no flower can defeat you!'},'garden.jpeg')

Daisy = Stage('Daisy', {0: 'A Daisy can put up little resistance to your giant hedge clippers.'},'garden.jpeg')

Sunflower= Stage('Sunflower', {0: 'Nothing says, "I like you" like a flower as big as your face. The Sunflower you picked is a giant monster flower and you are proud of yourself'},'garden.jpeg')

Garden = Stage('Garden', {0: 'There is a beautiful flower garden in the backyard. You are obsessed with the way flowers look and have always treated them with tenderness and love. Which flower are you going to chose to use tonight? '},'garden.jpeg',[MappingObject(Rose, 'Roses are a classic!', [1]), MappingObject(Daisy, 'A Daisy is simple and elegant', [1]), MappingObject(Sunflower,'Sunflowers are big and beautiful', [1])])

Trash = Stage('Trash', {0: 'You want to empty out the trash tonight, so everything is absolutely perfect! However, when you look into the trash can, you notice bouquets of flowers in the trash. Suddenly, you hear a noise from upstairs...'},'kitchen.png')

Kitchen = Stage('Kitchen', {0: 'Nothing screams cozy and comfy like a home cooked meal! You have been learning how to cook since you were child and am super eager to wow your date with your deliciously hypnotizing dishes!'},'kitchen.png',[MappingObject(Cookbook, 'Check out your favorite cookbook for a recipe to cook for tonight!', [1,2]), MappingObject(Garden, 'Head to your garden to choose a flower for tonight!', [1,2]), MappingObject(Trash, 'Take out the trash so the kitchen doesn’t smell weird later', [2])])

SunDress= Stage('SunDress', {0: 'What a cute Sun Dress! Yellow with pink flowers, this warm summery look will light up any room!'},'bedroom.png')

TShirt= Stage('TShirt', {0: 'T Shirt and Jeans is just a classic Julia outfit, and why mess with a classic??'},'bedroom.png')

PowerSuit= Stage('PowerSuit', {0: 'Go big or go home. Nothing screams confidence like a bright red suit. And the best part is it basically matches everything!'},'bedroom.png')

OutfitMakeup = Stage('Outfit and Makeup', {0: 'You have always loved picking out dresses, ever since you were little and you would dress up your dolls. Well tonight is the real deal and it is time to get serious about fashion. Which should you pick out for tonight?'},'bedroom.png', [MappingObject(SunDress, 'Sun Dress', [1]), MappingObject(TShirt, 'T Shirt', [1]), MappingObject(PowerSuit,'Power Suit', [1])])

Stranger= Stage('Stranger', {0: '"I saw a very Handsome Stranger the other day in the park today! He was staring right at me and his blue eyes reminded me of Steven. I sure hope Steven calls soon..."'},'bedroom.png')

Dreams= Stage('Dreams', {0: '"I keep having the same dream over and over agian. I am sitting in my kitchen and I am having THE most amazing date with THE most handsome man. He has beautiful blue eyes... I sure hope that its foreshadowing!"'},'bedroom.png')

LoveLife= Stage('LoveLife', {0: '"I cannot stop thinking about Steven! When we talked on the phone last week I had butterflies for hours! I sure hope he asks me on a date soon..."'},'bedroom.png')

Diary = Stage('Diary', {0: 'You have already read through this diary so many times you almost have it memorized. Which section do you want to reread?'},'bedroom.png', [MappingObject(Stranger, '"I saw a very Handsome Stranger the other day...""', [1]), MappingObject(Dreams, '"I keep having the same dream..."', [1]), MappingObject(LoveLife,'I cannot stop thinking about Steven!...', [1])])

Notes = Stage('Notes', {0: 'Have those notes always been there? They are percariously stacked up on the nightstand and are spilling over onto the floor. What do you do with the notes?'},'bedroom.png')

Bedroom = Stage('Bedroom', {0: 'Wow this room is a mess! You better clean up if you want to impress that special someone. Yes you are definitly going to clean. As soon as you are done picking out a dress. And putting on a little more makeup. Oh who are you kidding?'} ,'bedroom.png', [MappingObject(OutfitMakeup, 'Time to choose what to wear for this special Night!', [1,2]), MappingObject(Diary, 'Take a look at the Diary!', [1,2]), MappingObject(Notes, 'You notice a stack of notes on the table', [2])])

Hallway = Stage('Hallway', {0: 'Where do you want to go'},'livingroom.png',[MappingObject(Kitchen, 'Go downstairs to begin your cooking preparations for tonight!', [0]),MappingObject(Bedroom, 'Go upstairs to get ready!', [0])])

StartingPage = Stage('Start', {0 : 'The Perfect Date: Ever wanted to bring your dream date to reality?'},'livingroom.png', [MappingObject(Hallway, 'Start Game', [0])])


#Cookbook.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])
#Garden.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])

Lasagna.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])
Salad.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])
Pizza.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])

Rose.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])
Daisy.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])
Sunflower.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])

Trash.backbuttonmapping = MappingObject(Kitchen, 'Back to Kitchen', [0])

Kitchen.backbuttonmapping = MappingObject(Hallway, 'Back to Hallway', [0])



#OutfitMakeup.backbuttonmapping = MappingObject(Bedroom, 'Back to Bedroom', [0])
#Diary.backbuttonmapping = MappingObject(Bedroom, 'Back to Bedroom', [0])

SunDress.backbuttonmapping = MappingObject(Bedroom, 'Back to Bedroom', [0])
TShirt.backbuttonmapping = MappingObject(Bedroom, 'Back to Bedroom', [0])
PowerSuit.backbuttonmapping = MappingObject(Bedroom, 'Back to Bedroom', [0])

Stranger.backbuttonmapping = MappingObject(Bedroom, 'Back to Bedroom', [0])
Dreams.backbuttonmapping = MappingObject(Bedroom, 'Back to Bedroom', [0])
LoveLife.backbuttonmapping = MappingObject(Bedroom, 'Back to Bedroom', [0])

Notes.backbuttonmapping = MappingObject(Bedroom, 'Back to Bedroom', [0])

Bedroom.backbuttonmapping = MappingObject(Hallway, 'Back to Hallway', [0])




# def conditions(state):
#     if:
#         state.level += 1
