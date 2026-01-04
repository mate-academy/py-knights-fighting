from app.knights_battle.equipment import Armour, Weapon, Potion


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: Weapon,
                 potion: Potion) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = []
        self.weapon = None
        self.potion = None
        self.protection = 0
        if armour:
            for armour_piece in armour:
                self.armour.append(
                    Armour(
                        armour_piece["part"],
                        armour_piece["protection"]
                    )
                )
        # If weapon is provided, create a Weapon object
        if weapon:
            self.weapon = Weapon(weapon["name"], weapon["power"])

        # If potion is provided, create a Potion object
        if potion:
            self.potion = Potion(potion["name"], potion["effect"])

    def apply_armour(self) -> None:
        for var_a in self.armour:
            self.protection += var_a.protection

    def apply_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            for attr, effect in self.potion.effect.items():
                setattr(self, attr, getattr(self, attr) + effect)
