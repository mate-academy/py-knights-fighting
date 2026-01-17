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

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon.get("power")

    def apply_armour(self, armour: dict) -> None:
        for level_of_protection in armour:
            self.protection += level_of_protection["protection"]

    def apply_potion(self, potion: dict) -> None:
        list_of_powers = ["power", "protection", "hp"]
        for effect in list_of_powers:
            if effect in potion["effect"]:
                replacement = getattr(self, effect) + potion["effect"][effect]
                setattr(self, effect, replacement)
