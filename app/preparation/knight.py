from app.preparation.equipment import Weapon, Potion


class Knight:
    def __init__(
            self, name: str, power: int, hp: int,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_armour(self, part: int) -> None:
        self.protection += part

    def apply_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def apply_potion(self, potion: Potion) -> None:
        if potion is not None:
            self.power += potion.power
            self.hp += potion.hp
            self.protection += potion.protection

    def __repr__(self) -> str:
        return (f"Name: {self.name}, Power: {self.power}, "
                f"HP: {self.hp}, Protection: {self.protection}")
