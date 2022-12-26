import pygame
import os


class Block(pygame.sprite.Sprite):
    """Block class"""

    def __init__(self, x, y, image_dir, dimensions=(50, 50), group=None):
        super().__init__(group)
        self.image = pygame.image.load(
            os.path.join(image_dir))
        self.image = pygame.transform.scale(self.image, dimensions)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        """Update the block's position"""
        pass
