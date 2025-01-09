from typing import Dict
from app.knight import Knight
from app.knights_config import KNIGHTS


def battle(knightsconfig: Dict[str, Dict]) -> Dict[str, int]:
    lancelot = Knight(**knightsconfig["lancelot"])
    arthur = Knight(**knightsconfig["arthur"])
    mordred = Knight(**knightsconfig["mordred"])
    red_knight = Knight(**knightsconfig["red_knight"])

    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


if __name__ == "__main__":
    results = battle(KNIGHTS)
    print(results)
