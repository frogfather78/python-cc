class Settings():
	"""to store all the setting for Alien Invasion"""

	def __init__(self):
		"""initialise game settings"""
		#screen settings
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_colour = (0, 0, 255)

		#ship settings
		self.ship_speed_factor = 1.5
		self.ship_limit = 3

		#alien settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		#fleet_direction of 1 means go right, -1 means go left
		self.fleet_direction = 1

		#bullet settings
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_colour = (60, 60, 60)
		self.bullets_allowed = 3
