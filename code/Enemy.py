from code.Entity import Entity
import pygame
from code.const import ENEMY_LEVEL1_SPEED, TAMANHO_ENEMY, PLAYER_POSITION

class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.frames_walk = []
        self.frames_attack = []

        self.frame_index = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_delay = 150

        for image in range(10):
            walk = pygame.image.load(f"Assets/ZombieWalk{image+1}.png").convert_alpha()
            walk = pygame.transform.scale(walk, TAMANHO_ENEMY)
            self.frames_walk.append(walk)

        for image in range(5):
            attack = pygame.image.load(f"Assets/ZombieAttack{image+1}.png").convert_alpha()
            attack = pygame.transform.scale(attack, TAMANHO_ENEMY)
            self.frames_attack.append(attack)

        self.last_time_roar = 0
        self.roar_delay = 5000 #milisegundos
        self.zombie_sound = pygame.mixer.Sound("./Assets/ZombieRoar.wav")
        self.zombie_sound.set_volume(0.2)

        self.last_zombie_step = 0
        self.zombie_step_delay = 700 #milisegundos
        self.zombie_step = pygame.mixer.Sound("./Assets/ZombieFootStep.wav")
        self.zombie_step.set_volume(0.2)

    def move(self):
        now = pygame.time.get_ticks()
        pressed_key = pygame.key.get_pressed()

        if now - self.last_time_roar > self.roar_delay:
            self.last_time_roar = now
            self.zombie_sound.play()

        if now - self.last_zombie_step > self.zombie_step_delay:
            self.last_zombie_step = now
            self.zombie_step.play()

        if now - self.last_update > self.animation_delay:
            self.last_update = now
            self.frame_index += 1

        if(self.frame_index >= len(self.frames_walk)):
            self.frame_index = 0

        if(self.frame_index >= len(self.frames_attack)):
            self.frame_index = 0


        self.rect.x -= ENEMY_LEVEL1_SPEED
        self.surf = self.frames_walk[self.frame_index]

        if pressed_key[pygame.K_a]:
            self.rect.x += ENEMY_LEVEL1_SPEED

        if pressed_key[pygame.K_a] and pressed_key[pygame.K_LSHIFT]:
            self.rect.x += ENEMY_LEVEL1_SPEED * 2
        
        if pressed_key[pygame.K_d]:
            self.rect.x -= ENEMY_LEVEL1_SPEED * 1.5

        if pressed_key[pygame.K_d] and pressed_key[pygame.K_LSHIFT]:
            self.rect.x -= ENEMY_LEVEL1_SPEED * 3

        if self.rect.left < PLAYER_POSITION[0] + 70:
            self.rect.left = PLAYER_POSITION[0] + 70
            self.surf = self.frames_attack[self.frame_index]

        

        