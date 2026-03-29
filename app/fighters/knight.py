class Knight:
    knights = {}

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: dict | None,
            armour: dict | None,
            potion: dict | None,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        self.weapon = weapon
        self.armour = armour
        self.potion = potion
        Knight.knights[self.name] = self

    def up_protection(self) -> None:
        for armor in self.armour:
            self.protection += armor["protection"]

    def drink_potion(self) -> None:
        if self.potion is not None:
            self.hp += self.potion["effect"].get("hp", 0)
            self.power += self.potion["effect"].get("power", 0)
            self.protection += self.potion["effect"].get("protection", 0)

    def put_on_weapon(self) -> None:
        self.power += self.weapon["power"]

    def knight_hp(self) -> int:
        return self.hp
