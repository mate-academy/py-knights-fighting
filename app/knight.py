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

    @staticmethod
    def battle_preparations(knight: "Knight") -> None:
        for one_of_armours in knight.armour:
            knight.protection += one_of_armours["protection"]

        knight.power += knight.weapon["power"]

        if knight.potion is not None:
            if "power" in knight.potion["effect"]:
                knight.power += knight.potion["effect"]["power"]

            if "protection" in knight.potion["effect"]:
                knight.protection += (
                    knight.potion)["effect"]["protection"]

            if "hp" in knight.potion["effect"]:
                knight.hp += knight.potion["effect"]["hp"]
