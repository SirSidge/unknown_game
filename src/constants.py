import pygame

display_height = 1080
display_width = 1920
screen = pygame.display.set_mode((display_width, display_height))
screen_width = screen.get_width()
screen_height = screen.get_height()

ALPHABET_SUM = 100119
ALPHABET = {
    "A": 8200,
    "B": 1500,
    "C": 2800,
    "D": 4300,
    "E": 12700,
    "F": 2200,
    "G": 2000,
    "H": 6100,
    "I": 7000,
    "J": 150,
    "K": 770,
    "L": 4000,
    "M": 2400,
    "N": 6700,
    "O": 7500,
    "P": 1900,
    "Q": 95,
    "R": 6000,
    "S": 6300,
    "T": 9100,
    "U": 2800,
    "V": 980,
    "W": 2400,
    "X": 150,
    "Y": 2000,
    "Z": 74,
}

PLAYER_RADIUS = 40
PLAYER_TURN_SPEED = 200
PLAYER_SPEED = 350