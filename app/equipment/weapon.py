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

        for knight in knights.values():
            if knight["weapon"]:
                Weapon.weapons[knight["weapon"]["name"]] = Weapon(
                    knight["weapon"]["name"],
                    knight["weapon"]["power"]
                )
                Knight.knights[knight["name"]].weapon = \
                    Weapon.weapons[knight["weapon"]["name"]]
                Knight.knights[knight["name"]].power += \
                    knight["weapon"]["power"]
        return Weapon.weapons
