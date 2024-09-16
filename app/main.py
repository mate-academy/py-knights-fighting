from app.data.knights_config import KNIGHTS
from app.knight.processing import process_knight
from app.battle.simulation import attack


def battle(knights_config: KNIGHTS) -> dict:

    lancelot = process_knight(knights_config["lancelot"])
    arthur = process_knight(knights_config["arthur"])
    mordred = process_knight(knights_config["mordred"])
    red_knight = process_knight(knights_config["red_knight"])

    lancelot_hp = attack(lancelot, mordred)
    arthur_hp = attack(arthur, red_knight)
    mordred_hp = attack(mordred, lancelot)
    red_knight_hp = attack(red_knight, arthur)

    return {
        lancelot.name: lancelot_hp,
        arthur.name: arthur_hp,
        mordred.name: mordred_hp,
        red_knight.name: red_knight_hp,
    }


print(battle(KNIGHTS))
