class Knight:
    def __init__(self, power: int, health: int) -> None:
        self.power = power
        self.hp = health
        self.protection = 0

    def armour_on(self, armour: list) -> None:
        for piece_of_equip in armour:
            self.protection += piece_of_equip["protection"]

    def weapons_up(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def potion_in(self, potion: dict) -> None:
        for effect, strength in potion.items():
            with_buff = getattr(self, effect) + strength
            setattr(self, effect, with_buff)
