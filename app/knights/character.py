from app.items.equipment import Armour, Weapon, Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armours: list[Armour],
            weapon: Weapon,
            potion: Potion | None
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armours = armours
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare_for_battle(self) -> None:
        for armour in self.armours:
            self.protection += armour.protection

        self.power += self.weapon.power

        if self.potion is not None:
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)
            self.hp += self.potion.effect.get("hp", 0)
