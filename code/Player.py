import pygame

from code.Entity import Entity
from code.const import TAMANHO_PLAYER

class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        
        self.frames_idle = []
        self.frames_walk = []
        self.frames_walk_back = []
        self.frames_run = []
        self.frames_run_back = []

        self.frame_index = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_delay = 150

        for image in range(6):
            idle = pygame.image.load(f"Assets/PlayerIdle{image+1}.png").convert_alpha()
            idle = pygame.transform.scale(idle, TAMANHO_PLAYER)
            self.frames_idle.append(idle)

        for image in range(8):
            walk = pygame.image.load(f"Assets/PlayerWalk{image+1}.png").convert_alpha()
            walk = pygame.transform.scale(walk, TAMANHO_PLAYER)
            self.frames_walk.append(walk)

        for image in range(8):
            walk_back = pygame.image.load(f"Assets/PlayerWalkBack{image+1}.png").convert_alpha()
            walk_back = pygame.transform.scale(walk_back, TAMANHO_PLAYER)
            self.frames_walk_back.append(walk_back)

        for image in range(8):
            run = pygame.image.load(f"Assets/PlayerRun{image+1}.png").convert_alpha()
            run = pygame.transform.scale(run, TAMANHO_PLAYER)
            self.frames_run.append(run)

        for image in range(8):
            run_back = pygame.image.load(f"Assets/PlayerRunBack{image+1}.png").convert_alpha()
            run_back = pygame.transform.scale(run_back, TAMANHO_PLAYER)
            self.frames_run_back.append(run_back)



    def move(self):
        image_now = pygame.time.get_ticks()

        if image_now - self.last_update > self.animation_delay:
            self.last_update = image_now
            self.frame_index += 1

        if(self.frame_index >= len(self.frames_idle)):
            self.frame_index = 0

        self.surf = self.frames_idle[self.frame_index] # Idle animation
        

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_d]:
            self.surf = self.frames_walk[self.frame_index] # Walk animation to the right

        if pressed_key[pygame.K_a]:
            self.surf = self.frames_walk_back[self.frame_index] # Walk animation to the left

        if pressed_key[pygame.K_LSHIFT] and pressed_key[pygame.K_d]:
             self.surf = self.frames_run[self.frame_index] # Run animation to the right

        if pressed_key[pygame.K_LSHIFT] and pressed_key[pygame.K_a]:
            self.surf = self.frames_run_back[self.frame_index] # Run animation to the left
            