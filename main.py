# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys, pygame, constants, player, asteroid, asteroidfield, shot
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    dt = 0
    width, height = screen.get_size()
    x = width / 2
    y = height / 2
    print("Starting Asteroids!")
    print(f'Screen width: {constants.SCREEN_WIDTH}\nScreen height: {constants.SCREEN_HEIGHT}')

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player_obj = Player(x,y, shots)
    asteroidfield_obj = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)
        for asteroid_obj in asteroids:
            if asteroid_obj.collision(player_obj):
                print('Game over!')
                sys.exit()
            for shot in shots:
                if asteroid_obj.collision(shot):
                    shot.kill()
                    asteroid_obj.split(asteroids)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()