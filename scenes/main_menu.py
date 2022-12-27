import os
from typing import List
import pygame
from scenes.game import Game


class MainMenuScene():
    """Main menu scene"""

    def __init__(self, scene_stack):
        self.scene_stack = scene_stack

    def draw(self, screen):

        # use background image instead of a solid color
        background = pygame.image.load(os.path.join(
            "assets/images", "menu", "1.png"))
        background = pygame.transform.scale(background, (1280, 720))
        screen.blit(background, (0, 0))

        # draw a simple main menu with buttons over the whole screen
        pygame.draw.rect(screen, (255, 0, 0), (100, 100, 300, 100))
        pygame.draw.rect(screen, (0, 255, 0), (100, 300, 300, 100))

        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Start Game', False, (0, 0, 0))
        screen.blit(textsurface, (100, 100))
        textsurface = myfont.render('Quit', False, (0, 0, 0))
        screen.blit(textsurface, (100, 300))

    def update(self):
        # event loop
        events: List[pygame.event.Event] = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    self.scene_stack.append(Game(self.scene_stack))
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if 100 < mouse_pos[0] < 400 and 100 < mouse_pos[1] < 200:
                        self.scene_stack.append(Game(self.scene_stack))

                    if 100 < mouse_pos[0] < 400 and 300 < mouse_pos[1] < 400:
                        pygame.quit()
                        quit()
