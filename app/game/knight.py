from app.game.armour import Armour
from app.game.weapon import Weapon
from app.game.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list[Armour],
                 weapon: Weapon, potion: None | Potion) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self._get_protection()

    def __str__(self) -> str:
        return f"""hp = {self.hp}, power = {self.power}, protection = {self.protection}"""

    def _get_protection(self) -> None:
        self.protection = 0
        for armour in self.armour:
            self.protection += armour.get_protection()

    def _get_battle_power(self) -> None:
        self.power += self.weapon.get_power()
        if self.potion:
            if self.potion.power:
                self.power += self.potion.power

    def _get_battle_hp(self) -> None:
        if self.potion:
            if self.potion.hp:
                self.hp += self.potion.hp

    def _get_battle_protection(self) -> None:
        if self.potion:
            if self.potion.protection:
                self.protection += self.potion.protection

    def start_to_battle(self) -> None:
        self._get_battle_power()
        self._get_battle_hp()
        self._get_battle_protection()
