from app.actions.create_battle import (
    prepare_characters, fight, show_battle_results
)


def battle(knights_config: dict) -> dict:
    knights = prepare_characters(knights_config)
    fight(knights["Lancelot"], knights["Mordred"])
    fight(knights["Arthur"], knights["Red Knight"])
    return show_battle_results(knights)
