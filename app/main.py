from app.for_act.knights import KNIGHTS
from app.for_act.defeat import defeat_check
from app.for_act.preparation import prepare_to_the_battle


def battle(knights_config: dict) -> dict:

    knight_list = []
    for name in knights_config:
        knight = knights_config[name]
        prepare_to_the_battle(knight)
        knight_list.append(name)

    knight1 = knights_config[knight_list[0]]
    knight2 = knights_config[knight_list[1]]
    knight3 = knights_config[knight_list[2]]
    knight4 = knights_config[knight_list[3]]

    knight1["hp"] -= knight3["power"] - knight1["protection"]
    knight3["hp"] -= knight1["power"] - knight3["protection"]
    knight2["hp"] -= knight4["power"] - knight2["protection"]
    knight4["hp"] -= knight2["power"] - knight4["protection"]

    defeat_check([knight1, knight2, knight3, knight4])

    return {
        knight1["name"]: knight1["hp"],
        knight2["name"]: knight2["hp"],
        knight3["name"]: knight3["hp"],
        knight4["name"]: knight4["hp"],
    }


print(battle(KNIGHTS))
