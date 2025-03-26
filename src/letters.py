import pygame
from src.get_random import get_random
from src.constants import display_height, display_width

letter_height = 50
letter_width = 50

letter = pygame.Rect(get_random(0, display_width - letter_width), get_random(0, display_height - letter_height), letter_width, letter_height)