import pygame
import os


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, dimensions, health_bar, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(
            os.path.join('assets\images', 'enemy', '1.png'))
        self.image = pygame.transform.scale(self.image, dimensions)
        self.rect = self.image.get_rect(center=(x, y))

        self.direction = pygame.math.Vector2(0, 0)
        self.health = 100

        self.walk_speed = 2
        self.preparing_to_attack = False
        self.is_attacking = False
        self.health_bar = health_bar

    def update(self):
        """Walk towards the player and attack"""

        if not self.preparing_to_attack and not self.is_attacking:
            player_pos = self.groups()[0].sprites()[0].rect.center
            self.direction = pygame.math.Vector2(player_pos) - self.rect.center
            if self.direction.length() > 0:
                self.direction = self.direction.normalize()
            self.rect.move_ip(self.direction * self.walk_speed)

        # if the enemy is close enough to the player then prepare to attack and stop moving towards the player
        if self.rect.colliderect(self.groups()[0].sprites()[0].rect) and not self.preparing_to_attack and not self.is_attacking:
            self.preparing_to_attack = True
            self.is_attacking = False

        if self.preparing_to_attack:
            # start attacking after 1 second
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            self.preparing_to_attack = False
            self.is_attacking = True

        if self.is_attacking:
            # stop attacking after 1 second
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            self.preparing_to_attack = False
            self.is_attacking = False
