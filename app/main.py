from app.battle import battle_classes
from app.knights import knight_classes
from app.knights import knight_data


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = (
        knight_classes.
        Knight(knights_config, "lancelot").
        knight_characteristics()
    )
    # arthur
    arthur = (
        knight_classes.
        Knight(knights_config, "arthur").
        knight_characteristics()
    )
    # mordred
    mordred = (
        knight_classes.
        Knight(knights_config, "mordred").
        knight_characteristics()
    )
    # red_knight
    red_knight = (
        knight_classes.
        Knight(knights_config, "red_knight").
        knight_characteristics()
    )

    return battle_classes.battle(
        lancelot=lancelot,
        arthur=arthur,
        mordred=mordred,
        red_knight=red_knight
    )


knights = knight_data.KNIGHTS
print(battle(knights))
