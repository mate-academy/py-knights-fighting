class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def add_armour(self, armours: list) -> None:
        for armour in armours:
            self.protection += armour["protection"]

    def add_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def add_potion(self, potion: dict) -> None:
        self.power += potion["effect"].get("power", 0)
        self.hp += potion["effect"].get("hp", 0)
        self.protection += potion["effect"].get("protection", 0)
