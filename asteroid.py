from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import random
from logger import log_event
class Asteroid(CircleShape): 
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        # Draw a circle outline using the asteroid's position and radius
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # Move in a straight line at constant velocity scaled by delta time
        self.position += self.velocity * dt
    
    def split(self) -> None:
        # Immediately destroy this asteroid from all sprite groups
        self.kill()

        # If it's already a small asteroid, we are done
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Log the split event for testing purposes
        log_event("asteroid_split")

        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new velocities by splitting and rotating the current path
        # Scale up the speed slightly (e.g., multiply by 1.2) to make the game dynamic!
        velocity_a = self.velocity.rotate(random_angle) * 1.2
        velocity_b = self.velocity.rotate(-random_angle) * 1.2

        # Compute the radius for the two smaller fragments
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn the two new smaller asteroids
        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = velocity_a

