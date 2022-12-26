"""Player class"""

import pygame
import os


class Player(pygame.sprite.Sprite):
    """Player class"""

    def __init__(self, x, y, dimensions=(72, 86), *groups):
        super().__init__(*groups)
        self.direction = pygame.math.Vector2(0, 0)
        self.walk_speed = 3

        walk_img = (pygame.image.load(
            os.path.join('assets\images', 'Knight_1', 'Walk.png')))
        attack_img = (pygame.image.load(
            os.path.join('assets\images', 'Knight_1', 'Attack 1.png')))

        # split 8 frames from the image
        self.walk_frames = [walk_img.subsurface(
            (x, 0, 72, 86)) for x in range(0, 200, 72)]
        self.walk_frames = [pygame.transform.scale(
            frame, dimensions) for frame in self.walk_frames]

        # split 5 frames from the image
        self.attack_frames = [attack_img.subsurface(
            (x, 0, 72, 86)) for x in range(0, 200, 72)]
        self.attack_frames = [pygame.transform.scale(
            frame, dimensions) for frame in self.attack_frames]

        self.image = self.walk_frames[0]
        self.current_frame = 0
        self.rect = self.image.get_rect(center=(x, y))
        self.facing_right = True
        self.is_attacking = False

        self.health = 100

    def input(self, keys):
        """Handle player input"""
        self.direction = pygame.math.Vector2(0, 0)
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        if keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_right = False
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.facing_right = True

    def update(self):
        """Update the player's position"""
        self.input(pygame.key.get_pressed())
        self.rect.move_ip(self.direction * self.walk_speed)
        self.animate()

    def animate(self):
        """Animate the player"""
        # only animate if the player is moving in a direction
        # only animate every 5 frames
        # flip the image if the player is moving left
        if self.is_attacking:
            self.current_frame += 1
            if self.current_frame >= len(self.attack_frames) * 5:
                self.current_frame = 0
                self.is_attacking = False
            self.image = self.attack_frames[self.current_frame // 5]
        elif self.direction.x != 0 or self.direction.y != 0:
            self.current_frame += 1
            if self.current_frame >= len(self.walk_frames) * 5:
                self.current_frame = 0
            self.image = self.walk_frames[self.current_frame // 5]
        else:
            self.image = self.walk_frames[0]

        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

    def attack(self):
        """Attack"""
        self.is_attacking = True
