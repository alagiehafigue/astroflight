import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot 
from particle import Particle



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}\n Screen width: {SCREEN_WIDTH}\n Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    dt = 0.0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ui_font = pygame.font.SysFont("Courier", 24, bold=True)
    x = SCREEN_WIDTH / 2 
    y = SCREEN_HEIGHT / 2

    score = 0
    lives = 3

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    particles = pygame.sprite.Group()
   
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    Particle.containers = (updatable, drawable, particles)


    player = Player(x, y)
    asteroid_field = AsteroidField()
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        updatable.update(dt)
        for asteroid in asteroids: 
             if player.invulnerable_timer <= 0 and asteroid.collides_with(player):
                lives -= 1
                log_event("player_died")
                asteroid.explode()
                asteroid.kill()
                
                if lives <= 0:
                    log_event("game_over")
                    print(f"Game Over! Final Score: {score}")
                    sys.exit()
                else:
                    player.respawn(x, y)
            
        for shot in shots: 
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    score += int(1000 / asteroid.radius)
                    shot.kill()
                    asteroid.split()
        log_state()
        
        screen.fill("black")

        for obj in drawable: 
            obj.draw(screen)

        score_text = ui_font.render(f"SCORE: {score}", True, "white")
        lives_text = ui_font.render(f"LIVES: {lives}", True, "white")
        screen.blit(score_text, (20, 20))
        screen.blit(lives_text, (SCREEN_WIDTH - 150, 20))

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
