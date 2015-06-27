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

		""" Takes room instance; responsible for moving when there
			are multiple exits.
		"""
		print('\n---You enter the next room.---')
		print('This is the {0}.'.format(Room.description))

		Room.scenario_initiator()
		Room.decision_handler()

	def inventory_adder(self, room):

		""" Only responsible for adding items to inventory.
			Needs room instance as an argument so we can
			accept the specific room's list of treasure.
		"""

		if not room._has_treasure():
			print('There doesn\'t seem to be any more loot here.')

		if room._has_treasure():
			for item in room.treasure:
				print('*Added {0} to inventory*'.format(item))
				self.inventory[item] = ''
				room.treasure = []

	def inventory_manager(self, room):

		""" Shows inventory to player. Gives option to drop an item
			by typing the exact item name. Needs room instance so
			we can drop specified items in whichever room we're
			currently in.
		"""

		done_with_inventory = False

		while not done_with_inventory:

			print('\n---INVENTORY---')
			print('<-item-> Drop specified item.')
			print('<-exit-> Exit inventory manager\n')

			for item, description in enumerate(self.inventory):
				print(description)

			choice = raw_input('> ')
			if choice == 'exit':
				done_with_inventory = True

			elif choice not in self.inventory:
				print('You don\'t have a {0}\n'.format(choice))

			elif choice in self.inventory:
				del self.inventory[choice]
				room.treasure.append(choice)
				print('*You dropped the {0}*\n'.format(choice))



class RoomManager(object):


	"""Used to manage rooms, create and populate them."""
	def __init__(self, description = "", exits = 1, enemies = [],
				treasure = [], long_description = ""):
		super(RoomManager, self).__init__()
		self.description = description
		self.exits = exits
		self.enemies = enemies
		self.treasure = treasure
		self.long_description = long_description

		self.player_entered_inventory = None

	def show_treasure(self):

		"""Prints room's treasure list. This method is validated by the *_has_treasure* method."""
		if not self.player_entered_inventory:
			print('This room has some treasure in it: ')

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
			print('Doesn\'t seem to be anything around...')
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

	def decision_handler(self):

		"""Handles the room's logic, where the player wants to go, etc."""


		player_hasnt_moved = True
		while player_hasnt_moved:

			print('\n---What would you like to do?---')
			print('<-i View inventory->  '),
			print('<-s Show stats->  \n')

			if self._has_treasure():
				print('<-take-> Take the treasure')
			if self.long_description != "":
				print('<-explore-> Look around the {0}'.format(self.description))
			if self.player_entered_inventory and self._has_treasure():
				print('<-look-> What\'s dropped on the floor?')
			if self.exits > 0:
				print('<-move-> Move to the next room')
			if self.exits == 0:
				print('<-go back-> Return to the next room')

			player_decision = raw_input('\n')
			player_decision.lower()

			if player_decision == 'i':
				self.player_entered_inventory = True
				Ryan.inventory_manager(self)

			if player_decision == 's':
				print(Ryan.stats)

			if player_decision == 'take':
				Ryan.inventory_adder(self)

			if player_decision == 'look' and self._has_treasure():
				print('Just some junk: ')
				self.show_treasure()

			if player_decision == 'explore':
				print(self.long_description)

			if player_decision == 'move':
				# TODO: Call move() to go to next room
				player_hasnt_moved = False



# Set up a player character
Ryan = PlayerClass()

# Make some rooms with enemies and treasure!
entrance = RoomManager('Entrance', 1, treasure = ['Pile of gold'])
cave = RoomManager('Gloomy Cave', 3, enemies = ['Aggro Lizard'], treasure = ['Another watch'])
small_cove = RoomManager('Small Cove', 0, enemies = ['Bootguard'], treasure = ['Thirsty Boot', 'Clock'])

small_cove.long_description = 'There seems to be a body in the corner'
cave.long_description = 'Swing town'
# Move the player to the entrance room and start the game.
Ryan.move(entrance)
Ryan.move(small_cove)
Ryan.move(cave)







