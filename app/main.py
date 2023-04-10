from app.knights.raw_data import knights
from app.knights.unprepared_knight import UnpreparedKnight


def battle(knights: dict) -> dict:

    lancelot = UnpreparedKnight(knights["lancelot"]).battle_preparation()
    arthur = UnpreparedKnight(knights["arthur"]).battle_preparation()
    mordred = UnpreparedKnight(knights["mordred"]).battle_preparation()
    red_knight = UnpreparedKnight(knights["red_knight"]).battle_preparation()

    return {
        lancelot.name: lancelot.duel(mordred),
        arthur.name: arthur.duel(red_knight),
        mordred.name: mordred.duel(lancelot),
        red_knight.name: red_knight.duel(arthur)
    }


print(battle(knights))
