from app.inventory.inventory import Inventory


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict) -> None:
        self.name = name
        self._power = power
        self._hp = hp
        self.inventory = Inventory(armour, weapon, potion)

    @property
    def power(self) -> int:
        return self._power + self.inventory.get_power()

    @property
    def hp(self) -> int:
        return max(self._hp + self.inventory.get_hp(), 0)

    @property
    def protection(self) -> int:
        return self.inventory.get_protection()

    def take_damage(self, other_power: int) -> int:
        other_power -= self.protection
        self._hp -= other_power
        return self._hp
