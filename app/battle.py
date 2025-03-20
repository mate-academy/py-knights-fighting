from app.models.knight import Knight
from app.models.weapon import Weapon
from app.models.armour import Armour
from app.models.potion import Potion


def battle_pair(knight1: Knight, knight2: Knight) -> None:
    knight1.receive_damage(knight2.power)
    knight2.receive_damage(knight1.power)


def create_knight_from_config(config: dict) -> dict:
    armour = [Armour(**a) for a in config["armour"]]
    weapon = Weapon(**config["weapon"])
    potion = Potion(**config["potion"]) if config["potion"] else None
    return Knight(
        config["name"],
        config["power"],
        config["hp"],
        armour,
        weapon,
        potion,
    )


def battle(knights_config: dict) -> dict:

    lancelot = create_knight_from_config(knights_config["lancelot"])
    arthur = create_knight_from_config(knights_config["arthur"])
    mordred = create_knight_from_config(knights_config["mordred"])
    red_knight = create_knight_from_config(knights_config["red_knight"])

    lancelot.apply_equipment()
    arthur.apply_equipment()
    mordred.apply_equipment()
    red_knight.apply_equipment()

    battle_pair(lancelot, mordred)
    battle_pair(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
