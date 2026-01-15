from app.knight.knight import Knight
from app.fight.to_arm import to_arm
from app.fight.to_fight import fight


def battle(knights_config: dict) -> dict[Knight]:

    lancelot = Knight(knights_config.get("lancelot"))
    mordred = Knight(knights_config.get("mordred"))
    arthur = Knight(knights_config.get("arthur"))
    red_knight = Knight(knights_config.get("red_knight"))

    lancelot, mordred = fight(to_arm(lancelot), to_arm(mordred))
    arthur, red_knight = fight(to_arm(arthur), to_arm(red_knight))

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
