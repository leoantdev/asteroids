import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            direction_1 = self.velocity.rotate(angle) 
            direction_2 = self.velocity.rotate(-angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_1.velocity = direction_1 * 1.2 
            asteroid_2.velocity = direction_2 * 1.2 

        self.kill()

        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        