
import pygame
import sys
import ss_game_functions as ssgf

from ss_settings import Settings
from ss_ship import ss_Ship
from pygame.sprite import Group

def run_game():
	# Initializing pygame & creating 
	# a screen object
	pygame.init()
	settings_ss = Settings()
	screen = pygame.display.set_mode(
		(settings_ss.screen_width,
			settings_ss.screen_height))
	pygame.display.set_caption("sideways_shooter")


	# Make a ship.
	ship = ss_Ship(settings_ss,screen)
	# Make a group to store bullets in.
	bullets = Group()

	while True:
		ssgf.check_events(screen, ship, bullets,settings_ss)
		ship.update()
		ssgf.update_bullets(bullets,settings_ss)
		ssgf.update_screen(screen,settings_ss,ship,bullets)




run_game()
