from typing import Self

from app.knights.gear import Armour, Potion, Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def take_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def apply_armour(self, armours: list[Armour]) -> None:
        self.protection = sum(armour.protection for armour in armours)

    def drink_potion(self, potion: Potion | None) -> None:
        if potion is None:
            return
        for characteristic, change in potion.effect.items():
            current_value = getattr(self, characteristic)
            setattr(self, characteristic, current_value + change)

    @classmethod
    def from_config(cls, config: dict) -> Self:
        armours = [
            Armour(
                part=item["part"],
                protection=item["protection"]
            )
            for item in config["armour"]
        ]

        weapon = Weapon(
            name=config["weapon"]["name"],
            power=config["weapon"]["power"]
        )

        potion = config["potion"]

        if potion is not None:
            potion = Potion(
                name=config["potion"]["name"],
                effect=config["potion"]["effect"]
            )

        knight = cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"]
        )

        knight.take_weapon(weapon)
        knight.apply_armour(armours)
        knight.drink_potion(potion)

        return knight

    def take_damage(self, opponent: Knight) -> None:
        self.hp = max(0, self.hp - (opponent.power - self.protection))
