
[Meet the Team!](index2.md)

### Table of Contents:

[Idea Formation](#how-it-all-started)

[Meet the Team](#meet-the-team)

[Code Progress & Architecture](#code-progress-and-architecture)

[How to Play](#how-to-play)

[FAQ](#faq)

[Special Thanks](#special-thanks-to)

&nbsp;

### CHECK US OUT:
![]()

# how it all started

We are three college students, 2 from Olin College of Engineering and 1 from Babson College that are working together on a final class project! Upon brainstorming, we instantly fell in love with the idea of a text- based video game. With different learning goals in mind, we set out on an adventurous journey to see what we can do with python to bring this fantastic video game to life!

&nbsp;

### meet the team

## Sabrina Pereira

<img src="https://github.com/sd18fall/ThePerfectDate/blob/master/docs/sab.jpg" width="150" height="150" />

Sabrina is a huge fan of turtlenecks and Shakira. She wakes up looking like she just put on make up. She likes... videogames? And this is kind of off topic but she does not get why people like spicy food when it just burns their mouths HOWEVER she really likes sour food. One day she is going to finally be happy, and it will be a good day.

## Sophie Schaffer

<img src="https://github.com/sd18fall/ThePerfectDate/blob/master/docs/sophie.jpg" width="150" height="150" />

Sophie is a lover of raspberries and musicals. She likes to work on finicky graphics problems and is annoyed at how long the town hall meeting is going. All she wants to do right now is eat some chocolate and take a nap

## Cynthia Yong

<img src="https://github.com/sd18fall/ThePerfectDate/blob/master/docs/cyn.jpg" width="150" height="150" />

Cynthia is an avid fan of fresh smelling candles and organic hair products. She loves practicing yoga and going hiking during her free time. Her ultimate goal is to eventually grow her own food and be an incredible plant mom!

&nbsp;

# code progress and architecture

## In the beginning...



Our code is divided into 3 different sections:

**MODEL**

This file contains all the critical classes that provide information to the Viewer and Controller file so the game can be displayed.

| CLASSES & FUNCTIONS 	| WHAT IT DOES                                                                                                        	|
|:---------------------	|:---------------------------------------------------------------------------------------------------------------------	|
| Stage Class         	| Stores information about the rooms/screens that will be used to generate the visuals                                	|
| State Class         	| Stores information about player progress to advance plot                                                            	|
| MappingObject Class 	| This links screens to one another. It contains the text for the buttons on the screen and the stages that come next 	|
| Decision Functions  	| Series of functions that allow the player's choices to affect what part of the game they will be shown.             	|

&nbsp;

**VIEWER & CONTROLLER**

This file has the classes and functions that form the graphics of our game.

| CLASSES & FUNCTIONS  	 | WHAT IT DOES                                                                                                                                                      	|
|:---------------------- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Textbox Class        	 | This is used to display the plot descriptions onto the screen                                                                                                     	|
| Button Class         	 | This class inherits from the Textbox class and is used to display interactive buttons onto the screen                                                             	|
| Screen Class         	 | This class takes information from a Stage and State object. It can then store and generate textboxes,buttons and a background to be displayed for the user to see 	|
| Controller Functions 	 |  This section contains a series of functions that detect user mouse interactivity with the game and decides what should be done with the option selected           	|

&nbsp;

**GAME DATA**

This file stores all of our game data so the game can be personalized. The first two are essentially the blue print and this forms our actual game. It contains mainly all of the *stage* classes from Model.


&nbsp;

# how to play

To get started, please download:

#### PYGAME: This is needed so the game display can be generated.

```
pip install pygame
```

To **PLAY**, please run:

```
python3 ViewerandController.py
```

&nbsp;

# faq

**Q**: Are there multiple endings?

**A**: Yes! Depending on the options you select!

&nbsp;

**Q**: How long is the game?

**A**: ~ 10 - 15 minutes

&nbsp;

**Q**: Is it fun?

**A**: OF COURSE! DUH.

&nbsp;

**Q**: Will it require a lot of skill to play?

**A**: Nope! It's a text-based game, so you mostly read what is displayed and click on buttons with your mouse to proceed forward.

&nbsp;

# special thanks to

TBD

&nbsp;
## NOT INTENDED FOR THE EASILY DISTURBED.
