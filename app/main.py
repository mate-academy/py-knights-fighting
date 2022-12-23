from app.for_act.knights import KNIGHTS
from app.for_act.defeat import defeat_check
from app.for_knight.armour import apply_armour
from app.for_knight.potion import apply_potion
from app.for_knight.weapon import apply_weapon


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    knight_list = []
    # apply armour, weapon and potion
    for name in knights_config:
        knight = knights_config[f"{name}"]
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)
        knight_list.append(name)
    # participants get ready:
    knight1 = knights_config[f"{knight_list[0]}"]
    knight2 = knights_config[f"{knight_list[1]}"]
    knight3 = knights_config[f"{knight_list[2]}"]
    knight4 = knights_config[f"{knight_list[3]}"]
    # BATTLES:

    # 1 Lancelot vs Mordred:
    knight1["hp"] -= knight3["power"] - knight1["protection"]
    knight3["hp"] -= knight1["power"] - knight3["protection"]

    # 2 Arthur vs Red Knight:
    knight2["hp"] -= knight4["power"] - knight2["protection"]
    knight4["hp"] -= knight2["power"] - knight4["protection"]

    # check if someone fell in battle
    defeat_check([knight1, knight2, knight3, knight4])

    # show battle results:
    return {
        knight1["name"]: knight1["hp"],
        knight2["name"]: knight2["hp"],
        knight3["name"]: knight3["hp"],
        knight4["name"]: knight4["hp"],
    }


print(battle(KNIGHTS))
