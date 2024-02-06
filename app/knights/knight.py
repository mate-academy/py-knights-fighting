class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.base_power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight.get("armour", [])
        self.protection = sum(
            armor_piece["protection"] for armor_piece in self.armour
        )
        self.weapon = knight.get("weapon", {"power": 0})
        self.potion = knight.get("potion")
        self.power = self.base_power + self.weapon["power"]

        if self.potion:
            self.apply_potion_effect()

    def apply_potion_effect(self) -> None:
        effect = self.potion.get("effect", {})
        self.hp += effect.get("hp", 0)
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)
