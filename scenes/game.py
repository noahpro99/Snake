import os
from random import randint
from typing import List
import pygame
from groups.camera_group import CameraGroup
from sprites.player import Player
from sprites.enemy import Enemy
from scenes.pause_menu import PauseMenu


class Game():

    def __init__(self, scene_stack):
        self.scene_stack = scene_stack

        self.camera_group = CameraGroup()

        self.background = pygame.image.load(os.path.join(
            "assets/images", "background", "1.png"))
        self.background = pygame.transform.scale(self.background, (1500, 1500))

        self.player = Player(100, 100, (50, 50), self.camera_group)

        self.enemies = pygame.sprite.Group()

        # add random enemies around the player but not too close
        for i in range(8):
            x = randint(-500, 500)
            y = randint(-500, 500)

            enemy = Enemy(x, y, (50, 50), self.camera_group,
                          self.enemies)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        # draw the player health bar
        pygame.draw.rect(screen, (255, 0, 0), (10, 10, 100, 20))
        pygame.draw.rect(screen, (0, 255, 0), (10, 10, self.player.health, 20))

        self.camera_group.draw(screen)

        # draw the enemies health bars
        for enemy in self.enemies.sprites():
            pygame.draw.rect(screen, (255, 0, 0),
                             (enemy.rect.x, enemy.rect.y - 10, 50, 5))
            pygame.draw.rect(screen, (0, 255, 0), (enemy.rect.x,
                             enemy.rect.y - 10, enemy.health, 5))

    def update(self):
        # event loop
        events: List[pygame.event.Event] = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.scene_stack.append(PauseMenu(self.scene_stack))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.player.attack()

        # continually spawn new enemies
        if len(self.camera_group.sprites()) < 10:
            x = randint(-500, 500)
            y = randint(-500, 500)
            enemy = Enemy(x, y, (50, 50), self.camera_group, self.enemies)

        for enemy in self.enemies.sprites():
            if enemy.is_attacking and enemy.rect.colliderect(self.player.rect):
                self.do_damage(10, self.player)

            if self.player.is_attacking and self.player.rect.colliderect(enemy.rect):
                self.do_damage(10, enemy)

        self.camera_group.update()

    def do_damage(self, damage, target):
        target.health -= damage
        if target.health <= 0:
            target.kill()
