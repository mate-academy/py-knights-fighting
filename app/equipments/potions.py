class Potion:
    potions = {}

    def use_potion(self) -> None:
        if Potion.potions[self.name] is not None:
            for effect in ("hp", "power", "protection"):
                if effect not in Potion.potions[self.name]["effect"]:
                    Potion.potions[self.name]["effect"][effect] = 0
            self.power += Potion.potions[self.name]["effect"]["power"]
            self.protection += (Potion.potions[self.name]
                                ["effect"]["protection"])
            self.hp += Potion.potions[self.name]["effect"]["hp"]
