class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: dict,
            armor: list,
            potion: dict

    ) -> None:
        self.name = name.replace("_", " ")
        self.hp = hp
        self.power = power
        self.weapon = weapon
        self.armor = armor
        self.potion = potion
        self.protection = 0

    def common_settings(self) -> dict:

        temp_settings = {}
        current_protection = 0
        current_power = self.weapon["power"]
        current_hp = 0

        if self.armor:
            for part_of_armour in self.armor:
                current_protection += part_of_armour["protection"]

        if self.potion:
            for effect, value in self.potion["effect"].items():

                if effect == "protection":
                    current_protection += value
                    temp_settings["total_protection"] = \
                        (
                            self.protection + current_protection
                    )

                if effect == "power":
                    current_power += value
                    temp_settings["total_power"] = \
                        (
                            self.power + current_power
                    )

                if effect == "hp":
                    current_hp += value
                    temp_settings["total_hp"] = self.hp + current_hp

        return temp_settings
