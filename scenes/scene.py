from typing import List
import pygame
import os
# scene class


class Scene(object):
    """Base class for all scenes in a scene stack"""

    def __init__(self, scene_stack):
        self.sprite_groups: List[pygame.sprite.Group] = []
        self.image_dir = os.path.join("assets", "images")
        self.scene_stack = scene_stack

    def update(self):
        """Update the scene"""
        for group in self.sprite_groups:
            group.update()

    def draw(self, screen):
        """Draw the scene"""
        for group in self.sprite_groups:
            group.draw(screen)
