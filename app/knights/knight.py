class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.base_power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight.get("armour", [])
        self.protection = sum(
            armour_piece["protection"] for armour_piece in self.armour
        )
        self.weapon = knight.get("weapon", {"power": 0})
        self.potion = knight.get("potion")
        self.power = self.base_power + self.weapon["power"]

        if self.potion:
            self.apply_potion_effect()

    def apply_potion_effect(self) -> None:
        for effect, value in self.potion.get("effect", {}).items():
            setattr(self, effect, getattr(self, effect, 0) + value)
