from app.data.knights import KNIGHTS


class Knight:
    def __init__(self,
                 name: str,
                 hp: int,
                 power: int,
                 armour: list,
                 weapon: dict,
                 potion: dict = None
                 ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.protection += sum(part.get("protection", 0)
                               for part in self.armour)

    def apply_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        if self.potion and "effect" in self.potion:
            effects = self.potion.get("effect")
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        for knight in (KNIGHTS):
            if knight["hp"] < 0:
                knight["hp"] = 0
