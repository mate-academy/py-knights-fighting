from app.characters.knight import Knight

from app.battle_actions import check, fight


def assessment(knights_config: dict) -> dict:
    warriors = {}
    for knight_name, knight_data in knights_config.items():
        knight = Knight(
            name=knight_data.get("name"),
            power=knight_data.get("power"),
            hp=knight_data.get("hp"),
            armour=knight_data.get("armour"),
            weapon=knight_data.get("weapon"),
            potion=knight_data.get("potion"),
        )
        knight.equip()
        warriors[knight.name] = knight

    duels = [[warriors["Lancelot"], warriors["Mordred"]],
             [warriors["Artur"], warriors["Red Knight"]]]

    for duel in duels:
        fight.fight(duel)
        check.check_hp(duel[0])
        check.check_hp(duel[1])

    return {knight.name: knight.hp for knight in warriors.values()}
