from EasyPygame import *
import pygame


pygame.init()


fnt = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


btn = Button((200, 200), (300, 30), "Test")


inputTxt = TextInput((25, 100), (600, 75), True)


run = True
while run:
	clock.tick(60)

	fnt.fill(bases.WHITE)
	btn.draw(fnt)
	inputTxt.draw(fnt)
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		elif event.type == pygame.MOUSEMOTION:
			# Checking if the elements are hovered by the mouse.
			btn.is_hovered(event.pos)
			inputTxt.is_hovered(event.pos)

		elif event.type == pygame.MOUSEBUTTONDOWN:
			btn.is_pressed()
			inputTxt.is_pressed()
		elif event.type == pygame.MOUSEBUTTONUP:
			btn.is_released()
			inputTxt.is_released()

		elif event.type == pygame.KEYDOWN:
			inputTxt.listen_inputs(event)


pygame.quit()
