from app.battle_preparation.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {}
    for key, value in knights_config.items():
        knight = Knight.dict_read(value)
        knight.apply_power()
        knight.apply_potion()
        knights.update({key: knight})

    def _update_hp(knight_stats: Knight, opponent_stats: Knight) -> None:
        knight_stats.hp -= opponent_stats.power - knight_stats.protection
        knight_stats.hp = max(knight_stats.hp, 0)
        opponent_stats.hp -= knight_stats.power - opponent_stats.protection
        opponent_stats.hp = max(opponent_stats.hp, 0)

    _update_hp(knights["lancelot"], knights["mordred"])
    result = {
        "Lancelot": knights["lancelot"].hp,
        "Mordred": knights["mordred"].hp
    }

    _update_hp(knights["arthur"], knights["red_knight"])
    result.update(
        {
            "Artur": knights["arthur"].hp,
            "Red Knight": knights["red_knight"].hp
        }
    )

    return result
