from app.models.models import Knight


def fight(knight: Knight, enemy: Knight) -> None:
    knight.hp -= enemy.power - knight.protection

    if knight.hp < 0:
        knight.hp = 0
