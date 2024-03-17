from app.KNIGHTS.knights import Knights
from app.KNIGHTS.knight import Knight
from app.fight import fight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    fight(knight1=lancelot, knight2=mordred)
    fight(knight1=arthur, knight2=red_knight)

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
        red_knight.name: red_knight.hp
    }


print(battle(Knights))
        red_knight.name: red_knight.hp,
    }

print(main())
