# Import modules
import contextlib
with contextlib.redirect_stdout(None):
    import pygame as pyg
import subprocess
import random
import sys
import os


# Custom modules
import draw
from classes import Globals
from card import Card

# Initialize window
pyg.init()
info_object = pyg.display.Info()
Globals.WINDOW_WIDTH, Globals.WINDOW_HEIGHT = info_object.current_w, info_object.current_h
Globals.WIDTH, Globals.HEIGHT = (1920, 1080)
Globals.WINDOW = pyg.display.set_mode((Globals.WINDOW_WIDTH, Globals.WINDOW_HEIGHT))
pyg.display.set_caption("The Game")


def Main():
    os.system("cls")

    for i in range(2, 100):
        Globals.draw_pile += [i]

    Globals.current_piles += [Card((Globals.WIDTH/2 - 725, 50), (250, 400), 1), Card((Globals.WIDTH/2 - 325, 50), (250, 400), 1), Card((Globals.WIDTH/2 + 75, 50), (250, 400), 100), Card((Globals.WIDTH/2 + 475, 50), (250, 400), 100)]
    for i in range(8):
        card = draw_card()
        Globals.player_cards += [Card((0, 0), (200, 400), card, True)]
        update_cards()

    played_cards = 0

    while True:
        # Add new cards to player's hand
        if played_cards == 2:
            played_cards = 0
            card = draw_card()
            Globals.player_cards += [Card((0, 0), (200, 400), card, True)]
            card = draw_card()
            Globals.player_cards += [Card((0, 0), (200, 400), card, True)]
            update_cards()

        elif played_cards == 1 and len(Globals.draw_pile) == 0:
            card = draw_card()
            Globals.player_cards += [Card((0, 0), (200, 400), card, True)]
            update_cards()

        # Update mouse position
        Globals.mouse_position = pyg.mouse.get_pos()
        if Globals.dragging_card is not None:
            Globals.dragging_card.x = Globals.mouse_position[0] - Globals.dragging_card.offset[0]
            Globals.dragging_card.y = Globals.mouse_position[1] - Globals.dragging_card.offset[1]

        for event in pyg.event.get():
            # If event is quit
            if event.type == pyg.QUIT:
                pyg.quit()
                sys.exit()

            # If event is a key press
            elif event.type == pyg.KEYDOWN:
                key = event.key

                # Kill key
                if key == pyg.K_F1:
                    pyg.quit()
                    sys.exit()

                elif key == pyg.K_F5:
                    return "Reset"
                
            # If event is mouse click
            elif event.type == pyg.MOUSEBUTTONDOWN and event.button == 1:
                for card in Globals.player_cards:
                    if card.check_collision() and card.draggable:
                        Globals.dragging_card = card
                        card.offset = (Globals.mouse_position[0] - card.x, Globals.mouse_position[1] - card.y)

            elif event.type == pyg.MOUSEBUTTONUP:

                # Check the four piles
                for i in range(len(Globals.current_piles)):
                    pile = Globals.current_piles[i]
                    # Check the first two piles (increasing)
                    if i <= 1:
                        if pile.check_collision() and (pile.value < Globals.dragging_card.value or pile.value - 10 == Globals.dragging_card.value):
                            pile.value = Globals.dragging_card.value
                            Globals.player_cards.remove(Globals.dragging_card)
                            played_cards += 1

                    # Check the last two piles (decreasing)
                    else:
                        if pile.check_collision() and (pile.value > Globals.dragging_card.value or pile.value + 10 == Globals.dragging_card.value):
                            pile.value = Globals.dragging_card.value
                            Globals.player_cards.remove(Globals.dragging_card)
                            played_cards += 1

                Globals.dragging_card = None
                update_cards()


        draw.draw()
        Globals.clock.tick(Globals.FPS)


def draw_card():
    card = random.choice(Globals.draw_pile)
    Globals.draw_pile.remove(card)
    return card

def update_cards():
    cards = Globals.player_cards
    sort_cards()
    
    offset = Globals.WIDTH / 2- (230 * len(cards) / 2)
    for i in range(len(cards)):
        cards[i].x, cards[i].y = offset, 800
        offset += 230

def sort_cards():
    cards = Globals.player_cards
    n = len(cards)
    for i in range(n):
        for j in range(0, n - i - 1):
             
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found 
            #is greater than the adjacent element
            if cards[j].value > cards[j + 1].value:
                cards[j], cards[j + 1] = cards[j + 1], cards[j]

if __name__ == "__main__":
    ret_val = Main()
    while ret_val == "Reset":
        Globals.draw_pile = []
        Globals.current_piles = []
        Globals.player_cards = []
        Globals.turn = 1

        ret_val = Main()