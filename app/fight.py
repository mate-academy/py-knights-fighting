from app.knight_class import Knight

def fight(knight: Knight, enemy: Knight) -> None:
    knight.hp -= enemy.power - knight.protection
    knight.hp = 0 if knight.hp <= 0 else knight.hp
