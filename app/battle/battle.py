from app.battle.equipment import equip_knight


def battle(knights: dict) -> dict:

    warriors = []

    for name, options in knights.items():
        warrior = equip_knight(knights[name])
        warriors.append(warrior)

    battle_result = {
        warriors[0]["name"]:
            max(warriors[0]["hp"]
                - (warriors[2]["power"]
                - warriors[0]["protection"]), 0),

        warriors[2]["name"]:
            max(warriors[2]["hp"]
                - (warriors[0]["power"]
                   - warriors[2]["protection"]), 0),

        warriors[1]["name"]:
            max(warriors[1]["hp"]
                - (warriors[3]["power"]
                   - warriors[1]["protection"]), 0),

        warriors[3]["name"]:
            max(warriors[3]["hp"]
                - (warriors[1]["power"]
                   - warriors[3]["protection"]), 0)}

    return battle_result
