
import pygame
from pygame.sprite import Sprite 

class Bullet(Sprite):
	"""A class to manage bullets fired from the ss_ship"""
	
	def __init__(self,settings_ss,screen, ship):
		super(Bullet, self).__init__()
		self.screen = screen

		# Create a bullet rect at (0,0) and then set
		# correct position
		self.rect = pygame.Rect(0,0,settings_ss.bullet_width,
			settings_ss.bullet_height)
		self.rect.centery = ship.rect.centery
		self.rect.right = ship.rect.right

		# Store the bullet's position as a decimal value.
		self.x = float(self.rect.x)

		self.color = settings_ss.bullet_color
		self.speed_factor = settings_ss.bullet_speed_factor

	def update(self):
		"""Moove the bullet to the right of the screen."""
		# Update the decimal position of the bullet 
		self.x += self.speed_factor
		# update the rect position
		self.rect.x = self.x 

	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen,
			self.color,
			self.rect)
