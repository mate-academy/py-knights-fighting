from app.knights.knight import Knight
from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion
from app.battle.fight import fight


def create_knight(config):
    armour = [Armour(a["protection"]) for a in config.get("armour", [])]
    weapon = Weapon(config["weapon"]["power"])
    potion = (
        Potion(config["potion"]["effect"])
        if config.get("potion")
        else None
    )

    return Knight(
        name=config["name"],
        hp=config["hp"],
        power=config["power"],
        armour=armour,
        weapon=weapon,
        potion = potion,
    )


def battle(knights_config: dict) -> dict:
    lancelot = create_knight(knights_config["lancelot"])
    mordred = create_knight(knights_config["mordred"])
    arthur = create_knight(knights_config["arthur"])
    red_knight = create_knight(knights_config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
