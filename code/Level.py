from ast import List
from code.EntityFactory import EntityFactory
from code.Entity import Entity
import pygame


class Level:

    def __init__(self, window, name):
        self.window = window
        self.nome = name
        self.entity_list: List[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(entity_name="Level_1bg"))


    def run(self):
        while True:
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect) # instancias da Entity (surf e rect) para desenhar a imagem na tela
                entity.move()
            pygame.display.flip()

        pass

