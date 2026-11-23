from app.battle import fight
from app.knights.armour import Armour
from app.knights.knight import Knight
from app.knights.potion import Potion
from app.knights.weapon import Weapon


def create_knight(data: dict) -> Knight:
    armour = [
        Armour(item["part"], item["protection"])
        for item in data["armour"]
    ]
    weapon = Weapon(**data["weapon"])
    potion_data = data["potion"]
    potion = Potion(**potion_data) if potion_data is not None else None
    return Knight(
        name=data["name"],
        base_power=data["power"],
        hp=data["hp"],
        armour=armour,
        weapon=weapon,
        potion=potion,
    )


def battle(knights_config):
    lancelot = create_knight(knights_config["lancelot"])
    mordred = create_knight(knights_config["mordred"])
    arthur = create_knight(knights_config["arthur"])
    red_knight = create_knight(knights_config["red_knight"])
    fight(lancelot, mordred)
    fight(arthur, red_knight)
    return {
        knight.name: knight.hp
        for knight in (lancelot, arthur, mordred, red_knight)
    }
