import pygame
from pygame.locals import *

from uitl import *

enemyB = "data/bullet/enemymissile.gif"
playerB = "data/bullet/tankmissile.gif"
blast2 = "data/bullet/blast1.png"
blast3 = "data/bullet/blast2.png"
blast4 = "data/bullet/blast3.png"

SPEED_B = 3
bullets = [playerB, enemyB]
blasts_img = [blast2, blast3, blast4]
rel_pos = [[0, -30], [0, 30], [-30, 0], [30, 0]]
move_pos = [[0, -SPEED_B], [0, SPEED_B], [-SPEED_B, 0], [SPEED_B, 0]]
class Bullet(pygame.sprite.Sprite):
	def __init__(self, att, pos, dct):
		pygame.sprite.Sprite.__init__(self)
		self.att = att
		self.bullet = bullets[self.att]
		self.image = load_image(self.bullet, -1)
		self.rect = self.image.get_rect()
		self.rect.center = (pos[0] + rel_pos[dct][0], 
			pos[1] + rel_pos[dct][1])
		self.dct = dct
		self.temp_center = self.rect.center
		self.blast_disappear = 0
	def update(self):
		if self.blast_disappear == 0:
			self.move()


	def move(self):
		self.rect.move_ip(move_pos[self.dct][0], move_pos[self.dct][1])
	def check_out_window(self):
		pos = self.rect.center
		if (pos[1] - 8) < 0 or (pos[1] + 8) > 660 or (pos[0] - 8) < 0 or (pos[0] + 8) > 1200:
			return True
	def check_block_collide(self, blockG):
		rectlist = []
		for s in blockG:
			rectlist.append(s.rect)
		if self.rect.collidelistall(rectlist):
			if self.blast_disappear == 0:
				self.temp_center = self.rect.center
				self.blast_disappear = 1
		if self.blast_disappear > 0:
			self.blast_disappear = self.blast_disappear + 1
			if self.blast_disappear > 14:
				return True
			self.image = load_image(blasts_img[self.blast_disappear // 5], -1)
			self.rect = self.image.get_rect()
			self.rect.center = self.temp_center
		return False
	def check_enemy_collide(self, enemyG):
		rectlist = []
		for e in enemyG:
			rectlist.append(e.rect)
		for x in enemyG:
			if self.rect.colliderect(x.rect):
				if self.blast_disappear == 0:
					self.temp_center = self.rect.center
					self.blast_disappear = 1
					return x
		if self.blast_disappear > 0:
			self.blast_disappear = self.blast_disappear + 1
			if self.blast_disappear > 14:
				return 1
			self.image = load_image(blasts_img[self.blast_disappear // 5], -1)
			self.rect = self.image.get_rect()
			self.rect.center = self.temp_center
		return 0
	def blast(self):
		pass