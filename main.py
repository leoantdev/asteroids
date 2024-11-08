import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidField = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(x, y) 

    while True:
        game_over = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in asteroids:
            if obj.collision_check(player):
                print("Game over!")
                sys.exit() 

            for bullet in shots:
                if obj.collision_check(bullet):
                    obj.split()
                    bullet.kill()

        if game_over == True:
            break

        for obj in updatable:
            obj.update(dt)

        screen.fill((0, 0 ,0))

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
            
if __name__ == "__main__":
    main()
