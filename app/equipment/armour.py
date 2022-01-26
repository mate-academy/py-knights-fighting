from app.characters.knight import Knight


class Armour:

    armours = {}

    def __init__(self, name, protection):
        self.name = name
        self.protection = protection

    def __repr__(self):
        return f"{self.protection}"

    @staticmethod
    def protect_the_knight(knights):

        for pers in knights.values():
            if len(pers["armour"]) > 0:
                for part in pers["armour"]:
                    Armour.armours[part["part"]] = \
                        Armour(part["part"], part["protection"])
                    Knight.knights[pers["name"]].armour = \
                        Armour.armours[part["part"]]
                    Knight.knights[pers["name"]].protection += \
                        part["protection"]
        return Armour.armours
