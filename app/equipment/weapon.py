from app.characters.knight import Knight


class Weapon:

    weapons = {}

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __repr__(self):
        return f"{self.power}"

    @staticmethod
    def arm_the_knight(knights):

        for pers in knights.values():
            if pers["weapon"]:
                Weapon.weapons[pers["weapon"]["name"]] = Weapon(
                    pers["weapon"]["name"],
                    pers["weapon"]["power"]
                )
                Knight.knights[pers["name"]].weapon = \
                    Weapon.weapons[pers["weapon"]["name"]]
                Knight.knights[pers["name"]].power += \
                    pers["weapon"]["power"]
        return Weapon.weapons
