class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list = None,
            weapon: dict = None,
            potion: dict = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        self.apply_armour_protection()
        self.apply_weapon_power()
        self.apply_potion_effects()

    def apply_armour_protection(self) -> None:
        for armour_piece in self.armour:
            self.protection += armour_piece.get("protection", 0)

    def apply_weapon_power(self) -> None:
        if self.weapon:
            self.power += self.weapon.get("power", 0)

    def apply_potion_effects(self) -> None:
        if self.potion:
            effect = self.potion.get("effect", {})
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)
