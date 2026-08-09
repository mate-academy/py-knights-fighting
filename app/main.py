from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon
from app.knight.knight import Knight


def create_potion(potion_config: dict) -> Potion | None:
    if potion_config is None:
        return None

    effect = potion_config.get("effect", {})
    return Potion(
        potion_config["name"],
        hp=effect.get("hp", 0),
        power=effect.get("power", 0),
        protection=effect.get("protection", 0),
    )


def create_knight(knight_config: dict) -> Knight:
    armour_config = knight_config.get(
        "armour",
        knight_config.get("equipment", []),
    )

    return Knight(
        knight_config["name"],
        knight_config["power"],
        knight_config["hp"],
        [
            Armour(
                armour_item["part"],
                armour_item["protection"],
            )
            for armour_item in armour_config
        ],
        Weapon(
            knight_config["weapon"]["name"],
            knight_config["weapon"]["power"],
        ),
        create_potion(knight_config["potion"]),
    )


def convert_knights(knights: dict | list[Knight]) -> list[Knight]:
    if isinstance(knights, dict):
        return [
            create_knight(knights["lancelot"]),
            create_knight(knights["arthur"]),
            create_knight(knights["mordred"]),
            create_knight(knights["red_knight"]),
        ]

    return knights


def battle_between_two(knight_one: Knight, knight_two: Knight) -> dict:
    knight_one_battle_hp = knight_one.calculate_hp() - (
        knight_two.calculate_power() - knight_one.calculate_protection()
    )
    knight_two_battle_hp = knight_two.calculate_hp() - (
        knight_one.calculate_power() - knight_two.calculate_protection()
    )

    if knight_one_battle_hp <= 0:
        knight_one_battle_hp = 0

    if knight_two_battle_hp <= 0:
        knight_two_battle_hp = 0

    return {
        knight_one.name: knight_one_battle_hp,
        knight_two.name: knight_two_battle_hp,
    }


def battle(knights: dict | list[Knight]) -> dict:
    knights = convert_knights(knights)
    return battle_between_two(knights[0], knights[2]) | battle_between_two(
        knights[1], knights[3]
    )
