import os, pygame
from pygame.locals import *

import bullet, wall, tank, block
from uitl import *

sound_start_f = "data/sound/start.wav"
sound_add_f = "data/sound/add.wav"
sound_fire_f = "data/sound/fire.wav"
sound_blast_f = "data/sound/blast.wav"
sound_hit_f = "data/sound/hit.wav"

SCR_W = 1200
SCR_H = 660
FRAME = 60

COUNT_ENEMY = 20
COUNT_PLAYER = 3

enemy_add_pos = [
					[31, 31], [SCR_W - 31, SCR_H -31], 
					[31, SCR_H -31], [SCR_W - 31, 31],
				]
player_add_pos = [7 * 60 + 30, SCR_H - 31]

walls = [
			[0, 3, 3], [0, 4, 3], [0, 5, 3], [0, 6, 3], 
			[0, 7, 3], [0, 8, 3], [0, 9, 3], [0, 10, 3], 
			[0, 11, 3], [0, 12, 3], [0, 13, 3], [0, 14, 3], 
			]
steels = [
			[1, 3, 7], [1, 4, 7], [1, 5, 7], [1, 6, 7], 
			[1, 7, 7], [1, 8, 7], [1, 9, 7], [1, 10, 7], 
			[1, 11, 7], [1, 12, 7], [1, 13, 7], [1, 14, 7], 
		]
waters = [
			[2, 0, 5], [2, 1, 5], [2, 2, 5], [2, 18, 5], [2, 19, 5], 
		]
grasses = [
			[3, 1, 3], [3, 2, 3], [3, 18, 3], [3, 19, 3], 
		]

def block_init():
	blocks_no_move = pygame.sprite.Group()
	blocks_steel = pygame.sprite.Group()
	for x in steels:
		bl = block.Block(x[0], (x[1], x[2]))
		blocks_steel.add(bl)
		blocks_no_move.add(bl)

	blocks_wall = pygame.sprite.Group()
	for x in walls:
		bl = block.Block(x[0], (x[1], x[2]))
		blocks_wall.add(bl)
		blocks_no_move.add(bl)

	blocks_water = pygame.sprite.Group()
	for x in waters:
		bl = block.Block(x[0], (x[1], x[2]))
		blocks_water.add(bl)
		blocks_no_move.add(bl)

	blocks_grasses = pygame.sprite.Group()
	for x in grasses:
		bl = block.Block(x[0], (x[1], x[2]))
		blocks_grasses.add(bl)
	return blocks_no_move, blocks_steel, blocks_wall, blocks_water, blocks_grasses

def main():
	COUNT_ENEMY = 20
	COUNT_PLAYER = 3
	pygame.init()
	sound_start = load_sound(sound_start_f)
	sound_add = load_sound(sound_add_f)
	sound_fire = load_sound(sound_fire_f)
	sound_blast = load_sound(sound_blast_f)
	sound_hit = load_sound(sound_hit_f)
	screen = pygame.display.set_mode((SCR_W, SCR_H))
	pygame.display.set_caption('TANK BATTLE')
	pygame.mouse.set_visible(0)
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))

	screen.blit(background, (0, 0))
	pygame.display.flip()

	clock = pygame.time.Clock()

	blocks_no_move, blocks_steel, blocks_wall, blocks_water, blocks_grasses = block_init()

	players = pygame.sprite.Group()
	player1 = tank.PlayerTank(1, (player_add_pos[0], player_add_pos[1]))
	players.add(player1)

	enemys = pygame.sprite.Group()
	for x in xrange(0,3):
		enemy = tank.EnemyTank(x, (enemy_add_pos[x][0], enemy_add_pos[x][1]))
		enemys.add(enemy)

	sound_start.play()
	while 1:
		clock.tick(FRAME)
		screen.blit(background, (0, 0))

		for event in pygame.event.get():
			if event.type == QUIT:
				return
			if event.type == KEYDOWN and event.key == K_SPACE:
				player1.fire()
				sound_fire.play()
		pressed_keys = pygame.key.get_pressed()

		player1.move(pressed_keys, blocks_no_move)

		for x in enemys:
			x.move(blocks_no_move)
		enemys.update()
		players.update()
		enemys.draw(screen)
		players.draw(screen)

		blocks_steel.update()
		blocks_steel.draw(screen)
		blocks_wall.update()
		blocks_wall.draw(screen)
		blocks_water.update()
		blocks_water.draw(screen)
		blocks_grasses.update()
		blocks_grasses.draw(screen)

		# collide check!
		p_bullets = player1.get_bullets()
		p_bullets.update()
		for x in p_bullets:
			if x.check_out_window():
				p_bullets.remove(x)
			if x.check_block_collide(blocks_steel):
				p_bullets.remove(x)
				sound_hit.play()
			# bullet -- tank
			static_1 = x.check_enemy_collide(enemys)
			if static_1 == 0:
				pass
			elif static_1 == 1:
				p_bullets.remove(x)
			else :
				enemys.remove(static_1)
				sound_blast.play()
				if COUNT_ENEMY != 0:
					enemy = tank.EnemyTank(COUNT_ENEMY % 3, (enemy_add_pos[COUNT_ENEMY % 4][0], enemy_add_pos[COUNT_ENEMY % 4][1]))
					enemys.add(enemy)
					sound_add.play()
					COUNT_ENEMY = COUNT_ENEMY - 1

			# bullet -- wall
			static_2 = x.check_enemy_collide(blocks_wall)
			if static_2 == 0:
				pass
			elif static_2 == 1:
				p_bullets.remove(x)
				sound_blast.play()
			else :
				static_2.kill()
		p_bullets.draw(screen)

		for e in enemys:
			e_bs = e.get_bullets()
			e_bs.update()
			for b in e_bs:
				if b.check_out_window():
					e_bs.remove(b)
				if b.check_block_collide(blocks_steel):
					e_bs.remove(b)
					sound_hit.play()
				# bullet -- tank
				static_1 = b.check_enemy_collide(players)
				if static_1 == 0:
					pass
				elif static_1 == 1:
					p_bullets.remove(x)
				else :
					players.remove(static_1)
					sound_blast.play()
					if COUNT_PLAYER != 0:
						player1 = tank.PlayerTank(1, (player_add_pos[0], player_add_pos[1]))
						players.add(player1)
						sound_add.play()
						COUNT_PLAYER = COUNT_PLAYER - 1
				# # bullet -- wall
				static_2 = b.check_enemy_collide(blocks_wall)
				if static_2 == 0:
					pass
				elif static_2 == 1:
					p_bullets.remove(x)
					sound_blast.play()
				else :
					static_2.kill()
			e_bs.draw(screen)
		pygame.display.flip()

if __name__ == '__main__': main()
