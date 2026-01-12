from app.knights.knights_init import Knight
from app.knights.result_fight import fight
from app.knights.preparing import preparation_knight


def battle(knightsconfig: dict) -> dict:
    knights = {}

    for name, config in knightsconfig.items():
        knight = Knight(config)
        knight = preparation_knight(knight)
        knights[name] = knight

    lancelot_hp, mordred_hp = fight(knights["lancelot"], knights["mordred"])
    arthur_hp, red_knight_hp = fight(knights["arthur"], knights["red_knight"])

    return {
        lancelot_hp.name: lancelot_hp.hp,
        arthur_hp.name: arthur_hp.hp,
        mordred_hp.name: mordred_hp.hp,
        red_knight_hp.name: red_knight_hp.hp,
    }
