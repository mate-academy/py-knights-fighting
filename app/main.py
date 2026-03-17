from app.knights.prepared_knight import knight_from_dict
from app.battle.fight import fight


def battle(config: dict) -> dict[str, int]:
    lancelot = knight_from_dict(config["lancelot"])
    arthur = knight_from_dict(config["arthur"])
    mordred = knight_from_dict(config["mordred"])
    red = knight_from_dict(config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red.name: red.hp,
    }
