from app.knights_config import KnightInfo


def knight_battle(
        first_knight: KnightInfo,
        second_knight: KnightInfo
) -> dict:
    first_knight_hp = first_knight.hp - second_knight.power
    second_knight_hp = second_knight.hp - first_knight.power

    if first_knight_hp <= 0:
        first_knight_hp = 0
    if second_knight_hp <= 0:
        second_knight_hp = 0

    return {first_knight.name: first_knight_hp,
            second_knight.name: second_knight_hp}
