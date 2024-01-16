import pygame
from keylistener import KeyListener
from map import Map
from player import Player
from screen import Screen

pygame.init()

# Initialize game components
key_listener = KeyListener()
game_map = Map(800, 600)
player = Player(400, 300)
game_screen = Screen(800, 600)

# Main game loop
while True:
    key_listener.update()
    player.update(key_listener.keys)

    game_screen.clear()
    # Add code to update/draw map and player on the screen

    game_screen.update()