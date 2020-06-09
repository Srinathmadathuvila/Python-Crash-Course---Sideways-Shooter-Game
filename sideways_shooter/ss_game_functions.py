
import sys 
import pygame

from  ss_bullet import Bullet

def check_events(screen, ship, bullets, settings_ss):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				ship.moving_top = True
			elif event.key == pygame.K_DOWN:
				ship.moving_bot = True
			elif event.key == pygame.K_SPACE:
				fire_bullet(settings_ss, 
					screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				ship.moving_top = False
			elif event.key == pygame.K_DOWN:
				ship.moving_bot = False

def update_screen(screen, settings_ss,ship, bullets):
	"""Update images on the screen and flip to
	the new screen."""
	# Redraw the screen during each pass trought
	# the loop.
	screen.fill(color=settings_ss.bg_color)
	# redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	# Make the most recently drawn screen visible.
	pygame.display.flip()

def update_bullets(bullets,settings_ss):
	"""Update position of bullets and get rid of old
	bullets"""
	# Update bullet positions
	bullets.update()

	# get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.left >= settings_ss.screen_width:
			bullets.remove(bullet)

def fire_bullet(settings_ss, screen, ship, bullets):
	"""Fire a bullet if limit not reached yet."""
	# create a new bullet and add it to the bullets group
	if len(bullets) < settings_ss.bullets_allowed:
		new_bullet = Bullet(settings_ss, screen,ship)
		bullets.add(new_bullet)
