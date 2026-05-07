import pygame

from code.Shoot import Shoot
from code.Entity import Entity
from code.const import TAMANHO_PLAYER
from code.EntityMediator import EntityMediator

class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        
        self.frames_idle = []
        self.frames_walk = []
        self.frames_walk_back = []
        self.frames_run = []
        self.frames_run_back = []
        self.frames_hurt = []
        self.frames_shoot = []

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

        for image in range(2):
            hurt = pygame.image.load(f"Assets/PlayerHurt{image+1}.png").convert_alpha()
            hurt = pygame.transform.scale(hurt, TAMANHO_PLAYER)
            self.frames_hurt.append(hurt)

        for image in range(12):
            shoot = pygame.image.load(f"Assets/PlayerShoot{image+1}.png").convert_alpha()
            shoot = pygame.transform.scale(shoot, (TAMANHO_PLAYER[0]*2.2, TAMANHO_PLAYER[1])) #Compensa o tamanho do Sprite de tirom, deixando-o proporcional aos outros Sprites
            self.frames_shoot.append(shoot)

        self.last_step = 0
        self.step_delay = 500 #milisegundos
        self.player_step = pygame.mixer.Sound("./Assets/PlayerFootStep.wav")
        pygame.mixer.Sound.set_volume(self.player_step, 0.2)

        self.last_time_shoot = 0
        self.shoot_delay = 1100 #milisegundos
        self.bullet_shoot = pygame.mixer.Sound("./Assets/BulletShoot.wav")
        self.bullet_shoot.set_volume(0.2)



    def move(self):
        now = pygame.time.get_ticks()
        pressed_key = pygame.key.get_pressed()

        def step_sound():
            if pressed_key[pygame.K_LSHIFT]:
                self.step_delay = 300 #milisegundos
            else:
                self.step_delay = 500 #milisegundos

            if now - self.last_step > self.step_delay:
                self.last_step = now
                self.player_step.play()


        if now - self.last_update > self.animation_delay:
            self.last_update = now
            self.frame_index += 1

        if(self.frame_index >= len(self.frames_idle)):
            self.frame_index = 0
        
        if(self.frame_index >= len(self.frames_shoot)):
            self.frame_index = 0

        self.surf = self.frames_idle[self.frame_index] # Idle animation


        if pressed_key[pygame.K_d]:
            self.surf = self.frames_walk[self.frame_index] # Walk animation to the right
            step_sound()

        if pressed_key[pygame.K_a]:
            self.surf = self.frames_walk_back[self.frame_index] # Walk animation to the left
            step_sound()

        if pressed_key[pygame.K_LSHIFT] and pressed_key[pygame.K_d]:
            self.surf = self.frames_run[self.frame_index] # Run animation to the right
            step_sound()

        if pressed_key[pygame.K_LSHIFT] and pressed_key[pygame.K_a]:
            self.surf = self.frames_run_back[self.frame_index] # Run animation to the left
            step_sound()

        if pressed_key[pygame.K_LCTRL]:
            if now - self.last_time_shoot > self.shoot_delay:
                self.last_time_shoot = now
                self.bullet_shoot.play()
            self.surf = self.frames_shoot[self.frame_index] # Shoot animation

            
    def shoot(self):
        self.shooting = False

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LCTRL]:
            return Shoot(name="Shoot", position=(self.rect.right, self.rect.centery))
