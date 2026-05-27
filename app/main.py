from app.battle import build_knight


def battle(knights: dict) -> dict:
    lancelot = build_knight(knights["lancelot"])
    mordred = build_knight(knights["mordred"])
    arthur = build_knight(knights["arthur"])
    red_knight = build_knight(knights["red_knight"])

    for knight in [lancelot, mordred, arthur, red_knight]:
        if knight.potion:
            knight.hp += knight.potion.effect.get("hp", 0)

    # Snapshot powers before any potion is cleared
    lancelot_power = lancelot.get_total_power()
    mordred_power = mordred.get_total_power()
    arthur_power = arthur.get_total_power()
    red_knight_power = red_knight.get_total_power()

    lancelot.take_damage(mordred_power)
    mordred.take_damage(lancelot_power)

    arthur.take_damage(red_knight_power)
    red_knight.take_damage(arthur_power)

    return {
        "Lancelot": lancelot.hp,
        "Arthur": arthur.hp,
        "Mordred": mordred.hp,
        "Red Knight": red_knight.hp,
    }
