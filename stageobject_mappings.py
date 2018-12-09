"""
MetaGame: Game Data
Authors: Cynthia Yong, Sabrina Pereira, Sophie Schaffer


This file contains all of the Stages and related functions to run the game.
Think of Model.py and ViewerandController.py as the blueprint for generating a textbased game
and this file as the data for the game.

ONE IMPORTANT RULE: Be mindful of the order of stages. If you call a stage before it is made, then
the game will crash. One thing we did was to put the first screen the user sees at the bottom of
the list because it contains the buttons to everything else.


We decided to create a new file for inputting the game data in case users are interested in changing
the game plot. All they have to do is go in and edit the stages in this file without accidentally
changing the blueprint of the game. :)
"""

from Model import *


Lasagna = Stage('lasagna', {0: 'Making the Lovers Lasagna takes a biiit longer than you expected, but once it is in the oven the room immediatly smells delicious.'},'kitchen.png', None, 2,'lasagna.png')

Pizza = Stage('pizza', {0: 'Oof, there may or may not be some tomato sauce in your hair. You had better go clean up, but it is going to be totally worth it when the Platonic Pizza is out of the oven!'},'kitchen.png',None, 2,'pizza.png')

Salad = Stage('salad', {0: 'Well you made a salad. Even with a cool name like Sweetheart Cesear Salad it is still just a salad, so congrats I guess?'},'kitchen.png', None, 2,'salad.png')

Cookbook = Stage('COOKEDMEAL', {0: 'The Grandma Smith CookBook is decades old. All the dishes are killer, and you cannot wait to begin the preparations. What should you make tonight?'},'kitchen.png',
[MappingObject(Lasagna, 'Makes some delicious homemade Lovers Lasagna!', [0]),
    MappingObject(Pizza, 'Break out the dough and make some savory Platonic Pizza!', [0]),
    MappingObject(Salad, 'Keep it light and whip out a Sweetheart Ceaser Salad', [0])])

Rose = Stage('roses', {0: 'You prick your fingers trying to pick the rose, but no flower can defeat you! On your way back to the house a neighbor gives you a funny look, but you just stick your toungue out at him'},'garden.jpeg',None, 2,'rose.png')

Daisy = Stage('daisies', {0: 'The daisies can put up little resistance to your giant hedge clippers. On your way back to the house a neighbor gives you a funny look, but you just stick your toungue out at him'},'garden.jpeg', None, 2,'daisy.png')

Sunflower= Stage('sunflowers', {0: 'Nothing says, "I like you" like a flower as big as your face. The sunflower you picked is a giant monster flower and you are proud of yourself. On your way back to the house a neighbor gives you a funny look, but you just stick your toungue out at him'},'garden.jpeg', None, 2,'sunflower.png')

Garden = Stage('FLOWER', {0: 'There is a beautiful flower garden in the backyard. You are obsessed with the way flowers look and love this garden, but you have never had much luck as a gardener. Flowers are a great way to impress a date and you want to use your favorite one tonight'},'garden.jpeg',
[MappingObject(Rose, 'Roses are a classic!', [1]),
    MappingObject(Daisy, 'Daisies are simple and elegant', [1]),
    MappingObject(Sunflower,'Sunflowers are big and beautiful', [1])])

Trash = Stage('Trash', {0: 'You want to empty out the trash tonight, so everything is absolutely perfect! However, when you look into the trash can, you notice bouquets of flowers with a note signed, "Your Beloved". These don\'t belong in the here, they are good as new! Suddenly, you think you hear a noise from upstairs... Eh it\'s probably nothing'},'kitchen.png')

Kitchen = Stage('Kitchen', {1: 'Nothing screams cozy and comfy like a home cooked meal! You have been learning how to cook since you were a child and are super eager to wow your date with your deliciously hypnotizing dishes!',2: 'Time to clean up! The kitchen is a mess after all that cooking and for some reason there is a weird smell',3: 'Time to clean up! The kitchen is a mess after all that cooking and for some reason there is a weird smell'},'kitchen.png',
[MappingObject(Cookbook, 'Check out your favorite cookbook for a recipe to cook for tonight!', [1]),
    MappingObject(Garden, 'Head to the garden to choose a flower for tonight!', [1]),
    MappingObject(Trash, 'Take out the trash so the kitchen doesn’t smell weird later', [2,3])])

Dishes2 = Stage('Dishes', {0: 'You have to search a little to find the right cabinets to put all the dishes in but eventually everything is away. For the love of God what is happening upstairs.'},'kitchen.png',None,9)

Dishes = Stage('Dishes', {0: 'You wash and dry all of the dishes. Woo you really made a mess earleir. Sweat drips down your forehead.'},'kitchen.png',
[MappingObject(Dishes2,'Put away the dishes',[0])],8)

Napkins = Stage('Napkins', {0: 'You fold the white napkins to look like cranes and leave one at each end of the table. Your heart is beating fast.'},'kitchen.png',
[MappingObject(Dishes,'Uh oh you forgot to do the dishes!',[0])],7)

Weapon = Stage('Weapon', {0: 'You shove a newly polished fork in your pocket. Might be useful later. Are the noises upstairs getting louder?'},'kitchen.png',None,7,'fork.png')

Polish = Stage('Polish', {0: 'This silverware is looking a little dull. Nothing a little elbow grease cannot fix! You feel like someone is watching you.'},'kitchen.png',
[MappingObject(Napkins,'Put out napkins',[0]),
MappingObject(Weapon,'Use a fork as a weapon',[0])],6)

LightCandles = Stage('LightCandles', {0: 'These candles really set the mood. Classy. Elegant. You hear footsteps echo from the bedroom.'},'kitchen.png',
[MappingObject(Polish,'Polish the silverware',[0])],5)

SetTable = Stage('SetTable', {0: 'You start to set the table for tonight. Everything has to be perfect. The FLOWER you picked out earlier are quite the centerpiece. You hear a door slam.'},'kitchen.png',
[MappingObject(LightCandles,'Time to light some candles',[0])],4)

TableCloth = Stage('TableCloth', {0: 'The table cloth is floral and almost matches the plates! Did you just see a shadow coming from upstairs?'},'kitchen.png',
[MappingObject(SetTable,'Set the table',[0])],3)

PrepareFood = Stage('PrepareFood', {0: 'You take the COOKEDMEAL out of oven, and it is to die for! Well done! There is rustling noises coming from upstairs.'}, 'kitchen.png',
[MappingObject(TableCloth,'Lay out a beautiful tablecloth',[0])],2)

EndKitchen = Stage('Kitchen', {0:'You hear a loud crashing sound from upstairs!!'}, 'kitchen.png',
[MappingObject(PrepareFood,'Get the food out of the oven',[3,4])])

SunDress= Stage('sun dress', {0: 'What a cute sun dress! Yellow with pink flowers, this warm summery look will light up any room!'},'bedroom.png', None, 2,'dress.png')

TShirt= Stage('T shirt', {0: 'T shirt and jeans is just a classic NAME outfit, and why mess with a classic??'},'bedroom.png', None, 2,'shirt.png')

PowerSuit= Stage('power suit', {0: 'Go big or go home. Nothing screams confidence like a bright red suit. And the best part is it basically matches everything!'},'bedroom.png', None, 2,'suit.png')

Outfit = Stage('OUTFIT', {0: 'You have always loved picking out dresses, ever since you were little and you would dress up your dolls. Well tonight is the real deal and it is time to get serious about fashion. Which should you pick out for tonight?'},'bedroom.png',
[MappingObject(SunDress, 'Sun Dress', [1]),
    MappingObject(TShirt, 'T Shirt', [1]),
    MappingObject(PowerSuit,'Power Suit', [1])])

Stranger= Stage('Stranger', {0: '"Dear Diary, I was talking to Steven on the phone in the park today and I saw a very Handsome Stranger! He was staring right at me, he had striking blue eyes. But he kept staring a little too long and gave me a kind of creepy smile. -Love NAME"'},'bedroom.png')

Dreams= Stage('Dreams', {0: '"Dear Diary, I keep having the same dream over and over again. I am sitting in my kitchen and I am having THE most amazing date.. I sure hope that it\'s foreshadowing! -Love NAME"'},'bedroom.png')

LoveLife= Stage('LoveLife', {0: '"Dear Diary, I cannot stop thinking about Steven! When we talked on the phone last week I had butterflies for hours! I sure hope he asks me on a date soon... -Love NAME"'},'bedroom.png')

Diary = Stage('Diary', {0: 'You have already read through this diary so many times you almost have it memorized. Which section do you want to reread?'},'bedroom.png',
[MappingObject(Stranger, '"I saw a very Handsome Stranger the other day...""', [1,2]),
    MappingObject(Dreams, '"I keep having the same dream..."', [1,2]),
    MappingObject(LoveLife,'"I cannot stop thinking about Steven!...""', [1,2])])

NoteSteven = Stage('NoteSteven', {0: '"Dear NAME, what are you doing with Steven??? Don\'t you know that he isn\'t good for you?? I am the one giving you good advice, and sending you FLOWER when you have a bad day. You belong with me. -Your Beloved"'},'bedroom.png')

NoteGarden = Stage('NoteGarden', {0: '"Dear NAME, your flower garden is coming along swimmingly! I am a big fan of the FLOWER, those are my favorite! You are so good at gardening, you must have a green thumb! -Your Beloved"'},'bedroom.png')

NotePark = Stage('NotePark', {0: '"Dear NAME, I saw you in the park today. You looked beautiful in your OUTFIT. I love it when you wear OUTFITs. Why did you wear your hair in a ponytail? It looks better down, I already wrote to you about that. You should really listen to me more. -Your Beloved "'},'bedroom.png')

Notes = Stage('Notes', {0: 'There are a ton of letters all over. Some are percariously stacked up on the nightstand and are spilling over onto the floor. Which letter do you want to read before putting them away?'},'bedroom.png',
[MappingObject(NoteSteven,'"What are you doing with Steven???"',[0]),
    MappingObject(NoteGarden,'"Your flower garden is coming along swimmingly!"',[0]),
    MappingObject(NotePark,'"I saw you in the park today"',[0])])

Bedroom = Stage('Bedroom', {1: 'The room is extremely cozy and great for cuddling! It smells of freshly baked chocolate chip cookies and makes you feel warm and fuzzy inside. You are even more excited for what\'s to come tonight.', 2: 'Wow this room is a mess! Are those dirty socks? Is that a beer bottle on the dresser? Yikes! It looks like a hurricane came through here. You better clean up if you want to impress that Special Someone.',3: 'Wow this room is a mess! Are those dirty socks? Is that a beer bottle on the dresser? Yikes! It looks like a hurricane came through here. You better clean up if you want to impress that Special Someone.'} ,'bedroom.png',
[MappingObject(Outfit, 'Time to choose what to wear for this special night!', [1]),
    MappingObject(Diary, 'Take a look at the Diary!', [1]),
    MappingObject(Notes, 'Tidy up the stack of letters in a messy pile on the table', [2,3])])

NotOver = Stage('NotOver',{0: 'No reason to ruin a perfectly good date over a little spat. You help NAME get dressed in her OUTFIT and bring her downstairs to share some delicious COOKEDMEAL!'},'kitchen.png')

TryAgain = Stage('TryAgain',{0: 'Better luck with the next girl. Try again?'},'bedroom.png')

TheEnd = Stage('TheEnd',{0: 'The End'},'Black.jpg')

ForkAttack = Stage('ForkAttack',{0: 'You use fork to stab NAME once in the stomach. She staggers back. Your instincts take over. You throw her against the wall. There is a loud cracking noise and her head is tilted at a weird angle. You shake her a couple times, but she is not breathing.'},'Dark.jpeg',
[MappingObject(TryAgain,'Try again',[0]),
MappingObject(NotOver,'This isn\'t over',[0])])

Pulled = Stage('Pulled',{0: 'You pull NAME onto the ground. Hard. There is a loud cracking noise and her arms go limp.'},'Dark.jpeg',
[MappingObject(TryAgain,'Try again',[0]),
MappingObject(NotOver,'This isn\'t over',[0])])

Bottle2 = Stage('Bottle2',{0: 'While you are distracted NAME grabs a lamp and swings it over her head. Her face is red and she is baring her teeth. She brings it down over your head and everything goes dark.'},'Black.jpg',
[MappingObject(TheEnd,'The End',[0])])

Bottle = Stage('Bottle',{0: 'You jump up and grab the bottle before NAME. You didn\'t want to have to use it but she reached for it first. This is breaking your heart.'},'Dark.jpeg',
[MappingObject(Bottle2 ,'Use the bottle',[0])],1,'beer-bottle.png')

Approach8 = Stage('Approach8',{0: 'You touch the back of your head and your fingers are red with blood. Everything is in slow motion. NAME lunges for the beer bottle.'},'Dark.jpeg',
[MappingObject(Pulled,'Pull her down',[0]),
MappingObject(Bottle,'Get the bottle first',[0])])

Approach7 = Stage('Approach7',{0: 'You try to push NAME away but she trips you. You are trying to explain to her, you love her, you only want what is best for her, as she kicks you in the head.'},'Dark.jpeg',
[MappingObject(Approach8,'Check on your head',[0])])

Approach6 = Stage('Approach6',{0: 'You scream and pull NAME towards you. She rams into you and grabs you by the arms. She is reaching for an empty beer bottle on the nightstand. You try to turn her around and push her against the wall.'},'Dark.jpeg',
[MappingObject(Approach7,'Subdue her',[0]),
MappingObject(ForkAttack,'Use the fork',[5])])

Approach5 = Stage('Approach5',{0: 'NAME struggles to get away but you do not let go.'},'Dark.jpeg',
[MappingObject(Approach6,'SHE IS RUINING EVERYTHING!',[0]),
MappingObject(Approach6,'WHY IS SHE BEING SUCH A BITCH!',[0])])

Approach4 = Stage('Approach4',{0: 'NAME manages to dodge your hug and scratches you on the cheek. You see her looking for an escape. You grab her by the arm.'},'Dark.jpeg',
[MappingObject(Approach6,'SHE IS RUINING EVERYTHING!',[0]),
MappingObject(Approach6,'WHY IS SHE BEING SUCH A BITCH!',[0]),
MappingObject(Approach5,'Stay rational',[0])])

Approach3 = Stage('Approach3',{0: 'You say, "NAME, I am still not done preparing for our perfect date, and you didn\'t even put on the OUTFIT I put out for you. If you don\'t calm down, I will have to tie you up again and put you back into the closet. I need time to finish getting ready for you" She says, "I\'LL CALL THE POLICE!"'},'Dark.jpeg',
[MappingObject(Approach4,'Hug it out',[0])])

Approach2 = Stage('Approach2',{0: 'She screams, "GET...OUT...OF...MY HOUSE!!!" You are very confused at this point. You say, "But, it\'s just me, Your Beloved. And you are supposed to be waiting for me to come pick you up for our date."'},'bedroom.png',
[MappingObject(Approach3,'Threaten her to calm down',[0])])

Approach = Stage('Approach',{0: 'She says "Stay away from me! First you send me all those stupid flowers, then the letters, now youv\'e resorted to locking me in my own closet!? You need to leave. Now!". She does not know whats happening. She needs to be calmed down.'},'bedroom.png',
[MappingObject(Approach2,'Force her to calm down',[0])])

Corner = Stage('Corner',{0: 'She mumbles something under her breath and backs away from you into a corner of the room. She is looking back and forth between you and the chair in the closet.'},'bedroom.png',
[MappingObject(Approach,'Calm her down',[0])])

EndBedroom = Stage('Bedroom', {0:'It\'s hard to focus on dinner when it feels like something is wrong upstairs. You walk up to the bedroom and feel a pit in your stomach. You think you know what the noise coming from the closet is and you\'re right. She is staggering out of the closet. What\'s she doing?'} ,'bedroom.png',
[MappingObject(Corner,'"What are you doing?"',[0])])

Hallway = Stage('Hallway', {1: 'Time to get ready! Where do you want to go?',2: 'Now that you have a OUTFIT layed out on the bed and some COOKEDMEAL in the oven it is time to clean the house', 3: 'The oven timer is going off! Time to go check on your COOKEDMEAL!', 4: 'Where do you want to go?', 5: 'Where do you want to go'}, 'livingroom.png',
[MappingObject(Kitchen, 'Go downstairs to the kitchen!', [1]),
    MappingObject(Kitchen, 'Go downstairs to clean the kitchen!', [2]),
    MappingObject(EndKitchen,'Go downstairs to the kitchen and check on the oven!',[3,4,5]),
    MappingObject(Bedroom, 'Go upstairs to the bedroom!', [1,3]),
    MappingObject(Bedroom, 'Go upstairs to clean the bedroom!', [2]),
    MappingObject(EndBedroom,'Go upstairs to the bedroom!',[4,5])])

Intro3 = Stage('Intro3', {0 : 'There is no time to worry about brunch on a day like today! Tonight is a big night!'},'livingroom.png',
[MappingObject(Hallway, 'Start the preparations!', [0])])

Intro2 = Stage('Intro2', {0 : '"Good morning NAME, it\'s mom! Are you still in bed, you sleepy head? You missed our family brunch. Anyways, love you sweetheart. Call me soon."'}, 'livingroom.png', [MappingObject(Intro3, 'Aww so cute', [0])])

Intro = Stage('Intro', {0 : 'You finish washing your hands and shoot yourself a smile in the mirror. You wink once at your reflection and admire how nice you look today! Your blue eyes are especially vibrant. You hear a phone ring and go to voice mail.'},'livingroom.png', [MappingObject(Intro2, '"Hm I bet I know who that is!"', [0])])

StartingPage2 = Stage('', {0 : 'What is your favorite girls name?'},'livingroom.png', [MappingObject(Intro, '', [0],False, responseButton = True)],2)


StartingPage = Stage('Intro', {0 : 'Ever wanted to bring your dream date to reality?'},'livingroom.png', [MappingObject(StartingPage2, 'Yes', [0])])

Name = Stage('NAME', {0 : ''},'livingroom.png', [MappingObject(StartingPage, 'Start', [0])])

Name2 = Stage('NAME', {0 : ''},'', [MappingObject(Name, '', [0])])

LoopApproach5 = Stage('LoopApproach5',{0: 'NAME continues to struggle to get away but you still do not let go'},'Dark.jpeg',
[MappingObject(Approach6,'SHE IS RUINING EVERYTHING!',[0]),
MappingObject(Approach6,'WHY IS SHE BEING SUCH A BITCH!',[0]),
MappingObject(Approach5,'Stay rational',[0])])

#Needed to be put at the end as LoopApproach5 was one of the last stages created, but we wanted stage Approach5 to be able to access it.
Approach5.buttonMapping.append(MappingObject(LoopApproach5,'Stay rational',[0]))


"""
This part connects all stages in a hierarchy, assigning the bottomest tier stages which stage is the one previous. In our case, the HALLWAY stage is at the top of the hierarchy, as all other stages stem from it.
"""

#Beginning kitchen mappings
StartingPage2.backStage = Name
Name.backStage = Name2

Cookbook.backStage = Kitchen
Garden.backStage = Kitchen

Lasagna.backStage = Cookbook
Salad.backStage = Cookbook
Pizza.backStage = Cookbook

Rose.backStage = Garden
Daisy.backStage = Garden
Sunflower.backStage = Garden

Trash.backStage = Kitchen

Kitchen.backStage = Hallway

#Beginning bedroom mappings
Outfit.backStage = Bedroom
Diary.backStage = Bedroom

SunDress.backStage = Outfit
TShirt.backStage = Outfit
PowerSuit.backStage = Outfit

Stranger.backStage = Diary
Dreams.backStage= Diary
LoveLife.backStage= Diary

Notes.backStage = Bedroom
NoteSteven.backStage = Notes
NotePark.backStage = Notes
NoteGarden.backStage = Notes

Bedroom.backStage = Hallway

#End room mappings
EndBedroom.backStage = Hallway

EndKitchen.backStage = Hallway
PrepareFood.backStage = EndKitchen
TableCloth.backStage = PrepareFood
SetTable.backStage = TableCloth
LightCandles.backStage = SetTable
Polish.backStage = LightCandles
Napkins.backStage = Polish
Weapon.backStage = Polish
Dishes.backStage = Napkins
Dishes2.backStage = Dishes




"""
The list belows contains all the stages that need back buttons.
We do not want all stages to have back buttons, for the purpose of gameplay.
"""
backButtonList = [Lasagna,Salad,Pizza,Rose,Daisy,Sunflower,Trash,Kitchen,SunDress,TShirt,PowerSuit,Stranger,Dreams,LoveLife,Diary,Notes,Bedroom,EndKitchen,PrepareFood,SetTable,TableCloth,LightCandles,Polish,Weapon,Napkins,Dishes,Dishes2,NoteSteven,NotePark,NoteGarden]

def backButtonGen (stage):
    """
    This function adds a MappingObject representing a back button to the stage.buttonMapping list. Back buttons are
    in a static position while the other buttons in the list will be mathematically placed onto the
    screen depending on number of buttons and size.
    """
    backButton = MappingObject(goBack(stage),'Go back to the ' + str(goBack(stage).name),[0],True)
    if stage.buttonMapping != None:
        stage.buttonMapping.append(backButton)
    else:
        stage.buttonMapping = [backButton]

def allBackButtonGen (backButtonList):
    """
    This function generates a backbutton for every stage in the backButtonList.
    """
    for stage in backButtonList:
        backButtonGen(stage)


allBackButtonGen(backButtonList) #generates backbuttons for all stages in backButtonList


def levelConditions(state,stage):
    """
    This is specifically created for purpose of the game plot. It sets the conditions for when
    the game level changes and the plot moves forward.
    """
    if state.level == 1 and Diary.clicked and Outfit.clicked and Garden.clicked and Cookbook.clicked:
        state.level = 2 #Trash and Notes appear
    elif state.level == 2 and Trash.clicked and Notes.clicked:
            state.level = 3 #Oven goes off in Hallway
    elif state.level == 3 and EndKitchen.clicked:
        state.level =4 #Sound is heard in the bedroom
    elif state.level == 4 and Weapon.clicked:
        state.level = 5 #Unlocks weapon options

def checkEvents(state,stage):
    """
    Checks for specific events in the game that triggers a specific graphic
    """
    # if Name.clicked:
    #     win.blit(pygame.transform.scale(pygame.image.load('Logo.png'),(100,80)),(200, 100))








#end
