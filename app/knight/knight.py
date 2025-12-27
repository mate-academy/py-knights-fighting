class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

    def apply_armour(self) -> None:
        for armour_unit in self.armour:
            self.protection += armour_unit["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        relevant_stats = ["power", "protection", "hp"]
        if self.potion is not None:
            for stat in relevant_stats:
                if stat in self.potion["effect"]:
                    boost = self.potion["effect"][stat]
                    setattr(
                        self, stat,
                        getattr(self, stat) + boost
                    )

    def prepare_knight(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
