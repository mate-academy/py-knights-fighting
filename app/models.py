class Knight:
    def __init__(self, name: str, hp: int, power: int, protection: int):
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    def take_damage(self, enemy_power: int):
        damage = max(0, enemy_power - self.protection)
        self.hp = max(0, self.hp - damage)

    def __repr__(self):
        return (f"{self.name}(HP={self.hp}, "
                f"Power={self.power}, Protection={self.protection})")
