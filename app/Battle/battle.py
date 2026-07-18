from app.Knight_config.knight_config import Equipped_knight


def battle(pretendents:list = Equipped_knight) -> None:
    battle_result = []
    for ind, warrior in enumerate(pretendents):
        for opponent in pretendents[ind + 1:]:
            warrior_health_points = warrior.hp
            warrior_health_points -= opponent.power - warrior.protection
            opponent_health_points = opponent.hp
            opponent_health_points -= warrior.power - opponent.protection
            if warrior_health_points <= 0:
                warrior_health_points = 0
            if opponent_health_points <= 0:
               opponent_health_points = 0
            battle_result.append(f"Battle between: {warrior.name} vs {opponent.name}. "
                                 f"Results are: {warrior_health_points} and {opponent_health_points} respectively")

    return battle_result
