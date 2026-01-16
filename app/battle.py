from typing import Dict
from app.knight import Knight, Weapon, ArmourPart, Potion


def create_knight(data: dict) -> Knight:
    name = data["name"]
    power = data["power"]
    hp = data["hp"]

    weapon_data = data["weapon"]
    weapon = Weapon(name=weapon_data["name"], power=weapon_data["power"])

    armour_parts = [
        ArmourPart(part=a["part"], protection=a["protection"])
        for a in data.get("armour", [])
    ]

    potion_data = data.get("potion")
    potion = None
    if potion_data:
        potion = Potion(name=potion_data["name"], effect=potion_data["effect"])

    return Knight(
        name=name,
        power=power,
        hp=hp,
        armour=armour_parts,
        weapon=weapon,
        potion=potion,
    )


def run_battle(knights_config: Dict) -> Dict[str, int]:
    # Створюємо об'єкти
    lancelot = create_knight(knights_config["lancelot"])
    mordred = create_knight(knights_config["mordred"])
    arthur = create_knight(knights_config["arthur"])
    red_knight = create_knight(knights_config["red_knight"])

    # Готуємо
    for knight in [lancelot, mordred, arthur, red_knight]:
        knight.prepare()

    # Битви
    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }
