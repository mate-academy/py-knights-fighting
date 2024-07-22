class Knight:
    def __init__(self, name: str,
                 power: int, hp: int,
                 armour: list, weapon: dict,
                 potion: dict) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = sum(armour_piece.get("protection", 0)
                              for armour_piece in self.armour)
        self.power = self.base_power + self.weapon["power"]

        if self.potion:
            for attr, value in self.potion["effect"].items():
                setattr(self, attr, getattr(self, attr) + value)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage - self.protection
        if self.hp < 0:
            self.hp = 0
