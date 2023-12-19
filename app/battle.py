from app.models import Knight, Armour, Weapon, Potion


def calculate_damage(dealer: Knight, receiver: Knight) -> int:
    base_damage = dealer.power + dealer.weapon.power
    actual_damage = max(base_damage - receiver.total_protection(), 0)
    return actual_damage


def battle(knight1: Knight, knight2: Knight) -> str:
    knight1.apply_potion_effects()
    knight2.apply_potion_effects()

    damage_to_knight2 = calculate_damage(knight1, knight2)
    damage_to_knight1 = calculate_damage(knight2, knight1)

    knight1.hp -= damage_to_knight1
    knight2.hp -= damage_to_knight2

    if knight1.hp <= 0 and knight2.hp <= 0:
        return "Both knight have fallen"
    elif knight1.hp <= 0:
        return f"{knight2.name} wins"
    elif knight2.hp <= 0:
        return f"{knight1.name} wins"
    else:
        return "Both knights are still standing"
