class Knight:
    def __init__(self, knights: dict) -> None:
        self.knights = knights
        self.name = knights["name"]
        self.power = knights["power"]
        self.hp = knights["hp"]
        self.protection = 0

    def apply_weapon(self) -> None:
        weapon_pow = self.knights["weapon"]["power"]
        if isinstance(weapon_pow, int):
            self.power += weapon_pow

    def apply_armour(self) -> None:
        self.protection = \
            sum(armour["protection"] for armour in self.knights["armour"])

    def apply_potion(self) -> None:
        stats = (
            "hp",
            "power",
            "protection"
        )
        if self.knights["potion"]:
            potion_effects = self.knights["potion"]["effect"]
            for stat in stats:
                if stat in potion_effects:
                    stat_val = getattr(self, stat)
                    setattr(self, stat, potion_effects[stat] + stat_val)

    def arm_the_warrior(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
