from ast import List
from tkinter import font
from pygame import surface
from pygame import rect
from code.EntityFactory import EntityFactory
from code.Entity import Entity
import pygame
from code.const import WHITE, WIN_WIDTH


class Level:

    def __init__(self, window, name):
        self.window = window
        self.nome = name
        self.entity_list: List[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(entity_name="Level_1bg"))
        self.entity_list.append(EntityFactory.get_entity(entity_name="PlayerIdle"))
        self.entity_list.append(EntityFactory.get_entity(entity_name="ZombieIdle", position=(WIN_WIDTH - 200, 280)))

    def run(self):
        pygame.mixer.music.load("./Assets/level1Music.wav")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(30)
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect) # instancias da Entity (surf e rect) para desenhar a imagem na tela
                entity.move()
                
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    
            self.level_text("Level 1 - Cidade Velha", 30, WHITE, (WIN_WIDTH - 650, 20))
            self.level_text(f"FPS: {int(clock.get_fps())}", 20, WHITE, (WIN_WIDTH - 730, 40))

            pygame.display.flip()


    def level_text(self, text: str, font_size: int, color: tuple, position: tuple):
        text_font: font = pygame.font.SysFont("Lucida Sans Typewriter", font_size)
        text_surf: surface = text_font.render(text, True, color).convert_alpha()
        text_rect: rect = text_surf.get_rect(center = position)
        self.window.blit(source=text_surf, dest=text_rect)

