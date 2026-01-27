from app.knights.models import Knight
from app.knights.equipment import Armour, Weapon, Potion
from app.battle.mechanics import fight


def battle(knights_config: dict) -> dict:
    def make_knight(data: dict) -> Knight:
        armour_objs = [
            Armour(a["part"],
                   a["protection"]) for a in data.get("armour", [])
        ]

        weapon_data = data.get("weapon")
        weapon_obj = Weapon(
            weapon_data["name"], weapon_data["power"]
        ) if weapon_data else None

        potion_data = data.get("potion")
        potion_obj = Potion(
            potion_data["name"], potion_data["effect"]
        ) if potion_data else None

        return Knight(
            name=data["name"],
            hp=data["hp"],
            power=data["power"],
            armour=armour_objs,
            weapon=weapon_obj,
            potion=potion_obj,
        )

    knights = {key: make_knight(cfg) for key, cfg in knights_config.items()}

    # бої
    result1 = fight(knights["lancelot"], knights["mordred"])
    result2 = fight(knights["arthur"], knights["red_knight"])

    return {
        "Lancelot": result1["Lancelot"],
        "Arthur": result2["Arthur"],
        "Mordred": result1["Mordred"],
        "Red Knight": result2["Red Knight"],
    }
