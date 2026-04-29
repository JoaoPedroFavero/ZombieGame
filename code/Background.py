import pygame

from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_WIDTH

class Background(Entity):

    def __init__(self, name, position=(0, 0)):
        super().__init__(name=name, position=position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right < 0:
            self.rect.left = WIN_WIDTH
                    
