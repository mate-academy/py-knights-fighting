from app.equipment import Weapon, Armour, Potion


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict) -> None:
        self.name = name
        self.hp = hp
        self.weapon = Weapon(weapon["name"], weapon["power"])
        self.power = self._apply_weapon(power)
        self.armour = Armour(armour)
        self.potion = Potion(potion) if potion else None

    def _apply_weapon(self, power: int) -> int:
        return self.weapon.power + power

    def apply_potion(self) -> None:
        if self.potion:
            self.power += self.potion.effect["power"]
            self.hp += self.potion.effect["hp"]
            self.armour.protection += self.potion.effect.get("protection", 0)
