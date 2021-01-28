from Bases import bases
import pygame


class MotherObject:
	"""EasyPygame Mother Object.
	The mother class of all the objects in EasyPygame."""

	def __init__(self, pos, size):
		"""
		:param pos: (list or tuple) The position (X, Y) of the object.
		:param size: (list or tuple) The size (X, Y) of the object.
		"""

		assert isinstance(pos, list) or isinstance(pos, tuple), "Argument 'pos' must be a list or a tuple."
		assert isinstance(size, list) or isinstance(size, tuple), "Argument 'pos' must be a list or a tuple."

		self.pos = pos
		self.size = size

		# See drawing functions for further explanation.
		self.rect_data = None

		# ------------------------ STATUS VARIABLES ------------------------ #
		self.hovered = False
		self.pressed = False

		# ------------------------ ACTION VARIABLES ------------------------ #
		self.on_press = None
		self.on_release = None

		# ------------------------ BASIC MODE ------------------------ #
		self.background_color = bases.LIGHT_GRAY

		# Border variables.
		self.border_thickness = 1
		self.border_color = bases.BLACK

		# Text variables
		self.text_content = ""
		self.font = None
		self.font_size = 32
		self.font_color = bases.BLACK
		self.pos_text = ((self.size[0] // 2) + self.pos[0], (self.size[1] // 2) + self.pos[1])
		self.text, self.text_rect = self.render_text()

		# ------------------------ HOVER MODE ------------------------ #
		self.hover_background_color = bases.GRAY

		self.hover_border_color = bases.BLACK
		self.hover_border_thickness = 1

		# Text variables
		self.hover_text_content = self.text_content
		self.hover_font = self.font
		self.hover_font_size = self.font_size
		self.hover_font_color = self.font_color
		self.hover_pos_text = self.pos_text
		self.hover_text, self.hover_text_rect = self.render_hovered_text()

		# ------------------------ PRESSED MODE ------------------------ #
		self.press_background_color = bases.DARK_GRAY

		self.press_border_color = bases.BLACK
		self.press_border_thickness = 1

		# Text variables
		self.press_text_content = self.text_content
		self.press_font = self.font
		self.press_font_size = self.font_size
		self.press_font_color = self.font_color
		self.press_pos_text = self.pos_text
		self.press_text, self.press_text_rect = self.render_pressed_text()

	# ----------------------------------------- #
	# TEXT FUNCTIONS							#
	# ----------------------------------------- #
	def render_text(self, text=None, font=0, size=None, color=None):
		"""Render the text contained in the object. Is called when the object is initialized but can be called again
		to actualise the text, font, color or size."""

		# Checking if there is any changement in the text variables.
		if text is not None:
			self.text_content = text
		if font != 0:
			self.font = font
		if size is not None:
			self.font_size = size
		if color is not None:
			self.font_color = color

		# Create the pygame.font.Font object.
		self.text = pygame.font.Font(self.font, self.font_size).render(self.text_content, True, self.font_color)

		# Get the Rect object based on the size and position of the button.
		self.text_rect = self.text.get_rect(center=self.pos_text)

		return self.text, self.text_rect

	def render_hovered_text(self, text=None, font=None, size=32, color=bases.BLACK):
		"""Works like render_text() but for the hovered mode of the object."""

		if text is not None:
			self.hover_text_content = text
		if font != 0:
			self.hover_font = font
		if size is not None:
			self.hover_font_size = size
		if color is not None:
			self.hover_font_color = color

		self.hover_text = pygame.font.Font(self.hover_font, self.hover_font_size).render(
			self.hover_text_content, True, self.hover_font_color)

		self.hover_text_rect = self.hover_text.get_rect(center=self.hover_pos_text)

		return self.hover_text, self.hover_text_rect

	def render_pressed_text(self, text=None, font=None, size=32, color=bases.BLACK):
		"""Works like render_text() but for the pressed mode of the object."""

		if text is not None:
			self.press_text_content = text
		if font != 0:
			self.press_font = font
		if size is not None:
			self.press_font_size = size
		if color is not None:
			self.press_font_color = color

		# Create the pygame.font.Font object.
		self.press_text = pygame.font.Font(self.press_font, self.press_font_size).render(
			self.press_text_content, True, self.press_font_color)

		# Get the Rect object based on the size and position of the button.
		self.press_text_rect = self.press_text.get_rect(center=self.press_pos_text)

		return self.press_text, self.press_text_rect

	# ----------------------------------------- #
	# DRAWING FUNCTIONS							#
	# ----------------------------------------- #
	def draw(self, surface):
		"""Draw the button while considering the mode of the button."""

		self.rect_data = (self.pos[0], self.pos[1], self.size[0], self.size[1])

		# Ajouter les modes.
		if self.pressed:
			self.draw_pressed(surface)
		elif self.hovered:
			self.draw_hovered(surface)
		else:
			self.draw_basic(surface)

	# The following 3 functions are just acting as placeholder for the self.draw() function.
	def draw_basic(self, surface):
		pass

	def draw_pressed(self, surface):
		pass

	def draw_hovered(self, surface):
		pass

	# ----------------------------------------- #
	# DRAWING FUNCTIONS							#
	# ----------------------------------------- #
	def is_hovered(self, event_pos):
		"""Check if the object is hovered by the event.
		If True, self.hovered == True."""

		hover_test_X = self.pos[0] <= event_pos[0] <= self.pos[0] + self.size[0]
		hover_test_Y = self.pos[1] <= event_pos[1] <= self.pos[1] + self.size[1]

		# If the button is pressed, then the button can't be in hovered mode.
		if hover_test_X and hover_test_Y:
			self.hovered = True
		else:
			self.hovered = False

	def is_pressed(self):
		"""Function called to check if the object is pressed."""

		if self.hovered and not self.pressed:
			self.pressed = True

	def is_released(self):
		"""Function called to check if the object is released and execute the function linked to this event if
		there is one"""

		if self.pressed:
			self.pressed = False
