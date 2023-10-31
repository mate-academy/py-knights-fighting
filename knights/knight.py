from items.weapon import Weapon
from items.potion import Potion
from items.armour import Armour


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion = None,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def __str__(self) -> str:
        return (f"name: {self.name}, power: {self.power}, "
                f"hp: {self.hp}, protect: {self.protection}, "
                f"armour: {self.armour}, "
                f"weapon: {self.weapon}, potion: {self.potion}")

    @classmethod
    def create_knight(cls, name: str, knights_config: dict) -> "Knight":
        return cls(
            name.replace("_", " ").title(),
            knights_config[name.lower()]["power"],
            knights_config[name.lower()]["hp"],
            Armour.create_armour(knights_config[name]),
            Weapon.create_weapon(knights_config[name]),
            Potion.crate_potion(knights_config[name])
        )
