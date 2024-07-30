from app.knight import Knight


def battle(knights_config: dict) -> dict[str, int]:
    knights = create_knights(knights_config)
    for knight in knights:
        battle_preparations(knight)
    return start_battle(*knights)


def battle_preparations(knight: Knight) -> None:
    apply_armour(knight)
    apply_weapon(knight)
    use_potion(knight)


def start_battle(
        lancelot: Knight,
        arthur: Knight,
        mordred: Knight,
        red_knight: Knight
) -> dict[str, int]:
    # Lancelot vs Mordred
    duel_battle(lancelot, mordred)
    duel_battle(mordred, lancelot)

    # Arthur vs Red Knight
    duel_battle(arthur, red_knight)
    duel_battle(red_knight, arthur)

    return {
        knight.name: knight.hp
        for knight in [lancelot, arthur, mordred, red_knight]
    }


def create_knights(knights_config: dict) -> list:
    return [
        Knight(
            stats["name"],
            stats["power"],
            stats["hp"],
            armour=Knight.set_armours(stats["armour"]),
            weapon=Knight.set_weapon(stats["weapon"]),
            potion=Knight.set_potion(stats["potion"])
        )
        for stats in knights_config.values()
    ]


def duel_battle(knight_1: Knight, knight_2: Knight) -> None:
    knight_1.hp = knight_1.hp - (knight_2.power - knight_1.protection)
    check_hp([knight_1, knight_2])


def check_hp(knights: list) -> None:
    for knight in knights:
        if knight.hp <= 0:
            knight.hp = 0


def apply_armour(knight: Knight) -> None:
    protection = 0
    if not knight.armour:
        knight.protection = protection
        return
    for armour in knight.armour:
        protection += armour.protection
    knight.protection = protection


def apply_weapon(knight: Knight) -> None:
    knight.power += knight.weapon.power


def use_potion(knight: Knight) -> None:
    knight.use_potion()
