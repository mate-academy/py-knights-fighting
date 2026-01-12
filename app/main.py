from .engine import _prepare_knight_stats, _duel


def battle(knights_config: dict) -> dict:
    """
    Conducts two fixed battles (Lancelot vs Mordred, Arthur vs Red Knight)
    and returns the final HP of all knights.
    """
    lancelot = _prepare_knight_stats(knights_config["lancelot"])
    mordred = _prepare_knight_stats(knights_config["mordred"])
    arthur = _prepare_knight_stats(knights_config["arthur"])
    red_knight = _prepare_knight_stats(knights_config["red_knight"])

    lancelot_hp, mordred_hp = _duel(lancelot, mordred)
    arthur_hp, red_knight_hp = _duel(arthur, red_knight)

    return {
        knights_config["lancelot"]["name"]: lancelot_hp,
        knights_config["mordred"]["name"]: mordred_hp,
        knights_config["arthur"]["name"]: arthur_hp,
        knights_config["red_knight"]["name"]: red_knight_hp,
    }
