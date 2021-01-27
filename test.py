from EasyPygame import *
import pygame


def on_release():
	print("Bouton relaché")


def on_press():
	print("Bouton pressé")


pygame.init()


fnt = pygame.display.set_mode((800, 800))

btn = Button((200, 200), (300, 75), "Test")
btn.render_text(size=32)
btn.on_release = on_release
btn.on_press = on_press


# Modification du texte quand le bouton est pressé.
btn.render_pressed_text(color=bases.ORANGE)

# Modification de la couleur de fond quand le bouton est survolé.
btn.hover_background_color = bases.PINK


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
			btn.is_pressed()
		if event.type == pygame.MOUSEBUTTONUP:
			btn.is_released()


pygame.quit()
