
import pygame

class ss_Ship():
	"""Ship diplayed in the sideways_shooter game"""

	def __init__(self,settings_ss, screen):
		""" Initialize the ship and set its starting
		position"""
		self.screen = screen
		self.settings_ss = settings_ss

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ss_ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# start each new ship at the center left of the screen
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left
		# Store a decimal value for the ship's height
		self.center = float(self.rect.centery)

		# Moving flag 
		self.moving_top = False
		self.moving_bot = False

	def update(self):
		"""Update the ship's position based on the 
		movement flag"""
		# Update the ship's center value, not the rect.

		if self.moving_top and self.rect.top > self.screen_rect.top:
			self.center -= 1
		if self.moving_bot and self.rect.bottom < self.screen_rect.bottom:
			self.center += 1

		self.rect.centery = self.center

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

