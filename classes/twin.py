from .block import Block

class Twin(Block):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32, (255, 0, 100))
