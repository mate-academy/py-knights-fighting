from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name: str = knight["name"]
        self.power: int = knight["power"]
        self.hp: int = knight["hp"]
        self.armour: list[dict] = knight["armour"]
        self.weapon: dict = knight["weapon"]
        self.potion: dict = knight["potion"]
        self.protection: int = 0

    def apply_armour(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            for key, value in self.potion["effect"].items():
                if hasattr(self, key):
                    setattr(self, key, getattr(self, key) + value)

    def apply_all_equipment(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def battle_vs(self, other_knight: Knight) -> None:
        self.hp -= other_knight.power - self.protection
        other_knight.hp -= self.power - other_knight.protection
        self.check_hp()
        other_knight.check_hp()

    def check_hp(self) -> None:
        if self.hp <= 0:
            self.hp = 0
