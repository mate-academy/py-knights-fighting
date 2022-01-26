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

        for pers in knights.values():
            if pers["potion"]:
                Potion.potions[pers["potion"]["name"]] = Potion(
                    pers["potion"]["name"],
                    pers["potion"]["effect"]
                )
                Knight.knights[pers["name"]].potion = \
                    Potion.potions[pers["potion"]["name"]]

                for effect in pers["potion"]["effect"]:
                    if effect == "power":
                        Knight.knights[pers["name"]].power += \
                            pers["potion"]["effect"]["power"]
                    if effect == "hp":
                        Knight.knights[pers["name"]].hp += \
                            pers["potion"]["effect"]["hp"]
                    if effect == "protection":
                        Knight.knights[pers["name"]].protection += \
                            pers["potion"]["effect"]["protection"]

        return Potion.potions
