class Settings():
	"""to store all the setting for Alien Invasion"""

	def __init__(self):
		"""initialise game static settings"""
		#screen settings
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_colour = (0, 0, 255)

		#ship settings

		self.ship_limit = 2


		#alien settings

		#how quickly the game speeds up
		self.speedup_scale = 1.1

		#bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_colour = (60, 60, 60)
		self.bullets_allowed = 3

		self.initialise_dynamic_settings()

	def initialise_dynamic_settings(self):
		"""initialise settings that change during the game"""
		self.bullet_speed_factor = 3

		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		self.ship_speed_factor = 1.5
		#fleet_direction of 1 means go right, -1 means go left
		self.fleet_direction = 1
		#scoring
		self.alien_points = 50
		self.score_scale = 1.5

	def increase_speed(self):
		"""increase speed settings and alien point values"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		
