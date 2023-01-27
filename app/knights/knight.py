from __future__ import annotations


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[dict],
        weapon: dict,
        potion: dict,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    # створимо методи для спорядження лицарів:

    def apply_armour(self) -> None:
        self.protection = 0
        for kind in self.armour:
            self.protection += kind["protection"]
        if self.potion is not None and "protection" in self.potion["effect"]:
            self.protection += self.potion["effect"]["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]
        if self.potion is not None:
            self.power += self.potion["effect"]["power"]

    def result_hp(self) -> None:
        if self.potion is not None:
            self.hp += self.potion["effect"]["hp"]

    def gear_up(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.result_hp()

    # ініціюємо метод для битви між двома лицарями

    def fight(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
