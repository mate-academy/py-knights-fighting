class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.power = knight_data["power"]
        self.hp = knight_data["hp"]
        self.protection = 0

        self.apply_armour(knight_data.get("armour", []))
        self.apply_weapon(knight_data.get("weapon", {}))
        self.apply_potion(knight_data.get("potion"))

    def apply_armour(self, armour_list: list) -> None:
        for armour in armour_list:
            self.protection += armour.get("protection", 0)

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon.get("power", 0)

    def apply_potion(self, potion: dict | None) -> None:
        if potion and "effect" in potion:
            effects = potion["effect"]
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
