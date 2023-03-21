from app.knigths.knigth import Knight


def change_dead_knight_hp_to_0(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0
