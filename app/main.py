from app.models.knight import Knight
from app.models.weapon import Weapon
from app.models.armour import Armour
from app.models.potion import Potion
from app.models.battle import Battle
from app.data import KNIGHTS


def create_knight(data: dict) -> Knight:
    armour = [Armour(**a) for a in data.get("armour", [])]
    weapon = Weapon(**data["weapon"]) if data.get("weapon") else None
    potion = Potion(**data["potion"]) if data.get("potion") else None
    return Knight(
        name=data["name"],
        power=data["power"],
        hp=data["hp"],
        armour=armour,
        weapon=weapon,
        potion=potion,
    )


def battle(knights_data: dict) -> dict:
    lancelot = create_knight(knights_data["lancelot"])
    mordred = create_knight(knights_data["mordred"])
    arthur = create_knight(knights_data["arthur"])
    red_knight = create_knight(knights_data["red_knight"])

    battle1 = Battle(lancelot, mordred)
    battle2 = Battle(arthur, red_knight)

    result1 = battle1.fight()
    result2 = battle2.fight()

    return {**result1, **result2}


if __name__ == "__main__":
    print(battle(KNIGHTS))
