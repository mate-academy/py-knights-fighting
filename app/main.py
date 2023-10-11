from app.battle.battle import Battle


def battle(knightsconfig: dict) -> dict:
    prepare_result = Battle.prepare_battle(knightsconfig)
    Battle.start_battle(prepare_result["Lancelot"], prepare_result["Mordred"])
    Battle.start_battle(prepare_result["Arthur"], prepare_result["Red Knight"])
    return {
        prepare_result["Lancelot"].name: prepare_result["Lancelot"].hp,
        prepare_result["Arthur"].name: prepare_result["Arthur"].hp,
        prepare_result["Mordred"].name: prepare_result["Mordred"].hp,
        prepare_result["Red Knight"].name: prepare_result["Red Knight"].hp
    }
