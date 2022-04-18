import pygame


class TextBox:
    """
    The class TextBox represents a text box.
    """
    def __init__(self, pos, size, text='', font_size=20, frame=True):
        self.input_box = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.font_size = font_size
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.active = False
        self.text = text
        self.frame = frame

    def draw(self, window):
        """
        The function draws the text box.
        :param window: the main window
        :type window: pygame.Surface
        :return: None
        :rtype: None
        """
        font = pygame.font.SysFont('comicsans', self.font_size, True)
        txt_surface = font.render(self.text, True, pygame.Color('black'))
        # Resize the box if the text is too long.
        width = max(150, txt_surface.get_width() + 10)
        self.input_box.w = width
        height = max(30, txt_surface.get_height() + 10)
        self.input_box.h = height
        # Blit the text.
        window.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
        # Blit the input_box rect.
        if self.frame:
            pygame.draw.rect(window, self.color, self.input_box, 2)
