from app.data.knights import KNIGHTS
from app.knights_fighting.battle import Battle
from app.knights_fighting.knight import Knight


def prepare_knight(knight_data: dict) -> Knight:
    knight = Knight(
        knight_data["name"],
        knight_data["power"],
        knight_data["hp"]
    )
    knight.prepare(
        knight_data["weapon"],
        knight_data["armour"],
        knight_data["potion"]
    )
    return knight


def battle(knights_data: dict) -> dict:
    # BATTLE PREPARATIONS:
    lancelot = prepare_knight(knights_data["lancelot"])
    arthur = prepare_knight(knights_data["arthur"])
    mordred = prepare_knight(knights_data["mordred"])
    red_knight = prepare_knight(knights_data["red_knight"])

    # BATTLE:
    lancelot_vs_mordred_fight = Battle.fight(lancelot, mordred)
    arthur_vs_red_knight_fight = Battle.fight(arthur, red_knight)

    return {**lancelot_vs_mordred_fight, **arthur_vs_red_knight_fight}


print(battle(KNIGHTS))
