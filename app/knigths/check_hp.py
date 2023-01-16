from app.knigths.knigth import Knight


def is_dead(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0
