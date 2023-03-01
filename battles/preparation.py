class KnightsPrep:
    @staticmethod
    def count_protection(knight):
        for tool in knight.armour:
            knight.protection += tool["protection"]
        # return knight["protection"]

    @staticmethod
    def count_power(knight):
        knight.power += knight.weapon["power"]
        # return knight["power"]

    @staticmethod
    def apply_potion(knight):
        if knight.potion is not None:
            if "power" in knight.potion["effect"]:
                knight.power += knight.potion["effect"]["power"]
            if "protection" in knight.potion["effect"]:
                knight.protection += knight.potion["effect"]["protection"]
            if "hp" in knight.potion["effect"]:
                knight.hp += knight.potion["effect"]["hp"]
        # return knight["power"], knight["protection"], knight["hp"]
