from typing import Dict, List, Optional


class Knight:
    def __init__(self, config: Dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0

        weapon: Optional[Dict[str, int]] = config.get("weapon")
        if weapon:
            self.power += weapon.get("power", 0)

        armour: List[Dict[str, int]] = config.get("armour", [])
        for piece in armour:
            self.protection += piece.get("protection", 0)

        potion: Optional[Dict] = config.get("potion")
        if potion:
            effects: Dict[str, int] = potion.get("effect", {})
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
