import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Zombie Game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

