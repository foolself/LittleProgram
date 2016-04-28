import random
import pygame
from pygame.locals import *

from uitl import *
import bullet

p1tankU = "data/tank/p1tankU.png"
p1tankD = "data/tank/p1tankD.png"
p1tankL = "data/tank/p1tankL.png"
p1tankR = "data/tank/p1tankR.png"
p2tankU = "data/tank/p2tankU.png"
p2tankD = "data/tank/p2tankD.png"
p2tankL = "data/tank/p2tankL.png"
p2tankR = "data/tank/p2tankR.png"

enemy1U = "data/tank/enemy1U.png"
enemy1D = "data/tank/enemy1D.png"
enemy1L = "data/tank/enemy1L.png"
enemy1R = "data/tank/enemy1R.png"
enemy2U = "data/tank/enemy2U.png"
enemy2D = "data/tank/enemy2D.png"
enemy2L = "data/tank/enemy2L.png"
enemy2R = "data/tank/enemy2R.png"
enemy3U = "data/tank/enemy3U.png"
enemy3D = "data/tank/enemy3D.png"
enemy3L = "data/tank/enemy3L.png"
enemy3R = "data/tank/enemy3R.png"

born1 = "data/tank/born1.gif"
born2 = "data/tank/born2.gif"
born3 = "data/tank/born3.gif"
born4 = "data/tank/born4.gif"

SPEED = 1
enemyTanks = [
				[enemy1U, enemy1D, enemy1L, enemy1R], 
				[enemy1U, enemy1D, enemy1L, enemy1R], 
				[enemy1U, enemy1D, enemy1L, enemy1R],
			]
playerTanks = [
				[p1tankU, p1tankD, p1tankL, p1tankR], 
				[p2tankU, p2tankD, p2tankL, p2tankR], 
			]
borns = [born1, born2, born3, born4]

class PlayerTank(pygame.sprite.Sprite):
	"""moves a clenched fist on the screen, following the mouse"""
	def __init__(self, att, pos):
		pygame.sprite.Sprite.__init__(self)
		self.tank = playerTanks[att]
		self.image = load_image(self.tank[0], -1)
		self.rect = self.image.get_rect()
		self.rect.center = pos
		self.dct = 0
		self.bullets = pygame.sprite.Group()
		self.time = 0
	# def update(self):
	# 	pass

	def move(self, 	dct, blockG):
		if self.time < 79:
			self.image = load_image(borns[self.time // 6 % 4], -1)
			self.time = self.time + 1
			return
		if dct [K_UP]:
			self.dct = 0
			self.rect.move_ip(0, -SPEED)
			if self.check_block_collide(blockG):
				self.rect.move_ip(0, +SPEED)
			self.image = load_image(self.tank[0], -SPEED)
		if dct [K_DOWN]:
			self.dct = 1
			self.rect.move_ip(0, SPEED)
			if self.check_block_collide(blockG):
				self.rect.move_ip(0, -SPEED)
			self.image = load_image(self.tank[1], -1)
		if dct [K_LEFT]:
			self.dct = 2
			self.rect.move_ip(-SPEED, 0)
			if self.check_block_collide(blockG):
				self.rect.move_ip(SPEED, 0)
			self.image = load_image(self.tank[2], -1)
		if dct [K_RIGHT]:
			self.dct = 3
			self.rect.move_ip(SPEED, 0)
			if self.check_block_collide(blockG):
				self.rect.move_ip(-SPEED, 0)
			self.image = load_image(self.tank[3], -1)
	def fire(self):
		b = bullet.Bullet(0, self.rect.center, self.dct)
		self.bullets.add(b)
	def get_bullets(self):
		return self.bullets
	def check_block_collide(self, blockG):
		rectlist = []
		for s in blockG:
			rectlist.append(s.rect)
		pos = self.rect.center
		if (pos[1] - 30) < 0 or (pos[1] + 30) > 660 or (pos[0] - 30) < 0 or (pos[0] + 30) > 1200:
			return True

		return self.rect.collidelistall(rectlist)



class EnemyTank(pygame.sprite.Sprite):
	def __init__(self, att, pos):
		pygame.sprite.Sprite.__init__(self)
		self.tank = enemyTanks[att]
		self.image = load_image(self.tank[0], -1)
		self.rect = self.image.get_rect()
		self.rect.center = pos
		self.dct = 0
		self.bullets = pygame.sprite.Group()
		self.time = 0

	def update(self):
		if self.time < 79:
			return
		r = random.randint(0, 200)
		if r > 198:
			self.fire()
		if r == 1 or r == 100:
			self.turn_dct()
	def move(self, blockG):
		if self.time < 79:
			self.image = load_image(borns[self.time // 6 % 4], -1)
			self.time = self.time + 1
			return
		if self.dct == 0:
			self.rect.move_ip(0, -SPEED)
			if self.check_block_collide(blockG):
				self.rect.move_ip(0, +SPEED)
				self.turn_dct()
		if self.dct == 1:
			self.rect.move_ip(0, SPEED)
			if self.check_block_collide(blockG):
				self.rect.move_ip(0, -SPEED)
				self.turn_dct()
		if self.dct == 2:
			self.rect.move_ip(-SPEED, 0)
			if self.check_block_collide(blockG):
				self.rect.move_ip(SPEED, 0)
				self.turn_dct()
		if self.dct == 3:
			self.rect.move_ip(SPEED, 0)
			if self.check_block_collide(blockG):
				self.rect.move_ip(-SPEED, 0)
				self.turn_dct()
		self.image = load_image(self.tank[self.dct], -1)

	def turn_dct(self):
		dcts = [0, 1, 2, 3]
		# dcts.remove(self.dct)
		self.dct = random.choice(dcts)

	def check_block_collide(self, blockG):
		rectlist = []
		for s in blockG:
			rectlist.append(s.rect)
		pos = self.rect.center
		if (pos[1] - 30) < 0 or (pos[1] + 30) > 660 or (pos[0] - 30) < 0 or (pos[0] + 30) > 1200:
			return True
		return self.rect.collidelistall(rectlist)

	def fire(self):
		b = bullet.Bullet(1, self.rect.center, self.dct)
		self.bullets.add(b)
	def get_bullets(self):
		return self.bullets
