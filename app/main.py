from app.knights.factory_knights import factory_knights
from app.battle_m import Battle


def battle(knights_config: dict) -> dict:
    knights = factory_knights(knights_config)

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
