import pygame
import random
from constants import LINE_WIDTH

class Particle(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...] = ()

    def __init__(self, position: pygame.Vector2, velocity: pygame.Vector2, lifetime: float):
        if hasattr(self, "containers") and self.containers:
            super().__init__(*self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)
        self.lifetime = lifetime
        self.timer = 0.0

    def update(self, dt: float) -> None:
        self.timer += dt
        if self.timer >= self.lifetime:
            self.kill()
            return
        self.position += self.velocity * dt

    def draw(self, screen: pygame.Surface) -> None:
        # Calculate fade out based on remaining lifetime
        alpha = max(0, int(255 * (1.0 - (self.timer / self.lifetime))))
        # Small 2x2 particle point or line drawing
        color = (alpha, alpha, alpha)
        pygame.draw.line(screen, color, self.position, self.position + self.velocity * 0.05, LINE_WIDTH)
