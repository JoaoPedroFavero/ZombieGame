import pygame
from code.const import MENU_OPTIONS, WIN_WIDTH, WHITE, GRAY
from pygame import font
from pygame import surface
from pygame import rect


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./Assets/menuBG.png")
        self.rect = self.surf.get_rect()

    def run(self):
        pygame.mixer.music.load("./Assets/menuMusic.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text("Zombie Game", 100, WHITE, ((WIN_WIDTH / 2), 80))
            self.menu_text("developed by João Pedro Fávero - UR 4761148", 20, GRAY, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTIONS)):
                self.menu_text(MENU_OPTIONS[i], 40, WHITE, ((WIN_WIDTH / 2), 260 + (i * 40)))

            pygame.display.flip()
           
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
    
    def menu_text(self, text: str, font_size: int, color: tuple, position: tuple):
        text_font: font = pygame.font.SysFont("Lucida Sans Typewriter", font_size)
        text_surf: surface = text_font.render(text, True, color).convert_alpha()
        text_rect: rect = text_surf.get_rect(center = position)
        self.window.blit(source=text_surf, dest=text_rect)
