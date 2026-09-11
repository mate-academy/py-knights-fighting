from app.models.knight import Knight
from app.data.KNIGHTS_DATABASE import KNIGHTS


def attack(attacker: "Knight", defensor: "Knight") -> int:
    defensor.hp -= (attacker.power - defensor.protection)
    return defensor.hp


def new_round(knights: list[Knight]) -> None:
    for index, attacker in enumerate(knights):
        defensor = knights[1 - index]
        print(
            f"{attacker.name} {attacker.hp}❤️ \
            {attacker.power}⚔️ atacked {defensor.name} \
            {defensor.hp}❤️ {defensor.protection}🛡️"
        )
        if attack(attacker, defensor) <= 0:
            defensor.hp = 0


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = []
    knights = [Knight(knights_config[knight]) for knight in knights_config]

    for knight in knights:
        knight.apply_equipments()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    new_round([knights[0], knights[2]])

    # 2 Arthur vs Red Knight:
    new_round([knights[1], knights[3]])

    # Return battle results:
    return {
        knight.name: knight.hp for knight in knights
    }


print(battle(KNIGHTS))
