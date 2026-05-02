import pygame

from code.Background import Background
from code.Player import Player
from code.const import WIN_HEIGHT, WIN_WIDTH

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case "Level_1bg":
                list_bg = []
                for i in range(7):
                    list_bg.append(
                        Background(name=f"Level_1bg{i+1}", position=(0, 0))
                    ) 
                    list_bg.append(
                        Background(name=f"Level_1bg{i+1}", position=(WIN_WIDTH, 0))
                    )
                
                return list_bg

            case "PlayerIdle":
                return Player(name="PlayerIdle", position=(100, WIN_HEIGHT - 250))
            
            case "PlayerWalk":
                return Player(name="PlayerWalk", position=(100, WIN_HEIGHT - 250))
