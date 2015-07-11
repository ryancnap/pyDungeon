from Player import PlayerClass
from NPC import NPCCreator
from Rooms import RoomManager

# Global list variable room_list
# room_list = {'Entrance' : entrance.}


# Create a player named Ryan, and an NPC named John.
ryan = PlayerClass()
john = NPCCreator()

# There's a little bit of strange mess here with the way I implemented
# NPCCreator; need to set the .name property manually instead of with
# a named instance parameter.
john.name = 'john'

# Get the dialogue options first before running the main game.
# The process involves opening a file handle, iterating through the lines,
# and concatenating said lines to a string, which then gets returned to our
# NPCCreator instance *john*.
# For performance reasons I'd like to do it once, here.
john.get_dialogue_options()

# Create three rooms.
# RoomManager instances are created with a mix of
# mandatory and named (optional) instance paramaters. The class signature
# looks like:
# (self, description = "", exits = {}, enemies = [],
# treasure = [], long_description = "")
# For the style of this project, and since constructors are already quite
# long, the appropriate way to assign long description attribute is after
# the instantiation of a RoomManager object.

small_cove = RoomManager('Small Cove', exits = {}, enemies = ['Bootguard'],
 treasure = ['Thirsty Boot', 'Clock'])

cave = RoomManager('Gloomy Cave', exits = {'oak portcullis': 1}, enemies = ['Aggro Lizard'],
 treasure = ['Another watch'])

# The following line dealing with special features to rooms is not fully
# implemented yet. If a room instance's *special* attribute is set to True,
# the room's decision_handler will automatically play a special scenario AFTER
# the player has chosen to move from the room. That logic works fine, however
# can't figure out yet how to robustly/neatly define unique code structures
# for certain instance objects, aside from importing a separate room file
# (*.py) and immediaely running it. This would be done in much the same
# way as a DialogueManager.DialogueManager() -style import, so we should
# inherit from that to keep things DRY around here.
# Are inline imports bad form?
# Response to myself after a couple minutes on google: ^ hell yes they're bad,
# think of a better implementation instead of designing this like a fool!
cave.set_special(True)

entrance = RoomManager('Entrance', exits = {'dusty door': cave, 'hole': small_cove}, treasure = ['Pile of gold'])


# Test that NPCCreator instance john can speak; ie, we can use the
# string of text that we read in from the john NPC's dialogue.txt file
# and print it to the screen.
john.speak()

# Assign a couple of random rooms a *long description* property.
# These are left empty by default to simplify RoomManager constructors.
# The class contains logic to deal with the string being left empty.
# The *long description property is a string which will be printed if
# the user chooses the 'Look Around/Explore' option in the room.
small_cove.long_description = 'There seems to be a body in the corner'
cave.long_description = 'Swing town'

# Until the method is refactored, it must be called manually with the instance
# of RoomManager rooms as it's first and only argument.
# Move through the three rooms we created above.
# IMPORTANT: This method now only exists here for testing purposes,
# and because I've been generally lazy.
# Player instance's move() method is now called from within the RoomManager
# instance; alot of other sexy magic goes on with RoomManager helper methods,
# but ultimately move() is called after the player has been presented with a
# list of options in the form of exits to rooms; the exits are instantiated
# in RoomManager constructors as dictionaries, where keys are user-facing
# exit names and values are RoomManager instances that said exits lead to.
ryan.move(entrance)
#ryan.move(small_cove)
#ryan.move(cave)