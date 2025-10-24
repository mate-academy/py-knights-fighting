from app.data.knights_data import KNIGHTS
from app.entities.knight import Knight
from app.battle.battle import Battle


if __name__ == "__main__":
    arthur = Knight("Arthur", KNIGHTS["arthur"])
    lancelot = Knight("Lancelot", KNIGHTS["lancelot"])

    battle = Battle(arthur, lancelot)
    battle.start()
