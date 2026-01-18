from app.entities.armor import Armor
from app.entities.weapon import Weapon
from app.entities.potion import Potion


class Knight:
    def __init__(self, name: str, data: dict) -> None:
        self.name = data.get("name", name)
        self.power = data.get("power", 0)
        self.hp = data.get("hp", 0)

        # --- броня ---
        armor_data = data.get("armor", [])
        self.armor = [
            Armor(a["part"], a["protection"])
            for a in armor_data
        ]

        # --- оружие ---
        weapon_data = data.get("weapon", {})
        self.weapon = Weapon(
            weapon_data.get("name", ""),
            weapon_data.get("power", 0)
        )

        # --- зелье ---
        potion_data = data.get("potion", {})
        if potion_data:
            self.potion = Potion(
                potion_data.get("name", ""),
                potion_data.get("effect", {})
            )
        else:
            self.potion = None

    def total_protection(self) -> int:
        return sum(a.protection for a in self.armor)

    def attack(self, enemy: "Knight") -> None:
        """Атака"""
        damage = self.power + self.weapon.power
        print(f"{self.name} атакует {enemy.name} и наносит {damage} урона!")
        enemy.defend(damage)

    def defend(self, damage: int) -> None:
        """Получение урона с учетом брони"""
        total_protection = sum(
            a.protection for a in self.armor
        )
        damage_taken = max(0, damage - total_protection)
        self.hp -= damage_taken

        print(
            f"{self.name} получает {damage_taken} урона."
            f"HP осталось: {self.hp}"
        )

    def is_alive(self) -> bool:
        """Проверяет жив ли рыцарь"""
        return self.hp > 0
