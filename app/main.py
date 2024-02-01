from app.knights.players import KNIGHTS
from app.knights.knights import Knight
from app.battle.battle import Battle


def battle(player: dict) -> dict:
    lancelot = Knight(**player["lancelot"])
    mordred = Knight(**player["mordred"])
    arthur = Knight(**player["arthur"])
    red_knight = Knight(**player["red_knight"])
    first_battle = Battle(lancelot, mordred)
    second_battle = Battle(arthur, red_knight)
    Battle.before_battle()
    first_battle.battle_damage()
    second_battle.battle_damage()
    return Battle.battles_result()


if __name__ == "__main__":
    print(battle(KNIGHTS))
