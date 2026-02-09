from app.knights import knight
from app.knights.list_knights import KNIGHTS
from app.knights.factory_knights import factory_knights
from app.knights.knight import Knight
from app.battle_m import Battle


def battle(knightsConfig):
    knights = factory_knights(knightsConfig)

    lancelot = knights["Lancelot"]
    arthur = knights["Arthur"]
    mordred = knights["Mordred"]
    red_knight = knights["Red Knight"]

    lanc_vs_mord = Battle(lancelot, mordred)
    arth_vs_rk = Battle(arthur, red_knight)

    lanc_vs_mord.fight()
    arth_vs_rk.fight()

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }

if __name__ == "__main__":
    print(battle(KNIGHTS))