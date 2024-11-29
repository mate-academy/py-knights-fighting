class Knight:

    knights_instances = {}

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list = None,
                 weapon: dict = None,
                 potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = None
        Knight.knights_instances[name] = self

    def set_knight_protection(self) -> int:
        self.protection = self.calculating_protection_from_armor()
        return self.protection

    def calculating_protection_from_armor(self) -> int:
        self.protection = 0
        if self.armour:
            for unit in self.armour:
                self.protection += unit.get("protection", 0)
        return self.protection

    def applying_potion(self) -> None:
        if self.potion:
            self.power += self.potion.get("effect").get("power", 0)
            self.hp += self.potion.get("effect").get("hp", 0)
            self.protection += self.potion.get("effect").get("protection", 0)

    def weapon_to_battle(self) -> None:
        self.power += self.weapon.get("power")

    def __str__(self) -> str:
        return (f"Sir {self.name}: \npower {self.power}, hp {self.hp}\n"
                f"has armour: {self.armour}\n"
                f"weapon: {self.weapon}\n"
                f"potion: {self.potion}\n")
