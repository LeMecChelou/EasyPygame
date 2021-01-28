import pygame
import string
from Bases import MotherObject, bases
from objects.Button import Button


"""
TO DO:
	- REVOIR LE COMPORTEMENT DE ON_PRESS ET ON_RELEASE POUR POTENTIELLEMENT REMPLACER PAR ON_ACTION DANS LA CLASSE MERE.
	- Le texte est d'abord positioner à gauche de la barre de recherche puis à droite quand il dépasse une certaine
	longueur (comparer longueur rect texte et size).
	- Dessiner un carré de couleur press_background_color quand à gauche juste à côté du texte pour qu'il disparaisse
	en dessous quand l'utilisateur continue de rechercher.
"""


class TextInput(MotherObject.MotherObject):
	"""A text input bar. Can be automaticaly linked to a button."""

	def __init__(self, pos, size, has_button=False):
		"""
		:param pos: (list or tuple) The position (X, Y) of the input.
		:param size: (list or tuple) The size (X, Y)  of the input.
		:param has_button: Creates a 'Submit' button next to it if True.
		"""

		super().__init__(pos, size)

		# ------------------------ INPUT'S TEXT ------------------------ #
		self.text_input = ""
		self.listening = False

		# Changing the basic position of the text.
		self.pos_text = (self.pos[0] + 15, (self.size[1] - self.text_rect.h) // 2 + self.pos[1])
		self.render_text()

		# ------------------------ BACKGROUND COLORS ------------------------ #
		self.background_color = (240, 240, 240)
		self.hover_background_color = bases.LIGHT_GRAY
		self.press_background_color = bases.GRAY

		# ------------------------ INPUT'S BUTTON ------------------------ #
		if has_button:
			# Creating the button.
			pos_button = (pos[0] + size[0] + 10, pos[1])
			size_button = (100, size[1])
			self.button = Button(pos_button, size_button, "Submit")

			# Updating the button's text size.
			self.button.render_text(size=26)
			self.button.render_pressed_text(size=26)
			self.button.render_hovered_text(size=26)
		else:
			self.button = None

	# ----------------------------------------- #
	# TEXT FUNCTIONS							#
	# ----------------------------------------- #

	# ----------------------------------------- #
	# DRAWING FUNCTIONS							#
	# ----------------------------------------- #
	def draw(self, surface):
		super().draw(surface)

		# Drawing the button if there is one.
		if self.button is not None:
			self.button.draw(surface)

		if self.text_input != "":
			self.render_text(self.text_input)

	def draw_basic(self, surface):
		"""Draw the basic version of the input bar."""

		# Drawing the background of the input.
		pygame.draw.rect(surface, self.background_color, self.rect_data)

		# Drawing the border.
		if self.border_thickness > 0:
			pygame.draw.rect(surface, self.border_color, self.rect_data, self.border_thickness)

		# Adding the text.
		if self.text_input != "":
			surface.blit(self.text, self.pos_text)
		# Drawing the cursor when listening the inputs.
		# Drawing the rect to hide the text at the left.

	def draw_hovered(self, surface):
		"""Draw the hovered version of the input bar."""

		# Drawing the background of the input.
		pygame.draw.rect(surface, self.hover_background_color, self.rect_data)

		# Drawing the border.
		if self.border_thickness > 0:
			pygame.draw.rect(surface, self.hover_border_color, self.rect_data, self.hover_border_thickness)

	def draw_pressed(self, surface):
		"""This function will draw the input bar as writing mode."""

		# Drawing the background of the input.
		pygame.draw.rect(surface, self.press_background_color, self.rect_data)

		# Drawing the border.
		if self.border_thickness > 0:
			pygame.draw.rect(surface, self.press_border_color, self.rect_data, self.press_border_thickness)

	# ----------------------------------------- #
	# EVENT FUNCTIONS							#
	# ----------------------------------------- #

	def is_hovered(self, event_pos):
		"""Check if the input bar is hovered by the event.
		If True, self.hovered == True."""

		# Checking if the input bar is hovered.
		super().is_hovered(event_pos)

		# Checking if the input's button is hovered.
		if self.button is not None:
			self.button.is_hovered(event_pos)

	def is_pressed(self, *args):
		"""Function called to check if the button is pressed and execute the function linked to this event if
		there is one."""

		super().is_pressed()

		# Checking if the input is listening the keyboard events.
		if self.pressed and not self.listening:
			self.listening = True
		else:
			self.listening = False

		# Checking if the button is pressed.
		if self.button is not None:
			self.button.is_pressed(args)

	def is_released(self, *args):
		"""Function called to check if the button is released and execute the function linked to this event if
		there is one"""

		super().is_released()

		# Checking if the button is released.
		if self.button is not None:
			self.button.is_released(args)

	# ----------------------------------------- #
	# EVENT FUNCTIONS							#
	# ----------------------------------------- #
	def listen_inputs(self, event):
		"""Listen the inputs from the keyboard. If self.pressed == True, then the inputs are added to the text in the
		input bar."""

		if self.listening:
			if event.key == pygame.K_RETURN:
				if self.button.on_press is not None:
					self.button.on_press()
			elif event.key == pygame.K_ESCAPE:
				self.text_input = ""
			elif event.key == pygame.K_DELETE:
				self.text_input = self.text_input[:-1]
			elif event.unicode in string.printable:
				self.text_input += event.unicode

			print(self.text_input)
