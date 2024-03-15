from app.battle import battle
from app.KNIGHTS.knights import KnightsConfig
from app.KNIGHTS.knight import Knight


lancelot = Knight(KnightsConfig["lancelot"])
arthur = Knight(KnightsConfig["arthur"])
mordred = Knight(KnightsConfig["mordred"])
red_knight = Knight(KnightsConfig["red_knight"])


def main() -> dict:
    battle(knight1=lancelot, knight2=arthur)
    battle(knight1=mordred, knight2=red_knight)
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(main())
