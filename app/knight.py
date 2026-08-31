from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: dict,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def init_battle_stats(self) -> None:
        # add armour
        if len(self.armour) > 0:
            for armour in self.armour:
                self.protection += armour["protection"]

        # add weapon
        self.power += self.weapon["power"]

        # add potion
        if self.potion is not None:
            for effect, value in self.potion["effect"].items():
                match effect:
                    case "hp":
                        self.hp += value
                    case "power":
                        self.power += value
                    case "protection":
                        self.protection += value

    def battle(self, opponent: Knight) -> None:
        self.hp -= opponent.power - self.protection

        if self.hp <= 0:
            self.hp = 0
