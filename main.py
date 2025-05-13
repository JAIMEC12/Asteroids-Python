from asteroid import Asteroids
import pygame
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH 
from player import Player
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatables = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroids.containers = (asteroids, updatables, drawable)
    Player.containers = (updatables,drawable)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, drawable, updatables)

    player= Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
    print("Starting Asteroids")
    print("Screen size:", SCREEN_WIDTH, "x", SCREEN_HEIGHT)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), None, 0)
        for drawing in drawable:
            drawing.draw(screen)
        updatables.update(dt)
        for asteroid in asteroids:
            if(asteroid.collide(player)):
                print("Game Over!")
                return
            for shot in shots:
                if(shot.collide(asteroid)):
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()