import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shots
from logger import log_state, log_event
from score import Score
from starfield import StarField

def main():

    pygame.init()
    pygame.display.set_caption("Asteroids - by StressFree Gaming")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    starfield = StarField(SCREEN_WIDTH, SCREEN_HEIGHT, num_stars=300, layers=3)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shots.containers = (shots, updatable, drawable)

    score = Score()

    dt = 0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                score.save()
                return

        updatable.update(dt)

        try:
            parallax_x = player.velocity.x * dt * 0.5
            parallax_y = player.velocity.y * dt * 0.5
        except Exception:
            parallax_x = parallax_y = 0.0
        starfield.update(dt, parallax_x, parallax_y)

        for asteroid in asteroids:
            if player.check_collisions(asteroid):
                print(f"Game Over!")
                print(f"Your score: {score.value}, High score: {score.high}")
                score.save()
                pygame.quit()
                exit()

            for shot in shots:
                if shot.check_collisions(asteroid):
                    log_event("asteroid_shot")
                    # award points (use asteroid.points if present, fallback to heuristic)
                    pts = getattr(asteroid, "points", None)
                    if pts is None:
                        # heuristic: smaller asteroids -> more points; tweak to your game
                        radius = getattr(asteroid, "radius", None) or getattr(asteroid, "r", 10)
                        pts = max(20, int(100 / max(1, radius)))
                    score.add(pts)

                    asteroid.split()
                    shot.kill() # remove the shot upon collision

        screen.fill("black")
        starfield.draw(screen)

        for obj in drawable:
            obj.draw(screen)

        # draw score last so it sits on top
        score.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()