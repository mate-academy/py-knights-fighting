class Knights:

    def __init__(self,
                 name: str = "",
                 hp: int = 0,
                 power: int = 0,
                 protection: int = 0):
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    @staticmethod
    def knight_config(knights_dict: dict):
        knights = {}
        # create knight objects and save to dict
        for key, value in knights_dict.items():
            knight = Knights(name=value["name"],
                             hp=value["hp"],
                             power=value["power"])
            # apply armour
            for a in value["armour"]:
                knight.protection += a["protection"]

            # apply weapon
            knight.power += value["weapon"]["power"]

            # apply potion if exist
            if value["potion"] is not None:
                if "power" in value["potion"]["effect"]:
                    knight.power += value["potion"]["effect"]["power"]

                if "protection" in value["potion"]["effect"]:
                    protection = value["potion"]["effect"]["protection"]
                    knight.protection += protection

                if "hp" in value["potion"]["effect"]:
                    knight.hp += value["potion"]["effect"]["hp"]

            knights[value["name"]] = knight
        return knights
