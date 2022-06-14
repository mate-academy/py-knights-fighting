class FightOneToOne:
    """
    This class describe how battle looks like
    """

    def __init__(self, knight_1, knight_2):
        self.knight_1 = knight_1
        self.knight_2 = knight_2

    def make_battle(self):
        self.knight_1 -= self.knight_2
        self.knight_2 -= self.knight_1
