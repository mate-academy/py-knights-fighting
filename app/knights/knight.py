from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armours: list[Armour],
            weapon: Weapon,
            potion: Potion
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armours = armours
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def battle_preparation(self) -> None:
        self.protection = sum(armour.protection for armour in self.armours)

        self.power += self.weapon.power

        if self.potion:
            self.protection += self.potion.effect.get("protection", 0)
            self.power += self.potion.effect.get("power", 0)
            self.hp += self.potion.effect.get("hp", 0)

    @classmethod
    def from_config(cls, knight_config: dict) -> Knight:
        return cls(
            name=knight_config["name"],
            power=knight_config["power"],
            hp=knight_config["hp"],
            armours=[Armour(**a) for a in knight_config["armour"]],
            weapon=Weapon(**knight_config["weapon"]),
            potion=Potion(
                **knight_config["potion"]
            ) if knight_config["potion"] else None
        )
