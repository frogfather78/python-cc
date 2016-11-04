import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from ship"""
	
	def __init__(self, ai_settings, screen, ship):
		"""create a bullet object at the ship's current position"""
		super().__init__()
		self.screen = screen
		
		#create bullet rect at (0,0) the set correct position
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
			ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#store bullet's position as decimal value
		self.y = float(self.rect.y)
		
		self.colour = ai_settings.bullet_colour
		
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		"""move bullet up the screen"""
		#update decimal position of bullet
		self.y -= self.speed_factor
		
		#update rect position
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""draw bullet to screen"""
		pygame.draw.rect(self.screen, self.colour, self.rect)
