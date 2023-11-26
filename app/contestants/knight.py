from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.health_points = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        # BATTLE PREPARATIONS:
        armour = Armour(self.armour)
        armour.apply_armour(self)

        weapon = Weapon(self.weapon["power"])
        weapon.apply_weapon(self)

        if self.potion is not None:
            potion = Potion(self.potion["effect"])
            potion.apply_potion(self)
