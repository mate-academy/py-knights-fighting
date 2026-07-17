from app.knights.knight import Knight


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp = (first_knight.hp
                       - (second_knight.damage() - first_knight.protection))
    if first_knight.hp < 0:
        first_knight.hp = 0
    second_knight.hp = (second_knight.hp
                        - (first_knight.damage() - second_knight.protection))
    if second_knight.hp < 0:
        second_knight.hp = 0
