class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0,
            potion: int = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        self.potion = potion

    def apply_armour(self, armours: dict) -> None:
        for armour in armours["armour"]:
            self.protection += armour["protection"]

    def apply_weapon(self, weapons: dict) -> None:
        self.power += weapons["weapon"]["power"]

    def apply_potion(self, potion: dict) -> None:
        if potion:
            effects = potion["effect"]
            list_of_potion = ["power", "protection", "hp"]
            for potion_effect in list_of_potion:
                effect = getattr(self, potion_effect)
                setattr(
                    self,
                    potion_effect,
                    effect + effects.get(potion_effect, 0)
                )


def create_knight(knights: dict) -> Knight:
    return Knight(knights["name"], knights["power"], knights["hp"])
