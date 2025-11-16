import pygame
import random
from constants import *
from circleshape import CircleShape
from logger import log_state, log_event

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "black", self.position, self.radius)
        pygame.draw.circle(screen, "grey", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            asteroids = []
            log_event("asteroid_split")
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_angle = random.uniform(20, 50)
            
            for sign in (1, -1):
                new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                new_asteroid.velocity = self.velocity.rotate(new_angle * sign) * 1.2
                asteroids.append(new_asteroid)
    
            return asteroids