class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: (dict, None),
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def get_ready_to_battle(self) -> None:
        self.protection += sum(item.
                               get("protection", 0)
                               for item in self.armour)
        self.power += self.weapon.get("power", 0)
        if self.potion:
            buff = self.potion.get("effect", {})
            self.power += buff.get("power", 0)
            self.hp += buff.get("hp", 0)
            self.protection += buff.get("protection", 0)
