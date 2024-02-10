from app.battle.equipment import equip_knight


def battle(knights: dict) -> dict:

    warriors = []

    for name, options in knights.items():
        warrior = equip_knight(knights[name])
        warriors.append(warrior)

    battle_result = {}

    for i in range(len(warriors) // 2):
        attacker_index = i
        defender_index = attacker_index + 2

        attacker = warriors[attacker_index]
        defender = warriors[defender_index]

        attacker_hp_after_battle = max(
            attacker["hp"] - (defender["power"] - attacker["protection"]), 0)
        defender_hp_after_battle = max(
            defender["hp"] - (attacker["power"] - defender["protection"]), 0)

        battle_result[attacker["name"]] = attacker_hp_after_battle
        battle_result[defender["name"]] = defender_hp_after_battle

    return battle_result
