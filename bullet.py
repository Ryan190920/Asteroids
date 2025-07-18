import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,0)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)   
