class Knight:

    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict,
                 potion: (dict, None) = None) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:

        for armor in self.armour:
            self.protection += armor["protection"]

    def apply_weapon(self) -> None:

        self.power += self.weapon["power"]

    def apply_potion(self) -> None:

        if self.potion is not None:
            stats = ("protection", "power", "hp")
            for stat in stats:
                if stat in self.potion["effect"]:
                    if stat == "power":
                        self.power += self.potion["effect"][stat]
                    if stat == "hp":
                        self.hp += self.potion["effect"][stat]
                    if stat == "protection":
                        self.protection += self.potion["effect"][stat]

    def get_ready(self) -> None:
        self.apply_armour()
        self.apply_potion()
        self.apply_weapon()
