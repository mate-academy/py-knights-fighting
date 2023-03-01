class Potion:
    """
    method for drinking potions, potion = KNIGHTS[name]["potion"]
    """
    @staticmethod
    def apply_potion(potion, knight):
        if potion is not None:
            if "hp" in potion["effect"]:
                knight.hp += potion["effect"]["hp"]
            if "power" in potion["effect"]:
                knight.power += potion["effect"]["power"]
            if "protection" in potion["effect"]:
                knight.protection += potion["effect"]["protection"]
        return knight
