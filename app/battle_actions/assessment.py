from app.characters.knight import Knight

from app.battle_actions import check, fight


def assessment(knights_config: dict) -> dict:
    warriors = []
    for knight_name, knight_data in knights_config.items():
        knight = Knight(
            name=knight_data.get("name"),
            power=knight_data.get("power"),
            hp=knight_data.get("hp"),
            armour=knight_data.get("armour"),
            weapon=knight_data.get("weapon"),
            potion=knight_data.get("potion"),
        )
        warriors.append(knight)

    duels = [[warriors[0], warriors[2]],
             [warriors[1], warriors[3]]]

    for pair in duels:
        fight.fight(pair)
        check.check_hp(pair)

    return {knight.name: knight.hp for knight in warriors}
