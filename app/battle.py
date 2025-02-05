from app.knight import Knight
from app.knights_config import KNIGHTS


def battle(knights_config: dict = KNIGHTS) -> dict:
    lancelot, arthur, mordred, red_knight = [
        Knight(
            name=data.get("name"),
            power=data.get("power"),
            hp=data.get("hp"),
            armour=data.get("armour"),
            weapon=data.get("weapon"),
            potion=data.get("potion"),
        )
        for data in knights_config.values()
    ]
    lancelot.fight(mordred)
    arthur.fight(red_knight)

    battle_result_hp = {}
    for knight in (lancelot, arthur, mordred, red_knight):
        battle_result_hp[knight.name] = knight.hp
    return battle_result_hp


print(battle(knights_config=KNIGHTS))
