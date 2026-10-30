class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.hp = data["hp"]

        weapon = data.get("weapon")
        weapon_power = weapon["power"] if weapon else 0
        self.power = data["power"] + weapon_power

        armour = data.get("armour", [])
        self.protection = sum(item["protection"] for item in armour)

        potion = data.get("potion")
        if potion and "effect" in potion:
            effect = potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
