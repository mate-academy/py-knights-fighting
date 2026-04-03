from app.knights.knights import KnightBeforeBattle


def combat(
        first_knight: KnightBeforeBattle,
        second_knight: KnightBeforeBattle
) -> dict:
    first_knight_hp = (first_knight.hp
                       - (second_knight.power
                          - first_knight.protection))
    second_knight_hp = (second_knight.hp
                        - (first_knight.power
                           - second_knight.protection))

    return {
        first_knight.name:
            first_knight_hp if first_knight_hp > 0 else 0,
        second_knight.name:
            second_knight_hp if second_knight_hp > 0 else 0
    }
