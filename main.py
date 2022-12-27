"""This is a simple game for a player to roam a 2d world and interact with the blocks in it"""
import pygame
from scenes.game import Game
from scenes.main_menu import MainMenuScene


def main():
    # set up pygame
    pygame.init()

    # set up the window
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Game')

    # set fps
    clock = pygame.time.Clock()
    FPS = 60

    scene_stack = []
    scene_stack.append(MainMenuScene(scene_stack))

    while True:

        if len(scene_stack) == 0:
            break
        scene_stack[-1].update()
        scene_stack[-1].draw(screen)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    exit(0)


if __name__ == "__main__":
    main()
