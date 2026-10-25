class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Knight:
    @staticmethod
    def fight(first_knight: Knight, second_knight: Knight) -> None:
        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection

        # check if someone fell in battle
        if first_knight.hp <= 0:
            first_knight.hp = 0

        if second_knight.hp <= 0:
            second_knight.hp = 0

    @staticmethod
    def knight_from_dict(knight_dict: dict) -> Knight:
        return Knight(knight_dict["name"],
                      knight_dict["power"],
                      knight_dict["hp"],
                      Weapon(knight_dict["weapon"]["name"],
                             knight_dict["weapon"]["power"]),
                      knight_dict["armour"],
                      knight_dict["potion"])

    def __init__(self, name: str, power: int,
                 hp: int, weapon: Weapon, armour: dict = None,
                 potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour if armour is not None else []
        self.potion = potion

        # apply armour
        self.protection = 0
        for armour_piece in self.armour:
            self.protection += armour_piece["protection"]

        # apply weapon
        self.power += self.weapon.power

        # apply potion if exist
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
