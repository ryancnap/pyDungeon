from Player import PlayerClass
from NPC import NPCCreator
from Rooms import RoomManager

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
# (self, description = "", exits = 1, enemies = [],
# treasure = [], long_description = "")
entrance = RoomManager('Entrance', 1, treasure = ['Pile of gold'])

cave = RoomManager('Gloomy Cave', 3, enemies = ['Aggro Lizard'],
 treasure = ['Another watch'])

small_cove = RoomManager('Small Cove', 0, enemies = ['Bootguard'],
 treasure = ['Thirsty Boot', 'Clock'])

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

# The move function will eventually work on a stack of rooms, or might be
# implemented as a two-dimensional array, and will accept an id along with
# the number of exits to the RoomManager instance it's called from, to
# determine where the user can move and where each exit leads.
#
# Until the method is refactored, it must be called manually with the instance
# of RoomManager rooms as it's first and only argument.
# Move through the three rooms we created above.
ryan.move(entrance)
ryan.move(small_cove)
ryan.move(cave)