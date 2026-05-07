import pygame
from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.Shoot import Shoot
from code.const import WIN_WIDTH, PLAYER_POSITION

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        player_position = PLAYER_POSITION

        match entity_name:
            case "Level_1bg":
                list_bg = []
                for i in range(7):
                    list_bg.append(
                        Background(name=f"Level_1bg{i+1}", position=(0, 0))
                    ) 
                    list_bg.append(
                        Background(name=f"Level_1bg{i+1}", position=(WIN_WIDTH - 5, 0))
                    )
                
                return list_bg

            case "PlayerIdle":
                return Player(name="PlayerIdle", position=player_position)
            
            case "PlayerHurt":
                return Player(name="PlayerHurt", position=player_position)
            
            case "PlayerShoot":
                return Player(name="PlayerShoot", position=player_position)
            
            case "ZombieIdle":
                return Enemy(name="ZombieIdle", position=position)
            
            case "ZombieWalk":
                return Enemy(name="ZombieWalk", position=position)
            
            case "Shoot":
                return Shoot(name="Shoot", position=position)