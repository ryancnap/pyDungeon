from DialogueManager import DialogueManager


class NPCCreator(object):


	""" Responsible for creating arbitrarily-defined (read, use-once) NPC's.
	"""

	def init(self, name, inventory = {}):

		self.name = name
		self.inventory = inventory
		self.speech = speech
		#self.dialogue_file = dialogue_file


	def get_dialogue_options(self):

		# No idea why I have to put this down here instead of in the constructor.
		dialogue_file = self.name + '.txt'

		# On the first line we create an instance of DialogueManager to
		# the NPC's dialogue attribute, then give it a name that we passed into it
		# at creation time in the main game file.
		dialogue = DialogueManager()
		dialogue.npc_name = self.name

		# Note that the DialogueManager's get_dialogue_options method uses the name
		# of the npc to look up a file with that npc's text dialogue.
		self.speech = dialogue.get_dialogue(dialogue_file)

	def speak(self):
		print(self.speech)

