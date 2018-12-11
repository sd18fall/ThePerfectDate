
# Architectural Review 2: Reflection & Synthesis
### Sabrina, Sophie, Cynthia

For this review, we really wanted to focus on getting feedback on the structure of our game. Specifically, on how to store and display our game data onto the screen. After reviewing our design with the class, the feedback we received was that the organization seemed clear and practical. In terms of storing our data, some students suggested that we create a dictionary that stored whether the user has completed specific parts of the game or not. This will be useful when certain things pop up only after the user has reached a certain point. Moving forward, we plan on continuing to flush out the data into model, viewer, and controller to get the different pieces successfully interacting with one another. We will also implement more user experience suggestions provided by the class.

Several ideas from the last Architecture Review:

1. **Having a character image appear next to the text:** emotionally connects the player to the character and makes the game more interesting to play
2. **Adding random chance:** this makes the game more attractive because users can play it multiple times without achieving the same result. They can also be surprised in multiple ways.
3. **Adding an inventory:** allows the player to see artifacts they have already seen and allows us to remove the artifacts from rooms after they have seen them, narrowing their choices for things to investigate and pushing the plot forward
4. **Adding a map:** makes the game and locations more visual, connecting the player to the world we have created more
5. **Having all past actions matter instead of just the most recent decision:** makes the game more personalized and more fun to replay

We did not really get a chance to implement these ideas, although we have been building our plot and code around the ideas of adding them eventually. Hopefully we will get around to adding some of them this week. Several of these changes will be fairly easy now that we have our MVP accomplished, like adding a map or having a character image appear next to the text, but we hope to focus on adding random chance and having past decisions matter in the following week. Specifically the idea of having past decisions affect future decisions was brought but several times in the focus groups and is important to where we want our game to be going. This is also a good idea to focus on because it is involved in both the plot and coding aspects of the game.

For this review, we changed the way in which we talked about our architecture to follow the Model-View-Controller layout, making more sense of which classes and function fall under which area. Our audience seemed to better understand our code layout compared to last time, and asked questions about each section that we could properly answer with the graphical representation of the structure. We also showed them a demonstration of our MVP, and compared to the last review, they seemed to really understand what our game should look like.

We also took an idea from a team from the previous architecture review to engage more with the audience and have a more intimate conversation by breaking off into smaller groups and having discussions about the questions we were asking. We found it to be a more natural way to listen to the ideas they had, and people often would echo in agreement or add their own ideas after hearing what other had said. For a more effective technical review, we could add key short sections of codes to better explain portions of our structure.
