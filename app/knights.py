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
                for effect, points in stats["potion"]["effect"].items():
                    potion_effects = {"power": 0, "hp": 0, "protection": 0}
                    if effect in stats["potion"]["effect"]:
                        potion_effects[effect] = points
                    knight.power += potion_effects["power"]
                    knight.hp += potion_effects["hp"]
                    knight.protection += potion_effects["protection"]
            knights[stats["name"]] = knight
        return knights
