import pygame
import colorsys
from constants import *
from circleshape import CircleShape

class Shots(CircleShape):

    _next_hue = 0  # give each shot a different colour

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # assign a rainbow colour based on the shared hue and advance it
        h = (Shots._next_hue % 360) / 360.0
        Shots._next_hue += 28  # step to get different colours
        r, g, b = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        self.color = (int(r * 255), int(g * 255), int(b * 255))

    def draw(self, screen):
        # convert position to ints for pygame.draw
        pos = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, self.color, pos, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt