from app.battle.battle import Battle


def battle(knightsconfig: dict) -> dict:
    prepare_result = Battle.prepare_battle(knightsconfig)
    Battle.start_battle(prepare_result["Lancelot"], prepare_result["Mordred"])
    Battle.start_battle(prepare_result["Arthur"], prepare_result["Red Knight"])

    result = {}
    for character in Battle.prepare_battle(knightsconfig):
        name = prepare_result[character].name
        hp = prepare_result[character].hp
        result[name] = hp
    return result
