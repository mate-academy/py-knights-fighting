from app.knight import Knight


def battle(knightsconfig: dict) -> dict:
    knight_names = ["lancelot", "arthur", "mordred", "red_knight"]
    knights = {name: Knight(**knightsconfig[name]) for name in knight_names}

    for knight in knights.values():
        knight.prepare_for_battle()

    battles = [("lancelot", "mordred"), ("arthur", "red_knight")]

    results = {}
    for attacker, defender in battles:
        attacker_knight = knights[attacker]
        defender_knight = knights[defender]

        attacker_hp = max(0, attacker_knight.hp - (
            defender_knight.power - attacker_knight.protection))
        defender_hp = max(0, defender_knight.hp - (
            attacker_knight.power - defender_knight.protection))

        results[attacker_knight.name] = attacker_hp
        results[defender_knight.name] = defender_hp

    return results
