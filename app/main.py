from app.profiles import KNIGHTS
import app.knights.preparation as preparation
from app.knights.fight import fight


def battle(knights_config: dict) -> dict:
    prepared_knights = preparation.preparation(knights_config)
    return (
        fight(prepared_knights["lancelot"], prepared_knights["mordred"])
        | fight(prepared_knights["arthur"], prepared_knights["red_knight"]))

if __name__ == "__main__":
    print(battle(KNIGHTS))
