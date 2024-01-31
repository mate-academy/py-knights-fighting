from app.knights.players import KNIGHTS
from app.knights.knights import Knights
from app.battle.battle import Battle


def battle(player: dict) -> dict:
    lancelot = Knights(**player["lancelot"])
    mordred = Knights(**player["mordred"])
    arthur = Knights(**player["arthur"])
    red_knight = Knights(**player["red_knight"])
    first_battle = Battle(lancelot, mordred)
    second_battle = Battle(arthur, red_knight)
    Battle.before_battle()
    first_battle.battle_damage()
    second_battle.battle_damage()
    return Battle.battles_result()


if __name__ == "__main__":
    print(battle(KNIGHTS))
