from app.knigths.knigth import Knight


def fight(knight_1: Knight, knight_2: Knight) -> None:
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection
