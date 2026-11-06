from circleshape import CircleShape
import pygame
class Asteroid(CircleShape): 
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

        def draw(self, screen: pygame.Surface) -> None:
            # Draw a circle outline using the asteroid's position and radius
            pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

        def update(self, dt: float) -> None:
            # Move in a straight line at constant velocity scaled by delta time
            self.position += self.velocity * dt
