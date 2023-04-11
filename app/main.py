from app.knights.raw_data import knights_info
from app.knights.unprepared_knight import UnpreparedKnight


def battle(knights_info: dict) -> dict:

    lancelot = UnpreparedKnight(knights_info["lancelot"]).battle_preparation()
    arthur = UnpreparedKnight(knights_info["arthur"]).battle_preparation()
    mordred = UnpreparedKnight(knights_info["mordred"]).battle_preparation()
    red_knight = UnpreparedKnight(
        knights_info["red_knight"]
    ).battle_preparation()

    return {
        lancelot.name: lancelot.duel(mordred),
        arthur.name: arthur.duel(red_knight),
        mordred.name: mordred.duel(lancelot),
        red_knight.name: red_knight.duel(arthur)
    }


print(battle(knights_info))
