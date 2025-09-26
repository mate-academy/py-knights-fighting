from app.knights.prepare_knight import KnightConfig

def battle_win(first_knight: KnightConfig, second_knight: KnightConfig) -> dict[str, int]:
    dmg_value_first_knight = second_knight.power - first_knight.protection
    first_knight.hp -= dmg_value_first_knight
    dmg_value_second_knight = first_knight.power - second_knight.protection
    second_knight.hp -= dmg_value_second_knight

    if first_knight.hp <= 0:
        first_knight.hp = 0

    if second_knight.hp <= 0:
        second_knight.hp = 0

    battle_result = {
        first_knight.name: first_knight.hp,
        second_knight.name: second_knight.hp
    }

    return battle_result
