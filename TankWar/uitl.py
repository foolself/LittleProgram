import pygame
from pygame.locals import *

def load_image(fullpath, colorkey=None):
	try:
		image = pygame.image.load(fullpath)
	except pygame.error, message:
		print 'Cannot load image:', fullpath
		raise SystemExit, message
	image = image.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image#, image.get_rect()

def load_sound(fullpath):
	class NoneSound:
		def play(self): pass
	if not pygame.mixer or not pygame.mixer.get_init():
		return NoneSound()
	try:
		sound = pygame.mixer.Sound(fullpath)
	except pygame.error, message:
		print 'Cannot load sound:', fullpath
		raise SystemExit, message
	return sound