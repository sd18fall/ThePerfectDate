from Model import *



Seven = Stage('Seven',{0: 'Scrolling text that emerses you in the story'},'bedroom.png',
[MappingObject(Seven,'I have never been so emersed until this day',[0])])

Six = Stage('Six',{0: 'Scrolling text that emerses you in the story'},'bedroom.png',
[MappingObject(Seven,'I have never been so emersed until this day',[0])])

Five = Stage('Five',{0: 'And cute little icons to show what is in your inventory! Here, take a sunflower'},'bedroom.png',
[MappingObject(Six,'Wow a sunflower icon!',[0])],1,'sunflower.png')

Four = Stage('Four',{0: 'Scrolling text that emerses you in the story'},'bedroom.png',
[MappingObject(Five,'I have never been so emersed until this day',[0])])

Three = Stage('Three',{0: 'It comes with many features such as buttons that you can click'},'bedroom.png',
[MappingObject(Four,'Look at this button! It takes you to a new screen!',[0])])

Two = Stage('Two',{0: 'Welcome to The Perfect Date! The only video game where you can '},'bedroom.png',
[MappingObject(Three,'',[0])])

One = Stage('One',{0: 'Have you ever been unhappy with your love life? Have your past dates disapointed? Well, do we have the game for you!'},'bedroom.png',
[MappingObject(Two,'What is it?',[0]),MappingObject(Two,'Nah, I want to die alone',[0])])
