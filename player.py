import pygame
from circleshape import CircleShape
from shot import Shot
from constants import (
    PLAYER_RADIUS, 
    PLAYER_TURN_SPEED, 
    PLAYER_SPEED, 
    LINE_WIDTH, 
    PLAYER_SHOOT_SPEED, 
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_RESPAWN_TIME,
    PLAYER_ACCELERATION,
    PLAYER_FRICTION
)

class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0.0
        self.velocity = pygame.Vector2(0, 0)
        self.invulnerable_timer = PLAYER_RESPAWN_TIME

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def accelerate(self, dt: float, reverse: bool = False) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if reverse:
            self.velocity -= forward * PLAYER_ACCELERATION * dt
        else:
            self.velocity += forward * PLAYER_ACCELERATION * dt

    def shoot(self) -> None:
        if self.shoot_timer > 0: 
            return 
        
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        
        forward_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward_vector * PLAYER_SHOOT_SPEED
    
    def respawn(self, x: float, y: float) -> None:
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.invulnerable_timer = PLAYER_RESPAWN_TIME

    def update(self, dt: float) -> None:
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        
        if self.invulnerable_timer > 0:
            self.invulnerable_timer -= dt
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # Uses smooth vector acceleration instead of fixed positioning steps
        if keys[pygame.K_w]:
            self.accelerate(dt)
        if keys[pygame.K_s]:
            self.accelerate(dt, reverse=True)
        
        # Apply physics calculations
        self.position += self.velocity * dt
        self.velocity *= PLAYER_FRICTION
        
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def draw(self, screen: pygame.Surface) -> None:
        if self.invulnerable_timer > 0:
            if int(pygame.time.get_ticks() / 100) % 2 == 0:
                return
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
