from app.knight import Knight


def create_knights_stat(knights_config: dict) -> dict:
    knights_stat = {}
    for knight in knights_config.values():
        some_knight = Knight(
            knight["name"],
            knight["hp"],
            knight["power"]
        )
        some_knight.apply_improvements(knight)
        knights_stat[some_knight.name] = some_knight
    return knights_stat


def fight(fighter1: Knight, fighter2: Knight) -> None:
    fighter1.hp -= fighter2.power - fighter1.protection
    fighter2.hp -= fighter1.power - fighter2.protection
    fighter1.hp = is_alive(fighter1.hp)
    fighter2.hp = is_alive(fighter2.hp)


def is_alive(hp: int) -> int:
    if hp <= 0:
        hp = 0
    return hp
