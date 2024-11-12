class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: None,
                 weapon: None,
                 potion: None) -> None:
        self.protection = 0
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion
        self.apply_equipment()

    def apply_equipment(self) -> None:
        self.power = (self.power
                      + (self.weapon.power if self.weapon.power else 0))
        self.protection = sum(item.protection for item in self.armour)

        if self.potion:
            self.hp += self.potion.effect.hp
            self.power += self.potion.effect.power
