import pygame
from scenes.scene import Scene
from scenes.game import Game


class MainMenuScene(Scene):
    """Main menu scene"""

    def __init__(self, scene_stack):
        super().__init__(scene_stack)

    def draw(self, screen):
        # draw a simple main menu with buttons
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 500, 400))
        pygame.draw.rect(screen, (255, 0, 0), (100, 100, 300, 100))
        pygame.draw.rect(screen, (0, 255, 0), (100, 200, 300, 100))

        font = pygame.font.SysFont('Arial', 32)
        text = font.render('Play', True, (255, 255, 255))
        screen.blit(text, (200, 125))
        text = font.render('Quit', True, (255, 255, 255))
        screen.blit(text, (200, 225))

        super().draw(screen)

    def update(self):
        # check if the user clicked the play or quit button and change the scene accordingly
        # only check on mouse down to prevent multiple clicks
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 100 < mouse_x < 400 and 100 < mouse_y < 200:
                self.scene_stack.append(Game(self.scene_stack))
            elif 100 < mouse_x < 400 and 200 < mouse_y < 300:
                pygame.quit()
                exit(0)

        super().update()
