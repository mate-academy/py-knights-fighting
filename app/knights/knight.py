class Knight:
    def __init__(self, data: dict):
        self.name = data["name"]
        self.power = data["power"]
        self.hp = data["hp"]
        self.armour = data.get("armour", [])
        self.weapon = data.get("weapon")
        self.potion = data.get("potion")

    def prepared_stats(self) -> dict:
        base_hp = self.hp
        base_power = self.power
        base_protection = 0

        for armour in self.armour:
            base_protection += armour.get("protection", 0)

        if self.weapon:
            base_power += self.weapon.get("power", 0)

        if self.potion:
            effect = self.potion.get("effect", {})
            base_hp += effect.get("hp", 0)
            base_power += effect.get("power", 0)
            base_protection += effect.get("protection", 0)
        return {
            "hp": base_hp,
            "power": base_power,
            "protection": base_protection
        }
