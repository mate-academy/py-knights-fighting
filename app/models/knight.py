from .armour import Armour
from .weapon import Weapon
from .status import Status
from .potion import Potion

# {name: str, power: str, hp: int,
#         armour: list[Armour | None],
#         weapon: Weapon,
#         potion: Potion | None}
class Knight:
    def __init__(
        self, knight: dict
    ) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = [Armour(**armour) for armour in knight["armour"]]
        self.weapon = Weapon(**knight["weapon"])
        self.potion = Potion(**knight["potion"]) if knight["potion"] else None

    def apply_armours(self) -> None:
        self.protection = sum(armour.protection for armour in self.armour)
   
    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self):
        if(self.potion):
            for effect, value in self.potion.effect.items():
                self.__dict__[effect] += value
