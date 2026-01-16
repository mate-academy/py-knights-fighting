from app.fighters.fighter import Fighter
from app.fighters.armour import Armour
from app.fighters.weapon import Weapon
from app.fighters.potion import Potion
from app.config import KNIGHTS


def create_fighter(knight_data: dict) -> Fighter:
    fighter = Fighter(
        name=knight_data["name"],
        power=knight_data["power"],
        hp=knight_data["hp"],
        weapon=Weapon(**knight_data["weapon"]),
    )

    for armour_data in knight_data["armour"]:
        fighter.add_armour(Armour(**armour_data))

    if knight_data["potion"]:
        fighter.add_potion(Potion(**knight_data["potion"]))

    return fighter


def battle(knights_config: dict) -> dict:
    lancelot = create_fighter(knights_config["lancelot"])
    arthur = create_fighter(knights_config["arthur"])
    mordred = create_fighter(knights_config["mordred"])
    red_knight = create_fighter(knights_config["red_knight"])

    lancelot_stats = lancelot.update_fighter()
    arthur_stats = arthur.update_fighter()
    mordred_stats = mordred.update_fighter()
    red_knight_stats = red_knight.update_fighter()

    lancelot_stats["hp"] -= (
        mordred_stats["power"] - lancelot_stats["protection"]
    )
    mordred_stats["hp"] -= (
        lancelot_stats["power"] - mordred_stats["protection"]
    )

    if lancelot_stats["hp"] <= 0:
        lancelot_stats["hp"] = 0
    if mordred_stats["hp"] <= 0:
        mordred_stats["hp"] = 0

    arthur_stats["hp"] -= (
        red_knight_stats["power"] - arthur_stats["protection"]
    )
    red_knight_stats["hp"] -= (
        arthur_stats["power"] - red_knight_stats["protection"]
    )

    if arthur_stats["hp"] <= 0:
        arthur_stats["hp"] = 0
    if red_knight_stats["hp"] <= 0:
        red_knight_stats["hp"] = 0

    return {
        lancelot.name: lancelot_stats["hp"],
        arthur.name: arthur_stats["hp"],
        mordred.name: mordred_stats["hp"],
        red_knight.name: red_knight_stats["hp"],
    }


print(battle(KNIGHTS))
