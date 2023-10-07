import app.knights.apply_stats as stat


class Knight:
    def __init__(self, equipment: dict) -> None:
        self.name = equipment.get("name")
        self.hp = equipment.get("hp")
        self.power = equipment.get("power")
        self.armour = equipment.get("armour")
        self.weapon = equipment.get("weapon")
        self.potion = equipment.get("potion")

    def apply_all(self) -> None:
        if self.armour:
            stat.apply_armour(self)
        if self.weapon:
            stat.apply_weapon(self)
        if self.potion:
            stat.apply_potion(self)
