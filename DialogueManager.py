

class DialogueManager(object):


	""" Class responsible for taking the name of an npc and
		presenting dialog options to the player.
	"""

	def init(self, npc_name):

		""" Takes an NPC name from the NPC.pyc module, and uses the
			options defined there to open a file with that npc's dialogue.
		"""
		self.npc_name = npc_name

	def get_dialogue(self, file_path):

		""" Takes an NPC name (string) from NPCCreator in NPC module,
			where this method is called from. The name is suffixed with
			.txt string in the NPCCreator instance (which is called from Main)
			so DialogueManager's NPC-specific instance can find it's dialogue
			file on the system using the name of the NPC.
		"""

		# Possible problems: can't have NPC's with more than one name;
		# maybe I could make a NPCNameFormatter method in the NPCCreator
		# that's responsible for stripping a leading id number off the NPC
		# name string before displaying it to the user; the id could be the
		# room the NPC belongs to.
		#
		# This way the system could identify where the NPC should be placed,
		# via room id, and run a quick strip method on it's name string to
		# display only the NPC's real name. ie, we could have spooky_cave_John,
		# and secret_grotto_John, while the player will simply be in the
		# Secret Cave room talking to 'John'.

		self.file_path = file_path
		self.dialogue_directory = 'dialogue/' + file_path
		# Empty string will eventually have contents of dialogue file appended
		# to it; it will be returned to an NPCCreator instance as a string
		# named *speech*.
		self.file_contents = ''

		with open(self.dialogue_directory, 'r') as file_handle:
			for line in file_handle:
				# TODO: string concatenation is slow.
				# Find a better way to do this, slob.
				self.file_contents += line

			file_handle.close()
		# Pass the contents of the file back to the caller.
		# The caller in this case is an NPCCreator instance. The class method
		# will take the file contents as a string variable named speech,
		# and pass them onto NPCCreators speak() method to be printed out.
		return self.file_contents

