from app.models.Knight import Knight
from app.data.knight_data import KNIGHTS
from app.battle.prepare import prepare_knights

prepared = prepare_knights(KNIGHTS)

def duel(attacker: Knight, defender: Knight):
    """Один раунд бою між двома лицарями"""
    damage = max(attacker.total_attack() - defender.total_defence(), 0)
    defender.hp -= damage
    if defender.hp < 0:
        defender.hp = 0

    # Контратака лише якщо defender ще живий
    if defender.hp > 0:
        damage = max(defender.total_attack() - attacker.total_defence(), 0)
        attacker.hp -= damage
        if attacker.hp < 0:
            attacker.hp = 0

def battle(prepared: dict):
    duel(prepared["lancelot"], prepared["mordred"])
    duel(prepared["arthur"], prepared["red_knight"])

    name_map = {
        "lancelot": "Lancelot",
        "arthur": "Arthur",
        "mordred": "Mordred",
        "red_knight": "Red Knight"
    }
    return {name_map[name]: knight.hp for name, knight in prepared.items()}


if __name__ == "__main__":
    print(type(prepared["lancelot"]))
    prepared = prepare_knights(KNIGHTS)
    final_hp = battle(prepared)
    for k in prepared.values():
        print(k)
    print("\nFinal HP:", final_hp)