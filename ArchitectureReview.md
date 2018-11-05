# Architectural Review - MetaVideoGame
### By: Sabrina, Sophie, Cynthia

We are creating a “meta” video game. A meta video game is a type of game that leads the player to believe in a certain outcome throughout the game, but surprises the player at the end with a completely different outcome that also fits the game plot. 
The MVP will consist of buttons that players select and generated text to help move the plot further once the buttons are clicked. 

The **structural architecture** roughly includes: 
1. TextBox class: displays storyline text onto the screen
2. Button class: inherits from TextBox class to generate clickable buttons
3. Artifacts class (still developing): stores information of literal objects (diary, towel, etc.) that the user will interact with
4. Display Function: clears previous screen and displays several text boxes and buttons
Room Dictionary: 
   -Key: Room buttons
   -Values: Screens of what is in the room
5. Artifact Dictionary: 
   -Key: Literal item (diary, towel, etc.)
   -Values: Text to describe the item to help the player understand the situation and move plot forward

### QUESTIONS:
1. What are your thoughts on how to best store our storyline data?
2. What do you think of our textbox and button class? What other classes do you think would be useful?
3. What do you look for in a story game?
4. Do you have any thoughts on how to balance plot line and technical complexity?
5. Any general advice/ things to watch out for in game development?


### AGENDA: (15 minute total)

Intro (4 min): Explain project concept with illustrations

Concepts and Background (6 min): Explain software architecture & propose potentials questions and risks 

Questions & Feedback (5 min): Fill out survey & clarify questions about presented information

**Feedback Form Link:** https://goo.gl/forms/PYP9663v4fD1KaQA3

