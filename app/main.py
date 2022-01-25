from app.uitls.checks import check_who_won_or_loose
from app.uitls.feature_count import feature_count
from app.data.data import KNIGHTS


def battle(knights_config):
    lancelot = feature_count(knights_config, "lancelot")
    arthur = feature_count(knights_config, "arthur")
    mordred = feature_count(knights_config, "mordred")
    red_knight = feature_count(knights_config, "red_knight")
    check_who_won_or_loose(mordred, lancelot)
    check_who_won_or_loose(red_knight, arthur)
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


if __name__ == '__main__':
    battle(KNIGHTS)
