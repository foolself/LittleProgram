import pygame
from pygame.locals import *

from uitl import *
walls_img = "data/block/walls.gif"
wall_img = "data/block/wall.gif"
steels_img = "data/block/steels.gif"
steel_img = "data/block/steel.gif"
water_img = "data/block/water.gif"
grass_img = "data/block/grass.png"

blocks_img = [walls_img, steels_img, water_img, grass_img]

class Block(pygame.sprite.Sprite):
	def __init__(self, att, pos):
		pygame.sprite.Sprite.__init__(self)
		self.att = att
		self.block = blocks_img[self.att]
		self.image = load_image(self.block, -1)
		self.rect = self.image.get_rect()
		self.rect.topleft = (pos[0] * 60, pos[1] * 60)