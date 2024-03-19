# Import modules
import pygame as pyg
pyg.init()
pyg.font.init()

# Custom modules
from classes import Colors, Fonts, Globals

class Card:
    def __init__(self, pos, size, value, draggable=False, highlight=True):
        self.x, self.y = pos
        self.width, self.height = size
        self.draggable = draggable
        self.value = value
        self.offset = (0, 0)
        self.highlight = highlight

    def draw(self):
        x, y = self.x, self.y
        width, height = self.width, self.height
        if self.check_collision() and self.highlight:
            width *= 1.1
            height *= 1.1
            x -= 10

        pyg.draw.rect(Globals.VID_BUFFER, Colors.card_colors[self.value // 10], (x, y, width, height))

        text_w, text_h = Fonts.card_font.size(str(self.value))
        Globals.VID_BUFFER.blit(Fonts.card_font.render(str(self.value), True, Colors.white), (self.x + (self.width - text_w) / 2, self.y + (self.height - text_h) / 2))


    def check_collision(self):
        if self.x <= Globals.mouse_position[0] <= self.x + self.width and self.y <= Globals.mouse_position[1] <= self.y + self.height:
            return True
        return False