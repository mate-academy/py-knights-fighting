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
        if not isinstance(self.potions, type(None)):
            self.potions = self.potions["effect"]
            if "power" in self.potions:
                self.power += self.potions["power"]
            if "hp" in self.potions:
                self.hp += self.potions["hp"]
            if "protection" in self.potions:
                self.protection += self.potions["protection"]
        return self

    def set_weapon(self) -> Knight:
        self.power += self.weapon
        return self

    def knight_adjusting(self) -> Knight:
        return self.set_total_armor().set_potion().set_weapon()
