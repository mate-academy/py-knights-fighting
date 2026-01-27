from app.knights.models import Knight
from app.knights.equipment import Armour, Weapon, Potion
from app.battle.mechanics import fight


def battle(knights_config: dict) -> dict:
    def make_knight(data: dict) -> Knight:
        # броня: список словників → список Armour
        armour_objs = [
            Armour(a["part"],
                   a["protection"]) for a in data.get("armour", [])
        ]

        # зброя: словник → Weapon
        weapon_data = data.get("weapon")
        weapon_obj = Weapon(weapon_data["name"],
                            weapon_data["power"])\
            if weapon_data else None

        # зілля: словник → Potion
        potion_data = data.get("potion")
        potion_obj = Potion(potion_data["name"],
                            potion_data["effect"])\
            if potion_data else None

        return Knight(
            name=data["name"],
            hp=data["hp"],
            power=data["power"],
            armour=armour_objs,
            weapon=weapon_obj,
            potion=potion_obj,
        )

    # створюємо лицарів
    red_knight = make_knight(knights_config["red_knight"])
    arthur = make_knight(knights_config["arthur"])
    lancelot = make_knight(knights_config["lancelot"])
    mordred = make_knight(knights_config["mordred"])

    # бої
    result1 = fight(lancelot, mordred)
    result2 = fight(arthur, red_knight)

    # повертаємо результат у форматі, який очікують тести
    return {
        "Lancelot": result1["Lancelot"],
        "Arthur": result2["Arthur"],
        "Mordred": result1["Mordred"],
        "Red Knight": result2["Red Knight"],
    }
