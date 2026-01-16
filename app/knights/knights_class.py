from typing import Union


class Knights:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: Union[dict, None] = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.get_protection()

    def get_protection(self) -> None:
        self.protection = sum(arm["protection"] for arm in self.armour)

    def get_weapon(self) -> None:
        self.power += self.weapon["power"]

    def get_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def attack(self, enemy: "Knights") -> None:
        self.hp -= enemy.power - self.protection
        if self.hp <= 0:
            self.hp = 0
