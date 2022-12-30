class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion


def knights_instances_dict(knights_dict: dict) -> dict:
    return {
        knight_name: Knight(
            name=knight_stats["name"],
            power=knight_stats["power"],
            hp=knight_stats["hp"],
            armour=knight_stats["armour"],
            weapon=knight_stats["weapon"],
            potion=knight_stats["potion"])
        for knight_name, knight_stats in knights_dict.items()
    }
