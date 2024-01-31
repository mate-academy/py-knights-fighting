class Knight:

    def __init__(self, knight: dict) -> None:
        self.knight = knight

    def apply_point(self) -> None:
        self.knight["protection"] = 0
        if self.knight.get("potion"):
            effect = self.knight.get(
                "potion").get("effect", {})
            self.knight["power"] += effect.get("power", 0)
            self.knight["protection"] += effect.get("protection", 0)
            self.knight["hp"] += effect.get("hp", 0)

    def apply_armour(self) -> None:
        for armour in self.knight["armour"]:
            self.knight["protection"] += armour["protection"]

    def apply_weapon(self) -> None:
        self.knight["power"] += self.knight["weapon"]["power"]
