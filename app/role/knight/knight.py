from dataclasses import dataclass, field
from typing import Union, Optional, List
from app.role.knight.inventory.armour import Armour
from app.role.knight.inventory.potion import Potion
from app.role.knight.inventory.weapon import Weapon


@dataclass
class Knight:
    name: str
    hp: int
    power: int
    armour: List[Armour] = field(default_factory=list)
    weapon: Optional[Weapon] = None
    potion: Optional[Potion] = None
    protection: int = 0

    def equip(
            self,
            armours: list,
            weapon: dict,
            potion: Union[dict, None]
    ) -> None:
        for armour in armours:
            self.armour.append(Armour(armour["part"], armour["protection"]))
            self.protection += armour["protection"]
        self.weapon = Weapon(weapon["name"], weapon["power"])
        self.power += self.weapon.power
        if potion is not None:
            self.potion = Potion(potion["name"], potion["effect"])
            self.potion.apply_effect(self)

    @classmethod
    def form_config(cls, config: dict) -> "Knight":
        knight = cls(config["name"], config["hp"], config["power"])
        knight.equip(
            config["armour"],
            config["weapon"],
            config["potion"]
        )
        return knight
