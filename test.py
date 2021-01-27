from EasyPygame import *
import pygame


def test():
	print("test")


pygame.init()


fnt = pygame.display.set_mode((800, 800))

btn = Button((200, 200), (300, 75), "Test")
btn.render_text(size=32)
btn.on_release = test


run = True
while run:
	fnt.fill(bases.WHITE)
	btn.draw(fnt)
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEMOTION:
			# Check if the button is hovered by the mouse.
			btn.is_hovered(event.pos)

		if event.type == pygame.MOUSEBUTTONDOWN:
			btn.is_activated(event.pos)
		if event.type == pygame.MOUSEBUTTONUP:
			btn.is_activated(event.pos)


pygame.quit()
