import pygame

from get_random import get_random
from constants import screen_width, screen_height, ALPHABET

letter_size = 40

class Letter(pygame.sprite.Sprite):
    def __init__(self, color, char):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.color = color
        self.char = char
        self.pos = [get_random(0, screen_width - letter_size), get_random(0, screen_height - letter_size)]
        self.rect = pygame.rect.Rect(self.pos[0], self.pos[1], letter_size, letter_size)
        self.font = pygame.font.Font.render((pygame.font.SysFont("Arial", 48, bold=True)), self.char, 0, "white")
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit((self.font), (self.pos[0], self.pos[1]))

    def collision(self):
        #print("Collision detected")
        self.kill()

    def update(self):
        self.col_left = self.pos[0] - (letter_size / 2)
        self.col_right = self.pos[0] + (letter_size / 2)
        self.col_top = self.pos[1] - (letter_size / 2)
        self.col_bot = self.pos[1] + (letter_size / 2)