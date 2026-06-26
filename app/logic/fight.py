from app.knights.knight import Knight


def get_fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp -= (
        second_knight.get_power()
        - first_knight.get_protection()
    )
    second_knight.hp -= (
        first_knight.get_power()
        - second_knight.get_protection()
    )
