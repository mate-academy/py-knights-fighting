from app.fighter.armour import Armour
from app.fighter.potion import Potion
from app.fighter.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp

        self.protection = 0

        self.armour = []

        for piece in armour:
            self.armour.append(
                Armour(
                    name=piece.get("name"),
                    protection=piece.get("protection")
                )
            )
        self.weapon = Weapon(weapon)

        self.potion = None
        if potion:
            self.potion = Potion(
                name=potion.get("name"),
                effect=potion.get("effect")
            )

    def ready_up(self) -> None:

        if self.potion:
            self.potion.drink_potion(self)

        self.weapon.equip_to_knight(self)

        for piece in self.armour:
            piece.equip_armour_to_knight(self)
