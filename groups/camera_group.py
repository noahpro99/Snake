import pygame


class CameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surf = pygame.display.get_surface()

        self.offset = pygame.math.Vector2(0, 0)
        self.half_width = self.display_surf.get_width() // 2
        self.half_height = self.display_surf.get_height() // 2

        self.camera_borders = {'left': 200,
                               'right': 200, 'top': 100, 'bottom': 100}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surf.get_width(
        ) - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.display_surf.get_height(
        ) - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(l, t, w, h)

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_width
        self.offset.y = target.rect.centery - self.half_height

    def box_target_camera(self, target: pygame.sprite.Sprite):
        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']

    # takes a surface and a list of pygame.rects to draw
    def draw(self, surface):

        target = self.sprites()[0]
        self.box_target_camera(target)
        # self.center_target_camera(target)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            surface.blit(sprite.image, offset_pos)
