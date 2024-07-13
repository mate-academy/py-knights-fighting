from app.knight import Knight


def battle(knights_config: dict) -> str:
    knights = _create_knights(knights_config)
    battle_preparations(knights)
    return start_battle(knights)


def battle_preparations(knights: list) -> None:
    _apply_armour(knights)
    _apply_weapon(knights)
    _use_potion(knights)


def start_battle(knights: list) -> None:
    # Lancelot vs Mordred
    _duel_battle(knights[0], knights[2])
    _duel_battle(knights[2], knights[0])

    # Arthur vs Red Knight
    _duel_battle(knights[1], knights[3])
    _duel_battle(knights[3], knights[1])

    return {
        knight.name: knight.hp
        for knight in knights
    }


def _create_knights(knights_config: dict) -> list:
    knights = []

    for stats in knights_config.values():
        knight = Knight(
            stats["name"],
            stats["power"],
            stats["hp"],
            stats["armour"],
            stats["weapon"],
            stats["potion"]
        )
        knights.append(knight)

    return knights


def _duel_battle(knight_1: Knight, knight_2: Knight) -> None:
    knight_1.hp = knight_1.hp - (knight_2.power - knight_1.protection)
    _check_hp([knight_1, knight_2])


def _check_hp(knights: list) -> None:
    for knight in knights:
        if knight.hp <= 0:
            knight.hp = 0


def _apply_armour(knights: list) -> None:
    for knight in knights:
        protection = 0
        if knight.armour:
            for armour in knight.armour:
                protection += armour.protection
            knight.protection = protection


def _apply_weapon(knights: list) -> None:
    for knight in knights:
        knight.power += knight.weapon.power


def _use_potion(knights: list) -> None:
    for knight in knights:
        knight.use_potion()
