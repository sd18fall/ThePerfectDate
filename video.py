from Model import *

Ten = Stage('Nine',{0: 'What are we waiting for? Let\'s go see what it is like to get ready for your perfect date!'},'kitchen.png')

Nine = Stage('Nine',{0: 'Let\'s go see what it is like to get ready for your perfect date!'},'kitchen.png',[MappingObject(Ten,'Well alright then!!',[0])])

Eight = Stage('Eight',{0: 'Hm what about the kitchen? Don\'t you want to see that too?'},'bedroom.png',[MappingObject('Nine','Check out the kitchen!',[0]), MappingObject(Nine,'Go to the kitchen!',[0])])

Seven = Stage('Seven',{0: 'You can explore the house for however long you want!'},'bedroom.png',
[MappingObject('Eight','Go to the bedroom!',[0]), MappingObject(Nine,'Go to the kitchen!',[0])])

Six = Stage('Six',{0: 'Look! A sunflower has been added to your inventory! OOOoOOOoo AAAaAaaaAhhhhH'},'bedroom.png',
[MappingObject(Seven,'I will treasure it forever',[0])],1,'sunflower.png')

Five = Stage('Five',{0: 'And cute little icons to show what is in your inventory! Here, take a sunflower for good luck.'},'bedroom.png',
[MappingObject(Six,'Enthusiastically take the sunflower!',[0])])

Four = Stage('Four',{0: 'It also comes with scrolling text that emerses you in the story. Look at this text scroooollllll scroll scroll scrooollll wweeeeee wooooo yyyaaaaayyyy'},'bedroom.png',
[MappingObject(Five,'I have never been so emersed until this day',[0])])

Three = Stage('Three',{0: 'It comes with many amazing features such as pretty buttons that you can click! These buttons help you move along through the story and are your only form of navigation.'},'bedroom.png',
[MappingObject(Four,'Look at this button! It takes you to a new screen!',[0])])

Two = Stage('Two',{0: 'Welcome to The Perfect Date! A one of a kind video game that allows you to bring your dream date to reality through personalization! '},'bedroom.png',
[MappingObject(Three,'OMG. AMAZING. How do I play?',[0])])

One = Stage('One',{0: 'Have you ever been unhappy with your love life? Have your past dates disapointed you? Well, do we have the perfect game for you!'},'bedroom.png',
[MappingObject(Two,'YES AND YES.',[0]),MappingObject(Two,'Nah, I want to be alone for the rest of my life.',[0])])

Zero = Stage('Zero', {0 : ''},'TitleScreen.png', [MappingObject(One, 'Start', [0])])
