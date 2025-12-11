from app.knights_cfg import KNIGHTS
from app.battle.battle import knight_init
from app.battle.battle import arena


def battle(knights_cfg: dict) -> dict:
    knights_dct = {
        name: knight_init(item)
        for name, item in knights_cfg.items()
    }
    arena(knight_0=knights_dct["lancelot"],
          knight_1=knights_dct["mordred"])
    arena(knight_0=knights_dct["arthur"],
          knight_1=knights_dct["red_knight"])

    return {"Lancelot": knights_dct["lancelot"].hp,
            "Arthur": knights_dct["arthur"].hp,
            "Mordred": knights_dct["mordred"].hp,
            "Red Knight": knights_dct["red_knight"].hp,
            }


print((battle(KNIGHTS)))
