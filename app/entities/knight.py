from app.entities.armor import Armor
from app.entities.weapon import Weapon
from app.entities.potion import Potion


class Knight:
    def __init__(self, key: str, data: dict) -> None:
        self.key = key
        self.name = data["name"]
        self.hp = data["hp"]
        self.power = data["power"]

        self.armor = [
            Armor(a["part"], a["protection"])
            for a in data.get("armour", [])
        ]

        weapon_data = data.get("weapon")
        self.weapon = (
            Weapon(weapon_data["name"], weapon_data["power"])
            if weapon_data else None
        )

        potion_data = data.get("potion")
        self.potion = (
            Potion(potion_data["name"], potion_data["effect"])
            if potion_data else None
        )

        self.potion_used = False

    @property
    def protection(self) -> int:
        return sum(a.protection for a in self.armor)
