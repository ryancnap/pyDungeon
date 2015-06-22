""" Simple dungeon explorer.
	Created by Ryan Camaratta <ryancnap@gmail.com> Copyright 2015.
	A fun(?) take on a very simplistic dungeon explorer, with not-so-many
	decisions for exploring, and rather dull dungeons.
	Mainly created for me to practice my OOP and inventory systems.

	Licensed under the GNU GPL. See LICENSE.txt for details.
"""


class PlayerClass(object):


	"""Simple class for player characters to inherit"""
	def __init__(self, stats = {}, inventory = {}):
		super(PlayerClass, self).__init__()
		self.stats = {
			'Vitality' : 10,
			'Defense' : 15,
			'Agility' : 1,
			'Alacrity': 5
		}

		self.inventory = {
			'Iron Sword' : 'A nicked-up beater sword.',
			'HP+' : 'A health potion which raises vitality.',
			'Watch' : 'Used for telling time, among other things.'
		}

	def move(self, Room, exit = 0):

		print "You enter the next room.\n"
		print "This is the {0}.".format(Room.description)
		Room.scenario_initiator()


class CreateRoom(object):


	"""Used to manage rooms, create and populate them."""
	def __init__(self, description = "", exits = 1, enemies = [], treasure = []):
		super(CreateRoom, self).__init__()
		self.description = description
		self.exits = exits
		self.enemies = enemies
		self.treasure = treasure

	def show_treasure(self):

		"""Prints room's treasure list. This method is validated by the *_has_treasure* method."""

		print 'This room has some treasure in it: '
		for treasure in self.treasure:
			print('   * {0}'.format(treasure))

	def _has_enemies(self):

		if self.enemies != []:
			return True
		else:
			return False

	def _has_treasure(self):

		if self.treasure != []:
			return True
		else:
			return False

	def play_enemy_scenario(self):

		"""Scenario for handling enemies in a room."""

		if len(self.enemies) > 1 and len(self.enemies) > 0:
			# Implement more-than-one-enemy logic.
			print('More than one enemy.')
			pass
		elif len(self.enemies) <= 1 and len(self.enemies) > 0:
			# Implement one on one logic.
			print('Just one enemy.')
			pass
		else:
			# Handle room events.
			print('No enemies.')
			pass

	def scenario_initiator(self):

		"""Checks for room content (treasure/enemies) to figure out how best to proceed. """

		# Check for enemies.
		if not self._has_enemies():
			pass
		else:
			self.play_enemy_scenario()

		# Check for treasure.
		if not self._has_treasure():
			pass
		else:
			self.show_treasure()



# Set up a player character
Ryan = PlayerClass()

# Make some rooms with enemies and treasure!
entrance = CreateRoom('Entrance', 1, enemies = [], treasure = ['Pile of gold'])
cave = CreateRoom('Gloomy Cave', 3, enemies = ['Aggro Lizard'], treasure = ['Another watch'])
small_cove = CreateRoom('Small Cove', 1, enemies = ['Bootguard'], treasure = ['Thirsty Boot', 'Clock'])

# Move the player to the entrance room and start the game.
# Is the *move* method doing too much work? Does it know too much? What are the external
# requirements for *move* to do its job correctly?
Ryan.move(entrance)
Ryan.move(small_cove)







