import pygame

class Ship():
	def __init__(self, ai_settings, screen):
		"""initialise ship and set start position"""
		self.screen = screen
		self.ai_settings = ai_settings

		#load ship image and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#start each new ship at the bottom centre of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#store a decimal value for ship centre
		self.center = float(self.rect.centerx)

		#movement flags
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""update ship's position based on movement flag"""
		#update ship's centre value, not the rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		#update rect centre from self.center
		self.rect.centerx = self.center

	def blitme(self):
		"""draw ship at current location"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""move ship to centre of screen after being killed"""
		self.rect.centerx = self.screen_rect.centerx
