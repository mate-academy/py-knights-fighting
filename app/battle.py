from app.models.knight import Knight
from app.models.weapon import Weapon
from app.models.armour import Armour
from app.models.potion import Potion


def build_knight(data: dict) -> Knight:
    knight = Knight(
        name=data["name"],
        power=data["power"],
        hp=data["hp"]
    )

    knight.weapon = Weapon(
        data["weapon"]["name"],
        data["weapon"]["power"]
    )

    knight.armour = [
        Armour(a["part"], a["protection"])
        for a in data["armour"]
    ]

    if data["potion"]:
        knight.potion = Potion(
            data["potion"]["name"],
            data["potion"]["effect"]
        )

    return knight


def battle(knights: dict) -> dict:
    lancelot = build_knight(knights["lancelot"])
    arthur = build_knight(knights["arthur"])
    mordred = build_knight(knights["mordred"])
    red_knight = build_knight(knights["red_knight"])

    for key in (lancelot, arthur, mordred, red_knight):
        key.apply_potion()

    # fights
    lancelot.take_damage(mordred.get_total_power())
    mordred.take_damage(lancelot.get_total_power())

    arthur.take_damage(red_knight.get_total_power())
    red_knight.take_damage(arthur.get_total_power())

    return {
        "Lancelot": lancelot.hp,
        "Arthur": arthur.hp,
        "Mordred": mordred.hp,
        "Red Knight": red_knight.hp,
    }
