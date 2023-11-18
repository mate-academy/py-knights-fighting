from app.modules.knights import Knight


def battle(knights_dict: dict) -> dict:

    result_dict = {}

    Knight.make_knight(knights_dict)
    knight = Knight.knights

    Knight.fight(knight["Lancelot"], knight["Mordred"])
    Knight.fight(knight["Arthur"], knight["Red Knight"])

    result_dict.update({
        knight["Lancelot"].name: knight["Lancelot"].hp,
        knight["Arthur"].name: knight["Arthur"].hp,
        knight["Mordred"].name: knight["Mordred"].hp,
        knight["Red Knight"].name: knight["Red Knight"].hp
    })

    return result_dict
