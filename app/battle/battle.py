from app.knights.knights import Knight


def battle(knights: dict) -> dict:

    warriors = {}
    battle_result = {}

    for options in knights.values():
        warrior = Knight(options)
        warriors[warrior.name] = warrior.return_properties()

    pairings = [("Lancelot", "Mordred"), ("Arthur", "Red Knight")]

    for attacker_name, defender_name in pairings:
        attacker = warriors[attacker_name]
        defender = warriors[defender_name]

        attacker_hp_after_battle = max(
            attacker["hp"] - (defender["power"] - attacker["protection"]), 0
        )

        defender_hp_after_battle = max(
            defender["hp"] - (attacker["power"] - defender["protection"]), 0
        )

        battle_result[attacker_name] = attacker_hp_after_battle
        battle_result[defender_name] = defender_hp_after_battle

    return battle_result
