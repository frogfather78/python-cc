import sys

import pygame

from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	"""respond to keypresses"""
	if event.key == pygame.K_RIGHT:
		#move ship to the right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		#move ship to the left
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event,ship):
	"""respond to key releases"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def check_events(ai_settings,screen,ship,bullets):
	"""respond to keypresses and mouses"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event,ai_settings,screen,ship, bullets)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,ship)
		
def update_screen(ai_settings, screen, ship,bullets):
	"""update images on screen and flip to new screen"""		
	#redraw all bullets behind ship and aliens??
	screen.fill(ai_settings.bg_colour)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
		
	#make most recently drawn screen visible
	pygame.display.flip()

def update_bullets(bullets):
	"""update the position of bullets and remove old bullets"""
	#update bullet positions
	bullets.update()
	#get rid of bullets that have gone off the top of the screen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	
def fire_bullet(ai_settings,screen,ship,bullets):
	"""fire a bullet if limit not reached"""		
	#create a new bullet and add it to bullets group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
