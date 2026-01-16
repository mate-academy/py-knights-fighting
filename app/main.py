from app.data.knights_data import KNIGHTS
from app.entities.knight import Knight


def battle(): -> None:
    arthur = Knight("Arthur", KNIGHTS["arthur"])
    lancelot = Knight("Lancelot", KNIGHTS["lancelot"])

    # начинаем бой
    arthur.fight(lancelot)

    # возвращаем HP, не меньше 0
    return {
        arthur.name: max(arthur.hp, 0),
        lancelot.name: max(lancelot.hp, 0),
    }

if __name__ == "__main__":
    print(battle())
