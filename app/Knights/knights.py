from typing import Dict, Any, List, Optional


class Knights:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.name: str = data["name"]
        self.hp: int = data["hp"]
        self.power: int = data["power"]
        self.armour: List[Dict[str, Any]] = data["armour"]
        self.weapon: Dict[str, Any] = data["weapon"]
        self.potion: Optional[Dict[str, Any]] = data["potion"]
        self.protection: int = 0

    def prepare_for_battle(self) -> None:
        for arm in self.armour:
            self.protection += arm["protection"]

        self.power += self.weapon["power"]
        if self.potion:
            self.protection +=\
                self.potion["effect"].get("protection", 0)
            self.power += self.potion["effect"].get("power", 0)
            self.hp += self.potion["effect"].get("hp", 0)


def battle(knight1: "Knights", knight2: "Knights") -> None:
    damage_to_k1: int = max(0, knight2.power - knight1.protection)
    damage_to_k2: int = max(0, knight1.power - knight2.protection)
    knight1.hp = max(0, knight1.hp - damage_to_k1)
    knight2.hp = max(0, knight2.hp - damage_to_k2)
