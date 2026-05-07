from code.Entity import Entity
from code.const import SHOOT_SPEED

class Shoot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.x += SHOOT_SPEED