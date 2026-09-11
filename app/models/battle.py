from app.models.knight import Knight
from app.data.KNIGHTS_DATABASE import KNIGHTS


def apply_equipments(knight: "Knight"):
    knight.apply_armours()
    knight.apply_weapon()
    knight.apply_potion()

def attack(attacker: "Knight", defensor: "Knight"):
    defensor.hp -= (attacker.power - defensor.protection)
    return defensor.hp


def new_round(knights: list[Knight]):
    for index, attacker in enumerate(knights):
        defensor = knights[1 - index]
        print(f"{attacker.name} {attacker.hp}❤️ {attacker.power}⚔️ atacked {defensor.name} {defensor.hp}❤️ {defensor.protection}🛡️")
        if attack(attacker, defensor) <= 0:
            defensor.hp = 0


def battle(knightsConfig):
    # BATTLE PREPARATIONS:
    knights = []
    knights = [Knight(knightsConfig[knight]) for knight in knightsConfig]

    for knight in knights:
        apply_equipments(knight)

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
