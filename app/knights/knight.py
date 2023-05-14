from typing import Union


class Knights:
    def __init__(self, name: str, power: int, hp: int, weapon: str,
                 armor: list,
                 potion: Union[dict, None]) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
        self.potion = potion

    def get_stats(self) -> dict:
        stats = {
            "hp": self.hp,
            "power": self.power + self.weapon.power,
            "protection": sum(part["protection"] for part in self.armor.parts),
        }
        if self.potion:
            stats["hp"] += self.potion.effect.get("hp", 0)
            stats["power"] += self.potion.effect.get("power", 0)
            stats["protection"] += self.potion.effect.get("protection", 0)
        return stats
