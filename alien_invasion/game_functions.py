import sys

import pygame

from bullet import Bullet
from alien import Alien
from time import sleep

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
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event,ship):
	"""respond to key releases"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
	bullets, mouse_x, mouse_y):
	"""start a new game when player clicks on play"""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		#reset the game settings
		ai_settings.initialise_dynamic_settings()
		#hide mouse cursor
		pygame.mouse.set_visible(False)
		#reset game stats
		stats.reset_stats()
		stats.game_active = True
		#empty lists of bullets and aliens
		aliens.empty()
		bullets.empty()
		#create a new fleet and ship
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()


def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets):
	"""respond to keypresses and mouses"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event,ai_settings,screen,ship, bullets)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,ship)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				check_play_button(ai_settings, screen, stats, play_button,
					ship, aliens, bullets, mouse_x, mouse_y)

def get_number_aliens_x(ai_settings, alien_width):
	"""determine number of aliens in a row"""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
	"""determine number of rows of aliens that will fit on screen"""
	available_space_y = (ai_settings.screen_height -
		3 * alien_height) - ship_height
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	"""create an alien and put it in a row"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
	"""create a full fleet of aliens"""
	#create an alien and find the number of aliens in a row
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	#create first row of aliens
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
	play_button):
	"""update images on screen and flip to new screen"""
	#redraw all bullets behind ship and alien(s)
	screen.fill(ai_settings.bg_colour)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)

	#draw the score information
	sb.show_score()

	#only draw play button if game is inactive
	if not stats.game_active:
		play_button.draw_button()

	#make most recently drawn screen visible
	pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, 
	ship, aliens, bullets):
	"""update the position of bullets and remove old bullets"""
	#update bullet positions
	bullets.update()

	#get rid of bullets that have gone off the top of the screen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_settings, screen, stats, sb, 
		ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, 
	ship, aliens, bullets):
	"""respond to bullets that have hits aliens, remove bullet and aliens"""
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points
		sb.prep_score()
		check_high_score(stats, sb)
		
	if len(aliens) == 0:
		#destroy existing bullets, speed up game and create a new fleet
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings,screen,ship,bullets):
	"""fire a bullet if limit not reached"""
	#create a new bullet and add it to bullets group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_fleet_edges(ai_settings, aliens):
	"""respond if any alien in fleet has hit an edge"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
	"""check if any aliens have reached bottom of screen"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			#treat the same as if the ship was hit
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
			break

def change_fleet_direction(ai_settings, aliens):
	"""drop the fleet and change direction of movement"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
	"""check if the fleet is at an edge
	and then update the position of all aliens in fleet"""
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	#look for alien-ship collisions
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
	#look for aliens hitting bottom
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
	"""respond to ship being hit by aliens"""
	if stats.ships_left > 0:
		#decrement ships_left
		stats.ships_left -= 1

		#empty lists of aliens and bullets
		aliens.empty()
		bullets.empty()

		#create a new fleet and centre the ship
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

		#pause
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_high_score(stats, sb):
	"""check to see if there is a new high score"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
		
