from app.characters.knight import Knight


class Potion:

    potions = {}

    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def __repr__(self):
        return f"{self.effect}"

    @staticmethod
    def give_a_potion(knights):

        for knight in knights.values():
            if knight["potion"]:
                Potion.potions[knight["potion"]["name"]] = Potion(
                    knight["potion"]["name"],
                    knight["potion"]["effect"]
                )
                Knight.knights[knight["name"]].potion = \
                    Potion.potions[knight["potion"]["name"]]

                for effect in knight["potion"]["effect"]:
                    if effect == "power":
                        Knight.knights[knight["name"]].power += \
                            knight["potion"]["effect"]["power"]
                    if effect == "hp":
                        Knight.knights[knight["name"]].hp += \
                            knight["potion"]["effect"]["hp"]
                    if effect == "protection":
                        Knight.knights[knight["name"]].protection += \
                            knight["potion"]["effect"]["protection"]

        return Potion.potions
