class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_armour(self, armours: list[dict]) -> None:
        if armours:
            for armour in armours:
                self.protection += armour["protection"]

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, effects: dict) -> None:
        self.power += effects.get("power", 0)
        self.hp += effects.get("hp", 0)
        self.protection += effects.get("protection", 0)

    def calculate_hp_after_damage(self, damage: int) -> None:
        if self.hp <= (damage - self.protection):
            self.hp = 0
        else:
            self.hp -= (damage - self.protection)
