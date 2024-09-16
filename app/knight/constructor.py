class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list | list[dict],
            weapon: dict,
            potion: None | dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> int:
        for armour in self.armour:
            self.protection += armour.get("protection", 0)
        return self.protection

    def apply_weapon(self) -> int:
        self.power += self.weapon.get("power", 0)
        return self.power

    def apply_potion_effect(self) -> dict:
        knight_stats = {}
        if self.potion is not None:
            effects = self.potion.get("effect", {})

            if "power" in effects:
                self.power += effects["power"]
                knight_stats["power"] = self.power

            if "protection" in effects:
                self.protection += effects["protection"]
                knight_stats["protection"] = self.protection

            if "hp" in effects:
                self.hp += effects["hp"]
                knight_stats["hp"] = self.hp
        return knight_stats
