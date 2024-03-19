# Import modules
import pygame as pyg
pyg.init()
pyg.font.init()

# Custom modules
from classes import Colors, Fonts, Globals
from card import Card

def draw():
    WINDOW = Globals.WINDOW
    VID_BUFFER = Globals.VID_BUFFER
    WIDTH, HEIGHT = Globals.WIDTH, Globals.HEIGHT

    VID_BUFFER.fill(Colors.black)

    # Draw piles
    for pile in Globals.current_piles:
        pile.draw()

    # Draw directions
    VID_BUFFER.blit(Fonts.dir_font.render("/\\", True, Colors.white), (350, 10))
    VID_BUFFER.blit(Fonts.dir_font.render("/\\", True, Colors.white), (750, 10))
    VID_BUFFER.blit(Fonts.dir_font.render("\\/", True, Colors.white), (1150, 10))
    VID_BUFFER.blit(Fonts.dir_font.render("\\/", True, Colors.white), (1550, 10))

    # Draw player's cards
    for card in Globals.player_cards:
        card.draw()

    text_width, text_height = Fonts.dir_font.size("Cards left in draw pile: " + str(len(Globals.draw_pile)))
    VID_BUFFER.blit(Fonts.dir_font.render("Cards left in draw pile: " + str(len(Globals.draw_pile)), True, Colors.white), ((Globals.WIDTH - text_width)/2, (Globals.HEIGHT - text_height)/2))

    WINDOW.blit(pyg.transform.scale(VID_BUFFER, (Globals.WINDOW_WIDTH, Globals.WINDOW_HEIGHT)), (0, 0))
    pyg.display.update()