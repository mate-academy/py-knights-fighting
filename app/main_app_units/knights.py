class Knight:

    def __init__(self, name: str, power: int, hp: int, **kwargs) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.gear = kwargs

    def gear_converter(self) -> None:
        self.potion_converter()
        self.armour_converter()
        self.power_converter()

    def power_converter(self) -> None:
        if self.gear.get("weapon"):
            self.power += self.gear["weapon"]["power"]

    def armour_converter(self) -> None:
        if self.gear["armour"]:
            for piece_of_armor in self.gear["armour"]:
                self.hp += piece_of_armor["protection"]

    def potion_converter(self) -> None:
        if self.gear["potion"]:
            for stat in self.gear["potion"]["effect"]:
                if stat == "power":
                    self.power += self.gear["potion"]["effect"][stat]
                elif stat == "hp" or stat == "protection":
                    self.hp += self.gear["potion"]["effect"][stat]
