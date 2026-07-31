from app.potion import Potion
from app.weapon import Weapon
from app.armor import Armor


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armor: list[Armor],
            weapon: Weapon,
            potion: Potion = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armor = armor
        self.weapon = weapon
        self.potion = potion

    def apply_potion(self, potion: Potion) -> None:
        if potion is not None:
            if "power" in potion.effect:
                self.power += potion.effect["power"]
            if "protection" in potion.effect:
                self.protection += potion.effect["protection"]
            if "hp" in potion.effect:
                self.hp += potion.effect["hp"]

    def apply_armor(self) -> None:
        self.protection += sum(a.protection for a in self.armor)

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def battle(self, opponent: Knight) -> dict:
        self.apply_armor()
        self.apply_weapon()
        self.apply_potion(self.potion)

        opponent.apply_armor()
        opponent.apply_weapon()
        opponent.apply_potion(opponent.potion)

        self.hp -= max(opponent.power - self.protection, 0)
        opponent.hp -= max(self.power - opponent.protection, 0)

        if self.hp < 0:
            self.hp = 0
        if opponent.hp < 0:
            opponent.hp = 0

        return {self.name: self.hp, opponent.name: opponent.hp}
