from app.Knights.armor import Armor


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    # this method takes potions effects and normalized it
    # for the "build_knights_couples_from_config" func

    @staticmethod
    def potion_normalizer(potion: dict) -> dict:
        potion_effects = {
            "power": potion.get("power", 0),
            "hp": potion.get("hp", 0),
            "protection": potion.get("protection", 0)
        }
        return potion_effects

    # this method builds couples of knights that will fight

    @staticmethod
    def build_knight_couples_from_cfg(
        knights: dict
    ) -> list[tuple["Knight", "Knight"]]:

        fighters_dict = {}
        for name, stats in knights.items():
            potion_cfg = stats.get("potion")
            effects = potion_cfg.get("effect", {}) if potion_cfg else {}
            potion = Knight.potion_normalizer(effects)
            hp = stats["hp"] + potion["hp"]
            power = stats["power"] + stats["weapon"]["power"] + potion["power"]
            armor = Armor(stats["armour"])
            protection = armor.total_armor() + potion["protection"]
            knight = Knight(stats["name"], power, hp, protection)
            fighters_dict[name] = knight

        return [
            (
                fighters_dict.get("lancelot"),
                fighters_dict.get("mordred")
            ),
            (
                fighters_dict.get("arthur"),
                fighters_dict.get("red_knight")
            )
        ]
