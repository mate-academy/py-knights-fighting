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
    def knight_config(knights_dict: dict) -> dict:
        dict_of_knights = {}
        for name, atribute in knights_dict.items():
            knight = Knights(name=atribute["name"],
                             hp=atribute["hp"],
                             power=atribute["power"])
            for armour in atribute["armour"]:
                knight.protection += armour["protection"]
            knight.power += atribute["weapon"]["power"]

            if atribute["potion"] is not None:
                stats = {"protection": knight.protection,
                         "power": knight.power,
                         "hp": knight.hp}

                for option in stats:
                    if option in atribute["potion"]["effect"]:
                        stats[option] += atribute["potion"]["effect"][option]

                knight.protection = stats["protection"]
                knight.power = stats["power"]
                knight.hp = stats["hp"]

            dict_of_knights[atribute["name"]] = knight
        return dict_of_knights
