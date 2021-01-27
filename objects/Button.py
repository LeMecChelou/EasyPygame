import pygame
import bases


class Button:

	def __init__(self, pos, size, text):
		"""
		The graphical aspect of the button can be fully modified by the user after the creation.
		:param pos: (list or tuple) Position of the left top corner of the button.
		:param size: (list or tuple) Size (X, Y) of the button.
		:param text: (str) Text of the button.
		"""
		assert isinstance(pos, list) or isinstance(pos, tuple), "Argument 'pos' must be a list or a tuple."
		assert isinstance(size, list) or isinstance(size, tuple), "Argument 'pos' must be a list or a tuple."
		assert isinstance(text, str), "Argument 'text' must be of a string."

		self.pos = pos
		self.size = size

		# ------------------------ ACTION VARIABLES ------------------------ #
		self.on_press = None
		self.on_release = None

		# ------------------------ BASIC MODE ------------------------ #
		self.background_color = bases.LIGHT_GRAY

		# Border variables.
		self.border_thickness = 1
		self.border_color = bases.BLACK

		# Text variables
		self.text_content = text
		self.text, self.text_rect = self.render_text()

		# ------------------------ HOVER MODE ------------------------ #
		self.hovered = False

		self.hover_background_color = bases.GRAY

		self.hover_border_color = bases.BLACK
		self.hover_border_thickness = 1

		# To modify the hovered text, the user has to call the function render_hovered_text() which works
		# like render_text().
		self.hover_text, self.hover_text_rect = self.render_hovered_text()

		# ------------------------ PRESSED MODE ------------------------ #
		self.pressed = False

		self.press_background_color = bases.DARK_GRAY

		self.press_border_color = bases.BLACK
		self.press_border_thickness = 1

		# To modify the hovered text, the user has to call the function render_hovered_text() which works
		# like render_text().
		self.press_text, self.press_text_rect = self.render_pressed_text()

	# ----------------------------------------- #
	# TEXT FUNCTIONS							#
	# ----------------------------------------- #
	def render_text(self, font=None, size=32, color=bases.BLACK):
		"""Render the text contained in the button. Is called when the button is initialized but can be called again
		to actualise the text, font, color or size."""

		# Create the pygame.font.Font object.
		self.text = pygame.font.Font(font, size).render(self.text_content, True, color)

		# Get the Rect object based on the size and position of the button.
		self.text_rect = self.text.get_rect(center=(
			(self.size[0] // 2) + self.pos[0],
			(self.size[1] // 2) + self.pos[1])
		)

		return self.text, self.text_rect

	def render_hovered_text(self, font=None, size=32, color=bases.BLACK):
		"""Works like render_text() but for the hovered mode of the button."""

		self.hover_text = pygame.font.Font(font, size).render(self.text_content, True, color)

		self.hover_text_rect = self.hover_text.get_rect(center=(
			(self.size[0] // 2) + self.pos[0],
			(self.size[1] // 2) + self.pos[1])
		)

		return self.hover_text, self.hover_text_rect

	def render_pressed_text(self, font=None, size=32, color=bases.BLACK):
		"""Works like render_text() but for the pressed mode of the button."""

		# Create the pygame.font.Font object.
		self.press_text = pygame.font.Font(font, size).render(self.text_content, True, color)

		# Get the Rect object based on the size and position of the button.
		self.press_text_rect = self.press_text.get_rect(center=(
			(self.size[0] // 2) + self.pos[0],
			(self.size[1] // 2) + self.pos[1])
		)

		return self.press_text, self.press_text_rect

	# ----------------------------------------- #
	# DRAWING FUNCTIONS							#
	# ----------------------------------------- #
	def draw(self, surface):
		"""Draw the button while considering the mode of the button."""

		# Ajouter les modes.
		if self.pressed:
			self.draw_pressed_button(surface)
		elif self.hovered:
			self.draw_hovered_button(surface)
		else:
			self.draw_basic_button(surface)

	def draw_basic_button(self, surface: pygame.Surface):
		"""Draw the button with the basic mode aspect."""

		rect_data = (self.pos[0], self.pos[1], self.size[0], self.size[1])

		# Drawing the background of the button.
		pygame.draw.rect(surface, self.background_color, rect_data)

		# Drawing the border.
		if self.border_thickness > 0:
			pygame.draw.rect(surface, self.border_color, rect_data, self.border_thickness)

		# Drawing the text.
		surface.blit(self.text, self.text_rect)

	def draw_hovered_button(self, surface):
		"""Draw the button with the hovered mode aspect."""

		rect_data = (self.pos[0], self.pos[1], self.size[0], self.size[1])

		# Drawing the background of the button.
		pygame.draw.rect(surface, self.hover_background_color, rect_data)

		# Drawing the border.
		if self.hover_border_thickness > 0:
			pygame.draw.rect(surface, self.hover_border_color, rect_data, self.hover_border_thickness)

		# Drawing the text.
		surface.blit(self.hover_text, self.hover_text_rect)

	def draw_pressed_button(self, surface: pygame.Surface):
		"""Draw the button with the pressed mode aspect."""

		rect_data = (self.pos[0], self.pos[1], self.size[0], self.size[1])

		# Drawing the background of the button.
		pygame.draw.rect(surface, self.press_background_color, rect_data)

		# Drawing the border.
		if self.press_border_thickness > 0:
			pygame.draw.rect(surface, self.press_border_color, rect_data, self.press_border_thickness)

		# Drawing the text.
		surface.blit(self.press_text, self.press_text_rect)

	# ----------------------------------------- #
	# EVENTS FUNCTIONS							#
	# ----------------------------------------- #
	def is_hovered(self, event_pos):
		"""Check if the button is hovered by the event position.
		If True, self.hovered == True."""

		hover_test_X = self.pos[0] <= event_pos[0] <= self.pos[0] + self.size[0]
		hover_test_Y = self.pos[1] <= event_pos[1] <= self.pos[1] + self.size[1]

		if hover_test_X and hover_test_Y and not self.pressed:
			self.hovered = True
		else:
			self.hovered = False

	def is_activated(self, event_pos, *args):
		"""Check is the button is pressed and execute the actions in function of the case.
		It takes arguments to give to the function linked to the event when released of pressed."""

		# Checking if the button is hovered by the event.
		self.is_hovered(event_pos)

		if self.hovered and not self.pressed:
			self.pressed = True

			# Checking is there is a function linked to the on_press event.
			if self.on_press is not None:
				if args != ():
					self.on_press(args)
				else:
					self.on_press()

		elif not self.hovered and self.pressed:
			self.pressed = False

			# Checking is there is a function linked to the on_press event.
			if self.on_release is not None:
				if args != ():
					self.on_release(args)
				else:
					self.on_release()
