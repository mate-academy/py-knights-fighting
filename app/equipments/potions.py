class Potion:
    potions = {}

    @staticmethod
    def use(knight: None) -> None:
        if Potion.potions[knight.name] is not None:
            if "power" in Potion.potions[knight.name]["effect"]:
                knight.power += Potion.potions[knight.name]["effect"]["power"]

            if "protection" in Potion.potions[knight.name]["effect"]:
                knight.protection += (Potion.potions[knight.name]
                                      ["effect"]["protection"])

            if "hp" in Potion.potions[knight.name]["effect"]:
                knight.hp += Potion.potions[knight.name]["effect"]["hp"]
