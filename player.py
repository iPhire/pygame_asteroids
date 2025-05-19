import pygame, constants
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x,y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.timer = 0
        
        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt
 
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
            self.shoot(self.shots_group)
        self.timer = self.timer - dt    
            

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self, shots):
        if not self.timer > 0:
            shot_obj = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
            shot_obj.velocity = pygame.Vector2(0,1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
            shots.add(shot_obj)
            self.timer = constants.PLAYER_SHOOT_COOLDOWN
