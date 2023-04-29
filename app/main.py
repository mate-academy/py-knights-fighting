from app.knights import get_knights
from app.knights import Knight


def battle(resulting_dict: dict) -> dict:
    results = {}
    # BATTLE PREPARATIONS:
    lancelot = Knight(**resulting_dict["lancelot"])
    lancelot.apply_stats()
    arthur = Knight(**resulting_dict["arthur"])
    arthur.apply_stats()
    mordred = Knight(**resulting_dict["mordred"])
    mordred.apply_stats()
    red_knight = Knight(**resulting_dict["red_knight"])
    red_knight.apply_stats()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    results.update(lancelot.battle(mordred))
    # 2 Arthur vs Red Knight:
    results.update(arthur.battle(red_knight))
    # Return battle results:
    return {
        "Arthur": results.get(arthur),
        "Lancelot": results.get(lancelot),
        "Mordred": results.get(mordred),
        "Red Knight": results.get(red_knight),
    }


if __name__ == "__main__":
    resulting_dict_ = get_knights()
    battle(resulting_dict_)
