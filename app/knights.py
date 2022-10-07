class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @staticmethod
    def start_config(knights_config: dict) -> dict:
        knights = {}
        for stats in knights_config.values():
            knight = Knight(
                name=stats["name"],
                power=stats["power"],
                hp=stats["hp"]
            )
            for knight_armour in stats["armour"]:
                knight.protection += knight_armour["protection"]
            knight.power += stats["weapon"]["power"]
            if stats["potion"] is not None:
                if "power" in stats["potion"]["effect"]:
                    knight.power += stats["potion"]["effect"]["power"]

                if "protection" in stats["potion"]["effect"]:
                    knight.protection += \
                        stats["potion"]["effect"]["protection"]

                if "hp" in stats["potion"]["effect"]:
                    knight.hp += stats["potion"]["effect"]["hp"]
            knights[stats["name"]] = knight
        return knights
