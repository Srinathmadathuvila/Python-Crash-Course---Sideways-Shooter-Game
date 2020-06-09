
class Settings():

	""" A class to store all the settings for 
	Sideways shooter"""

	def __init__(self):
		""" Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (000,000,000)

		# bullets settings
		self.bullet_speed_factor = 1
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (250,60,60)
		self.bullets_allowed = 4


