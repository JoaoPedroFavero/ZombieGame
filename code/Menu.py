import pygame
from code.const import MENU_OPTIONS, WIN_WIDTH, WHITE, GRAY, PURPLE
from pygame import font
from pygame import surface
from pygame import rect


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./Assets/menuBG.png")
        self.rect = self.surf.get_rect()

    def run(self):
        menu_selected = 0
        pygame.mixer.music.load("./Assets/menuMusic.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text("Zombie Game", 100, WHITE, ((WIN_WIDTH / 2), 80))
            self.menu_text("developed by João Pedro Fávero - UR 4761148", 20, GRAY, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_selected:
                    self.menu_text(MENU_OPTIONS[i], 40, PURPLE, ((WIN_WIDTH / 2), 260 + (i * 40)))
                else:
                    self.menu_text(MENU_OPTIONS[i], 40, WHITE, ((WIN_WIDTH / 2), 260 + (i * 40)))

            pygame.display.flip()
           
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        menu_selected = (menu_selected - 1) % len(MENU_OPTIONS)
                    elif event.key == pygame.K_DOWN:
                        menu_selected = (menu_selected + 1) % len(MENU_OPTIONS)

                    elif event.key == pygame.K_RETURN:
                        if MENU_OPTIONS[menu_selected] == "Start Game":
                            return MENU_OPTIONS[menu_selected]
                        
                        elif MENU_OPTIONS[menu_selected] == "Options":
                            return MENU_OPTIONS[menu_selected]
                        
                        elif MENU_OPTIONS[menu_selected] == "Scoreboard":
                            return MENU_OPTIONS[menu_selected]
                        
                        elif MENU_OPTIONS[menu_selected] == "Exit":
                            pygame.quit()
                            exit()
                    
    
    def menu_text(self, text: str, font_size: int, color: tuple, position: tuple):
        text_font: font = pygame.font.SysFont("Lucida Sans Typewriter", font_size)
        text_surf: surface = text_font.render(text, True, color).convert_alpha()
        text_rect: rect = text_surf.get_rect(center = position)
        self.window.blit(source=text_surf, dest=text_rect)
