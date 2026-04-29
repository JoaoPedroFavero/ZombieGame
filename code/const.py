# Aqui vão as constantes do jogo, como as cores, a largura e altura da tela, etc.

# Window Size
WIN_WIDTH = 768
WIN_HEIGHT = 512

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
PURPLE = (163, 73, 164)


# Menu Options
MENU_OPTIONS = ("Start Game", "Options", "Scoreboard", "Exit")

#Entity Speed Parallax
ENTITY_SPEED = {
    "Level_1bg1": 0,
    "Level_1bg2": 1,
    "Level_1bg3": 2,
    "Level_1bg4": 3,
    "Level_1bg5": 4,
    "Level_1bg6": 5,
    "Level_1bg7": 6,
}

# Memmorize comands
#blit - desenha a imagem na tela, recebe a imagem e a posição (x, y) onde a imagem deve ser desenhada
#flip - atualiza a tela, deve ser chamado depois de desenhar tudo na tela para que as mudanças sejam visíveis
