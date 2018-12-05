
from Model import*

Lasagna = Stage('Lasagna', {0: 'Making the Lovers Lasagna takes a biiit longer than you expected, but once it is in the oven the room immediatly smells delicious'},'kitchen.png', None, 2)

Pizza = Stage('Pizza', {0: 'Oof, there may or may not be some tomato sauce in your hair. You had better go clean up, but it is going to be totally worth it when the Platonic Pizza is done it will be totally worth it!'},'kitchen.png',None, 2)

Salad = Stage('Salad', {0: 'Well you made a salad. Even with a cool name like Sweetheart Cesear Salad it is still just a salad, so congrats I guess?'},'kitchen.png', None, 2)

Cookbook = Stage('DISH', {0: 'The Grandma Smith CookBook is what you worship religiously. All the dishes are killer, and you cannot wait to begin the preparations. What should you make tonight?'},'kitchen.png',
[MappingObject(Lasagna, 'Makes some delicious homemade Lovers Lasagna!', [1]),
    MappingObject(Pizza, 'Break out the dough and make some savory Platonic Pizza!', [1]),
    MappingObject(Salad, 'Keep it light and whip out a Sweetheart Ceaser Salad', [1])])

Rose = Stage('Rose', {0: 'You prick your fingers trying to pick the Rose, but no flower can defeat you!'},'garden.jpeg',None, 2)

Daisy = Stage('Daisy', {0: 'A Daisy can put up little resistance to your giant hedge clippers.'},'garden.jpeg', None, 2)

Sunflower= Stage('Sunflower', {0: 'Nothing says, "I like you" like a flower as big as your face. The Sunflower you picked is a giant monster flower and you are proud of yourself'},'garden.jpeg', None, 2)

Garden = Stage('FLOWERS', {0: 'There is a beautiful flower garden in the backyard. You are obsessed with the way flowers look and have always treated them with tenderness and love. Which flower are you going to chose to use tonight? '},'garden.jpeg',
[MappingObject(Rose, 'Roses are a classic!', [1]),
    MappingObject(Daisy, 'A Daisy is simple and elegant', [1]),
    MappingObject(Sunflower,'Sunflowers are big and beautiful', [1])])

Trash = Stage('Trash', {0: 'You want to empty out the trash tonight, so everything is absolutely perfect! However, when you look into the trash can, you notice bouquets of flowers in the trash. Suddenly, you hear a noise from upstairs...'},'kitchen.png')

Kitchen = Stage('Kitchen', {0: 'Nothing screams cozy and comfy like a home cooked meal! You have been learning how to cook since you were child and am super eager to wow your date with your deliciously hypnotizing dishes!'},'kitchen.png',
[MappingObject(Cookbook, 'Check out your favorite cookbook for a recipe to cook for tonight!', [1,2]),
    MappingObject(Garden, 'Head to your garden to choose a flower for tonight!', [1,2]),
    MappingObject(Trash, 'Take out the trash so the kitchen doesn’t smell weird later', [2])])

Dishes2 = Stage('Dishes', {0: 'You have to search a little to find the right cabinets to put all the dishes in but eventually everything is away. For the love of God what is happening upstairs'},'kitchen.png')

Dishes = Stage('Dishes', {0: 'You wash and dry all of the dishes. Woo you really made a mess earleir. Sweat drips down your forehead'},'kitchen.png',
[MappingObject(Dishes2,'Put away the dishes',[0])])

Napkins = Stage('Napkins', {0: 'You fold the white napkins to look like cranes and leave one at each end of the table. Your heart is beating fast'},'kitchen.png',
[MappingObject(Dishes,'Uh oh you forgot to do the dishes!',[0])])

Polish = Stage('Polish', {0: 'This silverware is looking a little dull. Nothing a little elbow grease cannot fix! You feel like someone is watching you.'},'kitchen.png',
[MappingObject(Napkins,'Put out napkins',[0])])

LightCandles = Stage('LightCandles', {0: 'These candles really set the mood. Classy. Elegant. You hear footsteps echo from the Bedroom'},'kitchen.png',
[MappingObject(Polish,'Polish the silverware',[0])])

SetTable = Stage('SetTable', {0: 'You start to set the table for tonight. Everything has to be perfect. The FLOWERS you picked out earlier are the perfect centerpieces. You hear a door slam'},'kitchen.png',
[MappingObject(LightCandles,'Time to light some candles',[0])])

TableCloth = Stage('TableCloth', {0: 'The table cloth is floral and almost matches the plates! Did you just see a shadow coming from upstairs?'},'kitchen.png',
[MappingObject(SetTable,'Set the table',[0])])

PrepareFood = Stage('PrepareFood', {0: 'You take the DISH out of oven, and it is to die for! Well done! There is rustling noises coming from upstairs'}, 'kitchen.png',
[MappingObject(TableCloth,'Lay out a beautiful tablecloth',[0])])

EndKitchen = Stage('Kitchen', {0:'You hear a loud crashing sound from upstairs!!'}, 'kitchen.png',
[MappingObject(PrepareFood,'Get the Food out of the oven',[3,4])])

SunDress= Stage('SunDress', {0: 'What a cute Sun Dress! Yellow with pink flowers, this warm summery look will light up any room!'},'bedroom.png', None, 2)

TShirt= Stage('TShirt', {0: 'T Shirt and Jeans is just a classic Julia outfit, and why mess with a classic??'},'bedroom.png', None, 2)

PowerSuit= Stage('PowerSuit', {0: 'Go big or go home. Nothing screams confidence like a bright red suit. And the best part is it basically matches everything!'},'bedroom.png', None, 2)

OutfitMakeup = Stage('OUTFIT', {0: 'You have always loved picking out dresses, ever since you were little and you would dress up your dolls. Well tonight is the real deal and it is time to get serious about fashion. Which should you pick out for tonight?'},'bedroom.png',
[MappingObject(SunDress, 'Sun Dress', [1]),
    MappingObject(TShirt, 'T Shirt', [1]),
    MappingObject(PowerSuit,'Power Suit', [1])])

Stranger= Stage('Stranger', {0: '"Dear Diary, I saw a very Handsome Stranger the other day in the park today! He was staring right at me and his blue eyes reminded me of Steven. I sure hope Steven calls soon... -Love Julia"'},'bedroom.png')

Dreams= Stage('Dreams', {0: '"Dear Diary, I keep having the same dream over and over agian. I am sitting in my kitchen and I am having THE most amazing date with THE most handsome man. He has beautiful blue eyes... I sure hope that its foreshadowing! -Love Julia"'},'bedroom.png')

LoveLife= Stage('LoveLife', {0: '"Dear Diary, I cannot stop thinking about Steven! When we talked on the phone last week I had butterflies for hours! I sure hope he asks me on a date soon... -Love Julia"'},'bedroom.png')

Diary = Stage('Diary', {0: 'You have already read through this diary so many times you almost have it memorized. Which section do you want to reread?'},'bedroom.png',
[MappingObject(Stranger, '"I saw a very Handsome Stranger the other day...""', [1,2]),
    MappingObject(Dreams, '"I keep having the same dream..."', [1,2]),
    MappingObject(LoveLife,'"I cannot stop thinking about Steven!...""', [1,2])])

Notes = Stage('Notes', {0: 'Have those notes always been there? They are percariously stacked up on the nightstand and are spilling over onto the floor. What do you do with the notes?'},'bedroom.png')

Bedroom = Stage('Bedroom', {0: 'There is a big sign on the door that says, "Julias room". Wow this room is a mess! You better clean up if you want to impress that Special Someone. Yes you are definitly going to clean. As soon as you are done picking out a dress. Oh who are you kidding?'} ,'bedroom.png',
[MappingObject(OutfitMakeup, 'Time to choose what to wear for this special Night!', [1,2,3]),
    MappingObject(Diary, 'Take a look at the Diary!', [1,2,3]),
    MappingObject(Notes, 'You notice a stack of notes on the table', [2,3])])

Approach6 = Stage('Approach6',{0: 'You use your weapon to try to subdue her, she rams into you, and your instincts take her. You throw her against the wall. There is a loud cracking noise and her head is tilted at a weird angle. You shake her a couple times, but she is unconscious.'},'bedroom.png',
[MappingObject(Approach6,'SHE IS RUINING EVERYTHING!',[0]),
MappingObject(Approach6,'WHY IS SHE BEING SUCH A BITCH!',[0]),
MappingObject(Approach6,'Stay rational',[0])])

Approach5 = Stage('Approach5',{0: 'She manages to dodge your hug and scratches you on the cheek. You see her looking for an escape.'},'bedroom.png',
[MappingObject(Approach6,'SHE IS RUINING EVERYTHING!',[0]),
MappingObject(Approach6,'WHY IS SHE BEING SUCH A BITCH!',[0]),
MappingObject(Approach6,'Stay rational',[0])])

Approach4 = Stage('Approach4',{0: 'She manages to dodge your hug and scratches you on the cheek. You see her looking for an escape.'},'bedroom.png',
[MappingObject(Approach5,'SHE IS RUINING EVERYTHING!',[0]),
MappingObject(Approach5,'WHY IS SHE BEING SUCH A BITCH!',[0]),
MappingObject(Approach5,'Stay rational',[0])])

Approach3 = Stage('Approach3',{0: 'You say, "But Julia, this is OUR house. I cannot leave. I am still not done preparing for our perfect date, and you did not even put on the OUTFIT I put out for you. If you don\'t calm down, I will have to put you back into the closet."'},'bedroom.png',
[MappingObject(Approach4,'Hug it out',[0])])

Approach2 = Stage('Approach2',{0: 'She screams, "GET...OUT...OF...MY HOUSE!!!" You are very confused at this point.'},'bedroom.png',
[MappingObject(Approach3,'Threaten her to calm down',[0])])

Approach = Stage('Approach',{0: 'She says "...CRAZY...FLOWERS...GET OUT, LEAVE ME ALONE". She does not know whats happening. She needs to be calmed down'},'bedroom.png',
[MappingObject(Approach2,'Force her to calm down',[0]),
MappingObject(Approach2,'"WHAT ARE YOU DOING HERE?"',[0])])

Corner = Stage('Corner',{0: 'She mumbles something under her breath and backs away from you into a corner of the room'},'bedroom.png',
[MappingObject(Approach,'Calm her down',[0]),
MappingObject(Approach,'"What Are You Doing Here?"',[0])])

EndBedroom = Stage('Bedroom', {0:'She is staggering out of the closet. What is she doing here?'} ,'bedroom.png',
[MappingObject(Corner,'Try and calm her down',[0]),
MappingObject(Corner, 'Stay still',[0]),
MappingObject(Corner,'"What are you doing here?"',[0])])

Hallway = Stage('Hallway', {1: 'Where do you want to go',2: 'Where do you want to go', 3: 'The oven timer is going off! Time to go check on your DISH.', 4: 'Where do you want to go'}, 'livingroom.png', [MappingObject(Kitchen, 'Go downstairs to the kitchen!', [1,2]),
    MappingObject(Bedroom, 'Go upstairs to the bedroom!', [1,2,3]),
    MappingObject(EndKitchen,'Go downstairs to the kitchen!',[3,4]),
    MappingObject(EndBedroom,'Go upstairs to the bedroom!',[4])])

Intro2 = Stage('Intro2', {0 : 'She comes every monday to drop off groceries, but she never stays long. Anyways time to get ready! Tonight is a big night!'},'livingroom.png',
[MappingObject(Hallway, 'Start the preparations!', [0])])

Intro = Stage('Intro', {0 : 'You finish washing your hands and shoot yourself a smile in the mirror. You hear a voice from downstairs, "Goodmorning Julia! Are you still in bed, you sleepy head. I brought you some groceries to start your week! Anyways, love you sweetheart. Call your mom soon, I miss you"'},'livingroom.png', [MappingObject(Intro2, 'Aww so cute', [0])])

StartingPage = Stage('Start', {0 : 'The Perfect Date: Ever wanted to bring your dream date to reality?'},'livingroom.png', [MappingObject(Intro, 'Start Game', [0])])

Cookbook.back = Kitchen
Garden.back = Kitchen

Lasagna.back = Cookbook
Salad.back = Cookbook
Pizza.back = Cookbook

Rose.back = Garden
Daisy.back = Garden
Sunflower.back = Garden

Trash.back = Kitchen

Kitchen.back = Hallway


OutfitMakeup.back = Bedroom
Diary.back = Bedroom

SunDress.back = OutfitMakeup
TShirt.back = OutfitMakeup
PowerSuit.back = OutfitMakeup

Stranger.back = Diary
Dreams.back= Diary
LoveLife.back= Diary

Notes.back = Bedroom

Bedroom.back = Hallway

EndBedroom.back = Hallway

EndKitchen.back = Hallway
PrepareFood.back = Hallway
TableCloth.back = Hallway
SetTable.back = Hallway
LightCandles.back = Hallway
Polish.back = Hallway
Napkins.back = Hallway
Dishes.back = Hallway
Dishes2.back = Hallway

stageList = [Lasagna,Salad,Pizza,Rose,Daisy,Sunflower,Trash,Kitchen,SunDress,TShirt,PowerSuit,Stranger,Dreams,LoveLife,Diary,Notes,Bedroom,EndKitchen,PrepareFood,SetTable,TableCloth,LightCandles,Polish,Napkins,Dishes,Dishes2]

def backButtonGen (stage):
    backButton = MappingObject(goBack(stage),'Go back to the ' + str(goBack(stage).name),[0],True)
    if stage.buttonMapping != None:
        stage.buttonMapping.append(backButton)
    else:
        stage.buttonMapping = [backButton]

def allBackButtonGen (stageList):
    for stage in stageList:
        backButtonGen(stage)

allBackButtonGen(stageList)

def levelConditions(state,stage):
    if state.level == 1 and Diary.clicked and OutfitMakeup.clicked and Garden.clicked and Cookbook.clicked:
        state.level = 2 #Trash and Notes appear
    elif state.level == 2 and Trash.clicked and Notes.clicked:
            state.level = 3 #Oven goes off in Hallway
    elif state.level == 3 and EndKitchen.clicked:
        state.level =4 #Sound is heard in the kithen
