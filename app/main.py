from app.battle import battle
from app.KNIGHTS.knights import knightsConfig
from app.KNIGHTS.knight import Knight


lancelot = Knight(knightsConfig["lancelot"])
arthur = Knight(knightsConfig["arthur"])
mordred = Knight(knightsConfig["mordred"])
red_knight = Knight(knightsConfig["red_knight"])


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
