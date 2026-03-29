class Knight:
    def __init__(self, char: dict) -> None:
        self.char = char
        self.name = char["name"]
        self.power = char["power"]
        self.hp = char["hp"]
        self.protection = 0

    def _apply_weapon(self) -> None:
        weapon_pow = self.char["weapon"]["power"]
        if isinstance(weapon_pow, int):
            self.power += weapon_pow

    def _apply_armour(self) -> None:
        self.protection = sum(i["protection"] for i in self.char["armour"])

    def _apply_potion(self) -> None:
        stats = (
            "hp",
            "power",
            "protection"
        )
        if self.char["potion"]:
            potion_effects = self.char["potion"]["effect"]
            for stat in stats:
                if stat in potion_effects:
                    stat_val = getattr(self, stat)
                    setattr(self, stat, potion_effects[stat] + stat_val)

    def arm_the_warrior(self) -> None:
        self._apply_armour()
        self._apply_weapon()
        self._apply_potion()
