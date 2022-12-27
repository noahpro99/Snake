import pygame
import os


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, dimensions, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(
            os.path.join('assets\images', 'enemy', '1.png'))
        self.image = pygame.transform.scale(self.image, dimensions)
        self.rect = self.image.get_rect(center=(x, y))

        self.direction = pygame.math.Vector2(0, 0)
        self.health = 100

        self.walk_speed = 3
        self.preparing_to_attack = False
        self.is_attacking = False
        self.attack_delay = 30

    def update(self):
        """Walk towards the player and attack if close enough, first prepare to attack and stop moving and change the color of the sprite then attack after a delay and change the color back"""

        player_pos = self.groups()[0].sprites()[0].rect.center
        self.vector_to_player = pygame.math.Vector2(
            player_pos) - self.rect.center

        if not self.preparing_to_attack and not self.is_attacking:
            if self.vector_to_player.length() > 0:
                self.direction = self.vector_to_player.normalize()

            if self.vector_to_player.length() < 100:
                self.preparing_to_attack = True
                self.direction = pygame.math.Vector2(0, 0)
            else:
                self.rect.move_ip(self.direction * self.walk_speed)
                self.preparing_to_attack = False

        if self.preparing_to_attack:
            self.attack_delay -= 1
            if self.attack_delay <= 0:
                print('enemy finished preparing to attack')
                self.is_attacking = True
                self.preparing_to_attack = False
                self.attack_delay = 5

        if self.is_attacking:
            self.attack_delay -= 1
            if self.attack_delay <= 0:
                print('enemy finished attacking')
                self.is_attacking = False
                self.attack_delay = 60
