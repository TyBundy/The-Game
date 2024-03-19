# Import modules
import pygame as pyg
pyg.init()

class Fonts:
    card_font = pyg.font.SysFont("consolas", 30)
    dir_font = pyg.font.SysFont("consolas", 20)

class Colors:
    black = (25, 25, 25)
    dark_gray = (60, 60, 60)
    dark_blue = (0, 0, 150)
    aqua = (0, 200, 200)
    pink = (200, 0, 200)
    dark_green = (0, 100, 0)
    light_gray = (130, 130, 130)
    purple = (120, 0, 200)
    yellow = (200, 200, 0)
    light_blue = (170, 200, 230)
    green = (0, 200, 0)
    white = (255, 255, 255)

    card_colors = (yellow, light_blue, dark_gray, dark_blue, green, aqua, pink, dark_green, light_gray, purple, purple)

class Globals:
    WINDOW = None
    VID_BUFFER = pyg.Surface((1920, 1080))
    WIDTH, HEIGHT = (0, 0)
    WINDOW_WIDTH, WINDOW_HEIGHT = (0, 0)


    FPS = 60
    clock = pyg.time.Clock()
    mouse_position = (0, 0)

    dragging_card = None

    draw_pile = []
    current_piles = []
    player_cards = []
    turn = 1