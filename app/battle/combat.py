from app.battle.entities import Knight


def run_duel(first_knight: Knight, second_knight: Knight) -> None:
    first_power = first_knight.stats.power
    second_power = second_knight.stats.power

    first_knight.stats.take_damage(second_power)
    second_knight.stats.take_damage(first_power)
