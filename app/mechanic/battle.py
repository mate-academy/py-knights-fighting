from app.knight.armour import Armour
from app.knight.knight import Knight
from app.knight.weapon import Weapon
from app.knight.potion import Potion
from app.mechanic.prepare import prepare


def battle(knights_config: dict) -> dict[str, int]:
    def create_knight(data: dict) -> Knight:
        return Knight(
            name=data["name"],
            hp=data["hp"],
            power=data["power"],
            weapon=Weapon(**data["weapon"]),
            armour=Armour(data.get("armour", [])),
            potion=Potion(**data["potion"]) if data.get("potion") else None,
        )

    names = ["lancelot", "mordred", "arthur", "red_knight"]
    knights = {name: create_knight(knights_config[name]) for name in names}

    result = {}
    result.update(_fight(knights["lancelot"], knights["mordred"]))
    result.update(_fight(knights["arthur"], knights["red_knight"]))

    return result


def _fight(knight_1: Knight, knight_2: Knight) -> dict[str, int]:
    prepare(knight_1)
    prepare(knight_2)

    knight_1.hp -= max(0, knight_2.power - knight_1.protection)
    knight_2.hp -= max(0, knight_1.power - knight_2.protection)

    knight_1.hp = max(0, knight_1.hp)
    knight_2.hp = max(0, knight_2.hp)

    return {
        knight_1.name: knight_1.hp,
        knight_2.name: knight_2.hp,
    }
