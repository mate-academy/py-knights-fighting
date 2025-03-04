from app.models.armour import Armour
from app.models.knight import Knight
from app.models.potion import Potion
from app.models.weapon import Weapon

KnightData = dict[
    str,
    str
    | int
    | list[dict[str, int | str]]
    | dict[str, int | str]
    | dict[str, str | dict[str, int]]
    | None,
]


def create_armour(
    armour_list: list[dict[str, int | str]]
) -> list[Armour]:
    return [
        Armour(piece["part"], piece["protection"])
        for piece in armour_list
    ]


def create_weapon(data: dict[str, int | str]) -> Weapon:
    return Weapon(
        data["name"],
        data["power"],
    )


def create_potion(
    data: dict[str, dict[str, int] | str] | None
) -> Potion | None:
    return (
        Potion(data["name"], data["effect"])
        if data
        else None
    )


def prepare_knight(data: KnightData) -> Knight:
    return Knight(
        name=data["name"],
        power=data["power"],
        hp=data["hp"],
        armour=create_armour(data["armour"]),
        weapon=create_weapon(data["weapon"]),
        potion=create_potion(data["potion"]),
    )


def battle(knights_config: dict[str, KnightData]) -> dict[str, int]:
    knights = {
        name: prepare_knight(data)
        for name, data in knights_config.items()
    }

    lancelot, mordred, arthur, red_knight = (
        knights["lancelot"],
        knights["mordred"],
        knights["arthur"],
        knights["red_knight"],
    )

    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }
