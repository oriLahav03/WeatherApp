import pygame


class Button:
    """
    The class Button represents a button.
    """
    def __init__(self, pos, size, text):
        self.button = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.city = ''
        self.text = text

    def draw(self, window):
        """
        The function draws the button.
        :param window: the main window
        :type window: pygame.Surface
        :return: None
        :rtype: None
        """
        font = pygame.font.SysFont('comicsans', 20, True)
        txt_surface = font.render(self.text, True, pygame.Color('black'))
        # Resize the box if the text is too long.
        width = max(70, txt_surface.get_width() + 10)
        self.button.w = width
        height = max(30, txt_surface.get_height() + 10)
        self.button.h = height
        # Blit the text.
        window.blit(txt_surface, (self.button.x + 5, self.button.y + 5))
        # Blit the button rect.
        pygame.draw.rect(window, pygame.Color('lightskyblue3'), self.button, 2)
