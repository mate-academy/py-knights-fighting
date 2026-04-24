from typing import Any


class Knight:

    def __init__(self, *args, **kwargs: dict[str, Any]) -> None:
        self.name = kwargs.get("name")
        self.hp = kwargs.get("hp")
        self.power = kwargs.get("power")
        self.protection = 0
        self.armour = kwargs.get("armour")
        self.weapon = kwargs.get("weapon")
        self.potion = kwargs.get("potion")

    def apply_armor(self) -> int:
        if self.armour:
            for arm in self.armour:
                self.protection += arm["protection"]
        else:
            print(f"{self.name} has no armour")
        return self.protection

    def apply_weapon(self) -> int:
        if self.weapon:
            self.power += self.weapon["power"]
        else:
            print(f"{self.name} has no weapon")
        return self.power

    def apply_potion(self) -> tuple[int, int, int, str]:
        self.apply_armor()
        self.apply_weapon()
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
        else:
            print(f"{self.name} has no potion")
        return self.power, self.protection, self.hp, self.name


class Battle:

    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> dict[str, int]:
        knight1.apply_potion()
        knight2.apply_potion()

        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection

        if knight1.hp < 0:
            knight1.hp = 0
        if knight2.hp < 0:
            knight2.hp = 0
