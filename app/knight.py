class Knights:

    def __init__(self,
                 name: str = "",
                 hp: int = 0,
                 power: int = 0,
                 protection: int = 0) -> None :
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    @staticmethod
    def knight_config(knights_dict: dict) -> dict:
        knights = {}

        for name, character in knights_dict.items():
            knight = Knights(name=character["name"],
                             hp=character["hp"],
                             power=character["power"])

            for armour in character["armour"]:
                knight.protection += armour["protection"]

            knight.power += character["weapon"]["power"]

            if character["potion"] is not None:
                stats = {"protection": knight.protection,
                         "power": knight.power,
                         "hp": knight.hp}
                for option in stats:
                    if option in character["potion"]["effect"]:

                        stats[option] += character["potion"]["effect"][option]

                knight.protection = stats["protection"]
                knight.power = stats["power"]
                knight.hp = stats["hp"]

            knights[character["name"]] = knight
        return knights
