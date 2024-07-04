class Knight:
    def __init__(self,
                 name: str, power: int, hp: int,
                 armour: int, weapon: int, potion: int) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.power = self.base_power
        self.hp = self.base_hp
        self.apply_modifications()

    def apply_modifications(self) -> None:
        self.protection = sum(armour_piece["protection"]
                              for armour_piece in self.armour)

        self.power += self.weapon["power"]

        if self.potion:
            for stat, value in self.potion["effect"].items():
                setattr(self, stat, getattr(self, stat) + value)

    def calculate_damage(self, opponent_power: int) -> None:
        damage = max(0, opponent_power - self.protection)
        self.hp -= damage

    def is_defeated(self) -> bool:
        return self.hp <= 0
