from app.knights_data import KNIGHTS
from app.knights import Knight
from app.equipment import Weapon, Armour, Potion
from app.battle import battle, battle_round


def dict_to_knight(data: dict) -> Knight:
    weapon = Weapon(**data["weapon"]) if data.get("weapon") else None
    armour = []
    for armour_part in data.get("armour", []):
        armour.append(
            Armour(
                name=armour_part.get("name", armour_part.get("part", "")),
                protection=armour_part["protection"]
            )
        )
    potion = Potion(**data["potion"]) if data.get("potion") else None
    return Knight(
        name=data["name"],
        hp=data["hp"],
        base_power=data["power"],
        base_protection=0,
        accuracy=data.get("accuracy", 0.8),
        evasion=data.get("evasion", 0.1),
        weapon=weapon,
        armour=armour,
        potion=potion
    )


knights = {name: dict_to_knight(data) for name, data in KNIGHTS.items()}
for knight in knights.values():
    knight.apply_equipment()

results = battle_round(
    knights["lancelot"],
    knights["mordred"],
    knights["arthur"],
    knights["red_knight"]
)

for name, stats in results.items():
    print(
        f"{name}: HP={stats["hp"]}, "
        f"Accuracy={stats["accuracy"] : .2f}, "
        f"Evasion={stats["evasion"] : .2f}"
    )

__all__ = ["battle", "battle_round"]
