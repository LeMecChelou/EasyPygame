import pygame
from Bases import MotherObject, bases


class Button(MotherObject.MotherObject):

	def __init__(self, pos, size, text):
		"""
		The graphical aspect of the button can be fully modified by the user after the creation.
		:param pos: (list or tuple) Position of the left top corner of the button.
		:param size: (list or tuple) Size (X, Y) of the button.
		:param text: (str) Text of the button.
		"""
		assert isinstance(text, str), "Argument 'text' must be of a string."

		# Initialization of the mother class.
		super().__init__(pos, size)

		# Rendering the texts objects with the button's text.
		self.render_text(text=text)
		self.render_hovered_text(text=text)
		self.render_pressed_text(text=text)

	# ----------------------------------------- #
	# DRAWING FUNCTIONS							#
	# ----------------------------------------- #
	def draw_basic(self, surface: pygame.Surface):
		"""Draw the button with the basic mode aspect."""

		# Drawing the background of the button.
		pygame.draw.rect(surface, self.background_color, self.rect_data)

		# Drawing the border.
		if self.border_thickness > 0:
			pygame.draw.rect(surface, self.border_color, self.rect_data, self.border_thickness)

		# Drawing the text.
		surface.blit(self.text, self.text_rect)

	def draw_hovered(self, surface):
		"""Draw the button with the hovered mode aspect."""

		# Drawing the background of the button.
		pygame.draw.rect(surface, self.hover_background_color, self.rect_data)

		# Drawing the border.
		if self.hover_border_thickness > 0:
			pygame.draw.rect(surface, self.hover_border_color, self.rect_data, self.hover_border_thickness)

		# Drawing the text.
		surface.blit(self.hover_text, self.hover_text_rect)

	def draw_pressed(self, surface: pygame.Surface):
		"""Draw the button with the pressed mode aspect."""

		# Drawing the background of the button.
		pygame.draw.rect(surface, self.press_background_color, self.rect_data)

		# Drawing the border.
		if self.press_border_thickness > 0:
			pygame.draw.rect(surface, self.press_border_color, self.rect_data, self.press_border_thickness)

		# Drawing the text.
		surface.blit(self.press_text, self.press_text_rect)

	# ----------------------------------------- #
	# EVENT FUNCTIONS							#
	# ----------------------------------------- #
	def is_pressed(self, *args):
		"""Function called to check if the button is pressed and execute the function linked to this event if
		there is one."""

		if self.hovered and not self.pressed:
			self.pressed = True

			# Checking is there is a function linked to the on_press event.
			if self.on_press is not None:
				if args != ():
					self.on_press(args)
				else:
					self.on_press()

	def is_released(self, *args):
		"""Function called to check if the button is released and execute the function linked to this event if
		there is one"""

		if self.pressed:
			self.pressed = False

			# Checking is there is a function linked to the on_press event.
			if self.on_release is not None:
				if args != ():
					self.on_release(args)
				else:
					self.on_release()
