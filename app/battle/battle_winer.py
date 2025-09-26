from app.knights.prepare_knight import KnightConfig

def battle_win(first_knight: KnightConfig, second_knight: KnightConfig) -> str:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection

    if first_knight.hp <= 0:
        first_knight.hp = 0

    if second_knight.hp <= 0:
        second_knight.hp = 0

    return f"{first_knight.name}: {first_knight.hp}\n{second_knight.name}: {second_knight.hp}"
