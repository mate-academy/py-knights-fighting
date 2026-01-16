class Knight:
    def __init__(
            self, name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        self.calculate_protection()
        self.apply_weapon_effect()
        self.apply_potion_effect()

    def calculate_protection(self) -> None:
        for armour_piece in self.armour:
            self.protection += armour_piece["protection"]

    def apply_weapon_effect(self) -> None:
        if self.weapon:
            self.power += self.weapon["power"]

    def apply_potion_effect(self) -> None:
        if self.potion:
            effects = self.potion.get("effect", {})
            for effect, value in effects.items():
                if hasattr(self, effect):
                    setattr(self, effect, getattr(self, effect) + value)
