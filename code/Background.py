from Entity import Entity

class Background(Entity):

    def __init__(self, window):
        super().__init__(name="background", position=(0, 0))
        

    def move(self):
        pass