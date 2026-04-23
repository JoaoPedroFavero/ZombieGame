from ast import List
from code.Entity import Entity

class Level:

    def __init__(self, window, name):
        self.window = window
        self.nome = name
        self.entity_list: List[Entity] = []

        

    def run(self):
        pass