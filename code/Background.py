import pygame

from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_WIDTH

class Background(Entity):

    def __init__(self, name, position=(0, 0)):
        super().__init__(name=name, position=position)

    def move(self):
        pressed_key = pygame.key.get_pressed()

        background_speed = ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_LSHIFT]:
            background_speed = background_speed * 2.5

        if pressed_key[pygame.K_d]:
            self.rect.centerx -= background_speed
            if self.rect.right < 5:
                self.rect.left = WIN_WIDTH

        if pressed_key[pygame.K_a]:
            self.rect.centerx += background_speed
            if self.rect.left > WIN_WIDTH:
                self.rect.right = 5
