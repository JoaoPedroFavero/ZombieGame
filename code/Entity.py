from abc import ABC, abstractmethod
import pygame

from code.const import ENEMY_HEALTH, PLAYER_HEALTH


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load(f"Assets/{name}.png")
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

        if name.startswith("Player"):
            self.health = PLAYER_HEALTH

        elif name.startswith("Zombie"):
            self.health = ENEMY_HEALTH
        else:
            self.health = 1

