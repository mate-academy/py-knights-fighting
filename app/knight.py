class Knight:
    def __init__(self,
                 name: str,
                 hp: int,
                 power: int,
                 protection: int
                 ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    def take_damage(self, attack_power: int) -> None:
        self.hp -= (attack_power - self.protection)
        if self.hp <= 0:
            self.hp = 0
