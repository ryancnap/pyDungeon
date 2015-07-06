from Player import PlayerClass

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
			if self.exits > 0:
				print('<-move-> Move to the next room')
			elif self.exits == 0:
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

			if player_decision == 'move':
				# TODO: Call move() to go to next room
				player_hasnt_moved = False