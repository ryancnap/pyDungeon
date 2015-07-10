

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

		#exit_choice = Room.exit_choice()
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