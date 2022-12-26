import time
import pygame
from scenes.scene import Scene


class PauseMenu(Scene):
    def __init__(self, scene_stack):
        super().__init__(scene_stack)

    def draw(self, screen):
        # add a title to the pause menu
        font = pygame.font.SysFont('Arial', 32)
        text = font.render('Pause Menu', True, (255, 255, 255))
        screen.blit(text, (100, 50))

        # draw a simple main menu with buttons
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 500, 400))
        pygame.draw.rect(screen, (255, 0, 0), (100, 100, 300, 100))
        pygame.draw.rect(screen, (0, 255, 0), (100, 200, 300, 100))

        font = pygame.font.SysFont('Arial', 32)
        text = font.render('Resume', True, (255, 255, 255))
        screen.blit(text, (200, 125))
        text = font.render('Quit', True, (255, 255, 255))
        screen.blit(text, (200, 225))

        super().draw(screen)

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 100 < mouse_x < 400 and 100 < mouse_y < 200:
                self.scene_stack.pop()
            elif 100 < mouse_x < 400 and 200 < mouse_y < 300:
                # leave to main menu
                self.scene_stack.clear()
                from scenes.main_menu import MainMenuScene
                self.scene_stack.append(MainMenuScene(self.scene_stack))
                # small hack to prevent the user from clicking the button multiple times
                # since the button is in the same position as the main menu button
                time.sleep(0.1)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scene_stack.pop()
        super().update()
