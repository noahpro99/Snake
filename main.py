"""This is a simple game for a player to roam a 2d world and interact with the blocks in it"""
import pygame
from scenes.game import Game

# set up pygame
pygame.init()

# set up the window
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Game')

# set fps
clock = pygame.time.Clock()
FPS = 60

scene_stack = []
scene_stack.append(Game(scene_stack))

while True:

    scene_stack[-1].update()
    scene_stack[-1].draw(screen)

    pygame.display.update()
    clock.tick(FPS)
