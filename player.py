import pygame
from circleshape import CircleShape
from bullet import Shot
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
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
            self.shoot()

        self.cooldown -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.cooldown > 0:
            return
        self.cooldown = PLAYER_SHOOT_COOLDOWN
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.shots_group.add(new_shot)
        
