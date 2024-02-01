from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]

        self.prepare_to_battle()

    def prepare_to_battle(self) -> None:
        self.prepare_armour()
        self.prepare_weapon()
        self.drink_potion()

    def drink_potion(self) -> None:
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def prepare_armour(self) -> None:
        self.protection += sum(
            [armour_part["protection"] for armour_part in self.armour]
        )

    def prepare_weapon(self) -> None:
        self.power += self.weapon["power"]

    def fight(self, enemy: Knight) -> None:
        self.hp -= enemy.power - self.protection
        enemy.hp -= self.power - enemy.protection

        if self.hp < 0:
            self.hp = 0

        if enemy.hp < 0:
            enemy.hp = 0
