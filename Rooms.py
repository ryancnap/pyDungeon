from Player import PlayerClass

class RoomManager(object):


	"""Used to manage rooms, create and populate them."""
	def __init__(self, description = "", exits = {}, enemies = [],
				treasure = [], long_description = ""):
		super(RoomManager, self).__init__()
		self.description = description
		self.exits = exits
		self.enemies = enemies
		self.treasure = treasure
		self.long_description = long_description

		self.special = False

	def _has_exits(self):

		"""Helper method for _exit_maker()"""

		if len(self.exits) != 0: return True
		else: return False


	def _exit_choice(self):

		if self._has_exits():
			print('---You see the following means of exit: ---')

			# Print a list of the room's exits which are assigned
			# in the RoomManager constructor.
			print('\n{0}\n').format(' \n'.join([k for k in self.exits.iterkeys()]))

			# The key in the *exits* dict is a description of the exit;
			# the value should be the RoomManager instance it links to.
			player_exit_choice = raw_input('Where would you like to go?')

			# Throw the *player_choice* string back to the move() method
			# The logic for moving between rooms and making decisions should
			# be handled by the method that's responsible for moving :)
			return player_exit_choice




	def show_treasure(self):

		"""Prints room's treasure list. This method is validated by the *_has_treasure* method."""

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

		""" Normal scenario for handling enemies in a room.
		"""

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

	def set_special(self, has_special):

		""" Used to set the *special* attribute of the room instance to
			trigger special events; room.play_special_event()
		"""
		if has_special == True:
			self.special = True

	def play_special_scenario(self):
		raise NotImplementedError

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

	# The big boy.
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
			if self._has_exits():
				print('<-move-> Move to the next room')
			elif not self._has_exits():
				print('<-go back-> Return to the next room')

			player_decision = raw_input('\n')
			player_decision.lower()


			if player_decision == 'i':
				PlayerClass().inventory_manager(self)

			if player_decision == 's':
				print(PlayerClass().stats)

			if player_decision == 'take':
				PlayerClass().inventory_adder(self)


			if player_decision == 'explore':
				print(self.long_description)

			if player_decision == 'move' and self.special == False:
				# First break out of the input loop by saying the player has
				# now moved and this room's decision logic can end.
				player_hasnt_moved = False

				# Run RoomManager's exit choice method to prompt the player
				# which exit to choose.
				exit = self._exit_choice()

				# The provided string should match the key in the
				# current room instance's *exits* dict.
				if exit in self.exits.keys():

					# Reassign *exit* to be the key's value.
					exit = self.exits[exit]

					# This is why RoomManager's *exits* attribute is a
					# dictionary; each exit(key) maps to a different
					# RoomManager instance(value).
					# Keepin' it seperable baby;)
					PlayerClass().move(exit)
			elif player_decision == 'move' and self.special == True:
				raise NotImplementedError
				# Call a room instance's play_special_event() method.
				self.play_special_event()


