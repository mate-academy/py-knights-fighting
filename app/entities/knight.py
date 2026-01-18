from app.entities.armor import Armor
from app.entities.weapon import Weapon
from app.entities.potion import Potion


class Knight:
    def __init__(self, name: str, data: dict) -> None:
        self.name = data.get("name", name)
        self.hp = data.get("hp", 0)

        # базовая сила
        base_power = data.get("power", 0)

        # --- броня ---
        armor_data = data.get("armor") or data.get("armour", [])
        self.armor = [
            Armor(a["part"], a["protection"])
            for a in armor_data
        ]

        # суммарная защита
        self.protection = sum(a.protection for a in self.armor)

        # --- оружие ---
        weapon_data = data.get("weapon", {})
        self.weapon = Weapon(
            weapon_data.get("name", ""),
            weapon_data.get("power", 0),
        )

        # итоговая сила (1 раз!)
        self.power = base_power + self.weapon.power

        # --- зелье ---
        potion_data = data.get("potion")
        self.potion = (
            Potion(potion_data["name"], potion_data["effect"])
            if potion_data else None
        )

    def attack(self, enemy: "Knight") -> None:
        enemy.defend(self.power)

    def defend(self, damage: int) -> None:
        self.hp -= max(0, damage - self.protection)

    def is_alive(self) -> bool:
        return self.hp > 0
