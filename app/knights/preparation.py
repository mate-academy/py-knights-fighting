class Knight:
    def __init__(self, name: str, power: int, hp: int, protection: int = 0):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @classmethod
    def create_knight(cls, knight_and_amo):
        knight = cls(knight_and_amo["name"],
                     knight_and_amo["power"],
                     knight_and_amo["hp"])

        for armor in knight_and_amo["armour"]:
            knight.protection += armor["protection"]

        knight.power += knight_and_amo["weapon"]["power"]

        if knight_and_amo["potion"] is not None:
            if "power" in knight_and_amo["potion"]["effect"]:
                knight.power += knight_and_amo["potion"]["effect"]["power"]

            if "protection" in knight_and_amo["potion"]["effect"]:
                knight.protection += \
                    knight_and_amo["potion"]["effect"]["protection"]

            if "hp" in knight_and_amo["potion"]["effect"]:
                knight.hp += knight_and_amo["potion"]["effect"]["hp"]

        return knight
