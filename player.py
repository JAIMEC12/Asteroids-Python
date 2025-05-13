from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED
import pygame

from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0 
    
    def triangle(self):
        foward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + foward * self.radius
        b = self.position - foward * self.radius - right
        c = self.position - foward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self,dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0: 
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN 
    
    def move (self,dt):
        foward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += foward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)
        new_shot.velocity = pygame.Vector2(0.1).rotate(self.rotation) * PLAYER_SHOOT_SPEED