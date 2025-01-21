class Knight:
    def __init__(
            self,
            knight_data: dict
    ) -> None:
        self.name = knight_data.get("name")
        self.power = knight_data.get("power")
        self.hp = knight_data.get("hp")
        self.armour = knight_data.get("armour", [])
        self.weapon = knight_data.get("weapon")
        self.potion = knight_data.get("potion", None)

        self.protection = self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> int:
        return sum([item.get("protection", 0) for item in self.armour])

    def apply_weapon(self) -> None:
        self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        if self.potion is not None:
            for buff, value in self.potion.get("effect").items():
                if buff == "power":
                    self.power += value
                elif buff == "protection":
                    self.protection += value
                else:
                    self.hp += value
