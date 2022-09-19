from app.stats.features import knight_features
from app.knight.battles import first_battle, second_battle


def battle(knights_info):
    lancelot = knight_features(knights_info, knight_name="lancelot")
    arthur = knight_features(knights_info, knight_name="arthur")
    mordred = knight_features(knights_info, knight_name="mordred")
    red_knight = knight_features(knights_info, knight_name="red_knight")

    first_battle(lancelot, mordred)
    second_battle(arthur, red_knight)
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
