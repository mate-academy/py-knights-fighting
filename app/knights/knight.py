from typing import Dict, Any


class Knight:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.name = data["name"]
        self.hp = data["hp"]
        self.power = data["power"]

        self.protection = sum(a["protection"] for a in data["armour"])
        self.power += data["weapon"]["power"]

        potion = data["potion"]
        if potion:
            effect = potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
