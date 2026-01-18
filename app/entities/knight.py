from app.entities.armor import Armor
from app.entities.weapon import Weapon
from app.entities.potion import Potion


class Knight:
    def __init__(self, key: str, data: dict) -> None:
        self.key = key
        self.name = data["name"]

        # базовые характеристики
        self.hp = data["hp"]
        base_power = data["power"]

        # броня
        self.armor = [
            Armor(a["part"], a["protection"])
            for a in data.get("armor", [])
        ]

        self.protection = sum(a.protection for a in self.armor)

        # оружие (есть всегда по условиям)
        weapon_data = data["weapon"]
        self.weapon = Weapon(
            weapon_data["name"],
            weapon_data["power"],
        )

        # итоговая сила
        self.power = base_power + self.weapon.power

        # зелье
        potion_data = data.get("potion")
        self.potion = (
            Potion(potion_data["name"], potion_data["effect"])
            if potion_data else None
        )
