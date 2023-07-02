from app.battle.before_battle import Knight
from app.battle.knights import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    def fight(attacker: Knight, defender: Knight) -> None:
        damage = max(0, attacker.power - defender.protection)
        defender.hp = max(0, defender.hp - damage)

    fight(lancelot, mordred)
    fight(mordred, lancelot)
    fight(arthur, red_knight)
    fight(red_knight, arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(KNIGHTS))
