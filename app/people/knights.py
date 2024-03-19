from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list | None,
                 weapon: dict | None,
                 potion: dict | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.weapon = weapon
        self.armour = armour
        self.potion = potion

    def weapon_up(self) -> None:
        self.power += self.weapon["power"]

    def armour_up(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def drink_potion(self) -> None:
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

    def battle(self, enemy: Knight) -> dict:
        print(self.hp, self.power, self.protection)
        print(enemy.hp, enemy.power, enemy.protection)
        self.hp -= enemy.power - self.protection
        enemy.hp -= self.power - enemy.protection

        if self.hp < 0:
            self.hp = 0
        if enemy.hp < 0:
            enemy.hp = 0
        return {self.name: self.hp,
                enemy.name: enemy.hp}
