import sys
import pygame

from settings import Settings

def run_game():
	#initialise game, settings and screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	
	#set the game loop
	while True:
		#watch for keyboard/mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		#redraw screen during each pass
		screen.fill(ai_settings.bg_colour)
		
		#make most recently drawn screen visible
		pygame.display.flip()
	
run_game()
