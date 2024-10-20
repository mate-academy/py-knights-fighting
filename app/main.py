from app.config.config import KNIGHTS
from app.knight.knight import Knight
from app.knight.weapon import Weapon
from app.knight.armour import Armour
from app.knight.potion import Potion


def create_knight(knight_data: dict) -> Knight:
    weapon = Weapon(
        name=knight_data["weapon"]["name"],
        power=knight_data["weapon"]["power"],
    )

    armour = [
        Armour(part=item["part"], protection=item["protection"])
        for item in knight_data["armour"]
    ]

    potion = None
    if knight_data.get("potion"):
        potion = Potion(
            name=knight_data["potion"]["name"],
            effect=knight_data["potion"]["effect"],
        )

    return Knight(
        name=knight_data["name"],
        power=knight_data["power"],
        hp=knight_data["hp"],
        armour=armour,
        weapon=weapon,
        potion=potion,
    )


def battle(knights_config: dict[str, dict]) -> dict[str, int]:
    knights = {
        name: create_knight(params) for name, params in knights_config.items()
    }

    for knight in knights.values():
        knight.prepare_for_battle()

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    lancelot.get_hit(mordred.power)
    mordred.get_hit(lancelot.power)
    arthur.get_hit(red_knight.power)
    red_knight.get_hit(arthur.power)

    return {knight.name: knight.hp for knight in knights.values()}


print(battle(KNIGHTS))
