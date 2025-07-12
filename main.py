import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from bullet import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots)

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")
        for drawables in drawable:
            drawables.draw(screen)
        updatable.update(dt)
        for shot in shots:
            shot.draw(screen)
            shot.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.is_colliding_with(asteroid):
                    asteroid.split()
                    shot.kill()
        for asteroid in asteroids:
            if player.is_colliding_with(asteroid):
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
