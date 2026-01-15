from app.championship.competition import Competition
from app.participants.knight import Knight
from app.participants.stats import knights


def battle(knights_config: dict) -> dict:
    competition = Competition()

    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    battle_result = competition.fight(lancelot, mordred)
    battle_result.update(competition.fight(arthur, red_knight))

    return battle_result


print(battle(knights))
