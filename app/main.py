from app.knights.knight import Knight
from app.knights.weapon import Weapon
from app.knights.armour import Armour
from app.knights.potion import Potion
from app.config.knights_config import KNIGHTS


def build_knight(data: dict) -> Knight:
    weapon = Weapon(**data["weapon"])
    armour = [Armour(**a) for a in data.get("armour", [])]
    potion = Potion(**data["potion"]) if data.get("potion") else None
    return Knight(
        name=data["name"],
        hp=data["hp"],
        power=data["power"],
        weapon=weapon,
        armour=armour,
        potion=potion,
    )


def battle(knight1: Knight, knight2: Knight) -> dict[str, int]:
    knight1.take_damage(knight2.power)
    knight2.take_damage(knight1.power)
    return {knight1.name: knight1.hp, knight2.name: knight2.hp}


def main() -> None:
    red_knight = build_knight(KNIGHTS["red_knight"])
    x_knight = build_knight(KNIGHTS["x_knight"])
    result = battle(red_knight, x_knight)
    print(result)


if __name__ == "__main__":
    main()
