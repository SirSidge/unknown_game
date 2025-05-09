import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.col_left = self.position[0] - PLAYER_RADIUS
        self.col_right = self.position[0] + PLAYER_RADIUS
        self.col_top = self.position[1] - PLAYER_RADIUS
        self.col_bot = self.position[1] + PLAYER_RADIUS
        self.pos = {
            "left": self.col_left,
            "right": self.col_right,
            "top": self.col_top,
            "bot": self.col_bot,
        }

    def draw(self, screen):
        pygame.draw.polygon(screen, "red", self.triangle())

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.col_left = self.position[0] - PLAYER_RADIUS
        self.col_right = self.position[0] + PLAYER_RADIUS
        self.col_top = self.position[1] - PLAYER_RADIUS
        self.col_bot = self.position[1] + PLAYER_RADIUS
        self.pos = {
            "left": self.col_left,
            "right": self.col_right,
            "top": self.col_top,
            "bot": self.col_bot,
        }