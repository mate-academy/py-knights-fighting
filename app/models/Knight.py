from __future__ import annotations


class Knight:
    def __init__(self, knight_stats: dict) -> None:
        self.name = knight_stats["name"]
        self.power = knight_stats["power"]
        self.hp = knight_stats["hp"]
        self.protection = 0
        self.armours = knight_stats["armour"]
        self.weapon = knight_stats["weapon"]["power"]
        self.potions = knight_stats["potion"]

    def set_total_armor(self) -> Knight:
        total_armor = 0
        for armor in self.armours:
            total_armor += armor["protection"]
        self.protection = total_armor
        return self

    def set_potion(self) -> Knight:
        if self.potions is not None:
            self.potions = self.potions["effect"]

            potions_map = {
                "power": self.__add_power,
                "hp": self.__add_hp,
                "protection": self.__add_hp
            }
            for key, value in potions_map.items():
                if key in self.potions:
                    value(self.potions[key])

        return self

    def set_weapon(self) -> Knight:
        self.power += self.weapon
        return self

    def knight_adjusting(self) -> Knight:
        return self.set_total_armor().set_potion().set_weapon()

    def __add_power(self, power: int) -> None:
        self.power += power

    def __add_hp(self, hp: int) -> None:
        self.hp += hp

    def __add_protection(self, protection: int) -> None:
        self.protection += protection
