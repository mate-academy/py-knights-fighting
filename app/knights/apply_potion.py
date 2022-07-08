class Potion:

    @staticmethod
    def app_potion(potion: dict, power, hp, protection):
        if "power" in potion["effect"]:
            power += potion["effect"]["power"]

        if "protection" in potion["effect"]:
            protection += potion["effect"]["protection"]

        if "hp" in potion["effect"]:
            hp += potion["effect"]["hp"]
        return power, hp, protection
