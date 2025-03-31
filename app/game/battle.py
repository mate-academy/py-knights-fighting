def battle(knight1: "Knight", knight2: "Knight") -> dict[str, int]:
    """
    Simulates a battle between two knights based on their attributes.

    Args:
        knight1 (Knight): The first knight participating in the battle.
        knight2 (Knight): The second knight participating in the battle.

    Returns:
        dict[str, int]: A dictionary with the names of the knights as keys
                        and their remaining health points as values.
    """
    knight1_damage: int = max(0, knight2.power - knight1.protection)
    knight2_damage: int = max(0, knight1.power - knight2.protection)

    knight1.hp = max(0, knight1.hp - knight1_damage)
    knight2.hp = max(0, knight2.hp - knight2_damage)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }