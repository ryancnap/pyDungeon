# pyDungeon
Text-based dungeon crawler written in Python 3.

Haven't decided whether this should be a pick-your-exit kind of game,
or just a linear crawl; the former would challenge me from a design perspective, 
the latter would challenge me from a creative (content-wise) perspective.

Right now it's linear. This might transition to pygame once I get more of the skeleton 
built: I'm thinking about throwing some Tiled .tmx maps as attributes to the rooms, 
a couple display options to the RoomManager, and some (poorly) animated sprites to 
the PlayerClass and NPCCreator constructors; add in a stack of room IDs and some pygame
event listeners for Player's move() method, and you got yourself a 2D dungeon-crawl!

But all that's in the future for now:) 
