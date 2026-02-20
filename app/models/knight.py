from app.models.armour import Armour
from app.models.weapon import Weapon
from app.models.potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list = None,
        weapon: dict = None,
        potion: dict = None,
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0
        self.armours = [Armour(**a) for a in (armour or [])]
        self.weapon = Weapon(**weapon) if weapon else None
        self.potion = Potion(**potion) if potion else None

    def apply_equipment(self) -> None:
        for armour in self.armours:
            self.protection += armour.protection

        if self.weapon:
            self.power += self.weapon.power

        if self.potion:
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)
            self.hp += self.potion.effect.get("hp", 0)
