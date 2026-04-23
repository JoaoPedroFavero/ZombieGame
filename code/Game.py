import pygame
from code.Level import Level
from code.Menu import Menu
from code.const import MENU_OPTIONS, WIN_WIDTH, WIN_HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Zombie Game")

    def run(self):
        while True:
            menu = Menu(self.window)
            selected_option = menu.run()
            if selected_option == MENU_OPTIONS[0]:  # Start Game
                level = Level(self.window, "Level 1")
                level_return = level.run()
            elif selected_option == MENU_OPTIONS[1]:  # Options
                # Show options
                pass
            elif selected_option == MENU_OPTIONS[2]:  # Scoreboard
                # Show scoreboard
                pass
            elif selected_option == MENU_OPTIONS[3]:  # Exit
                # Exit the game
                pygame.quit()
                exit()