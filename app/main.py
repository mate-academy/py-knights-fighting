import app.GameSettings.KnightsSettings as KnightsSettings
import app.Characters.Knight as Knight
KNIGHTS = KnightsSettings.KnightsSettings().knights_settings


def battle(knights_config):
    # Prepare knights from settings
    lancelot = Knight.Knight.knight_from_dict(knights_config["lancelot"])
    arthur = Knight.Knight.knight_from_dict(knights_config["arthur"])
    mordred = Knight.Knight.knight_from_dict(knights_config["mordred"])
    red_knight = Knight.Knight.knight_from_dict(knights_config["red_knight"])
    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.change_knights_hp(mordred)

    # 2 Arthur vs Red Knight:
    arthur.change_knights_hp(red_knight)

    # Return battle results:
    # return {
    #     lancelot["name"]: lancelot["hp"],
    #     arthur["name"]: arthur["hp"],
    #     mordred["name"]: mordred["hp"],
    #     red_knight["name"]: red_knight["hp"],
    # }
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
