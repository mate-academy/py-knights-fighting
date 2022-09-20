from app.stats.features import knight_features
from app.knight.battles import battles


def battle(knights_info):
    lancelot = knight_features(knights_info, knight_name="lancelot")
    arthur = knight_features(knights_info, knight_name="arthur")
    mordred = knight_features(knights_info, knight_name="mordred")
    red_knight = knight_features(knights_info, knight_name="red_knight")

    battles(lancelot, mordred, arthur, red_knight)
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
