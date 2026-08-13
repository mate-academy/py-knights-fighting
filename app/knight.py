class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: None
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        self.default_hp = self.hp

    def preparation(self) -> None:
        self.apply_power()
        self.apply_armour()
        if self.potion is not None:
            self.apply_potion()

    def apply_armour(self) -> None:
        for item in self.armour:
            self.protection += item["protection"]

    def apply_power(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        effect = self.potion["effect"]
        if effect.get("power"):
            self.power += effect["power"]
        if effect.get("hp"):
            self.hp += effect["hp"]
        if effect.get("protection"):
            self.protection += effect["protection"]

    def rest(self) -> None:
        self.hp = self.default_hp
