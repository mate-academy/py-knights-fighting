from app.data import KNIGHTS
from app.knight import Knight
from app.battle import single_battle


def battle(knights_config: str) -> None:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    lancelot_vs_mordred = single_battle(lancelot, mordred)
    arthur_vs_red_knight = single_battle(arthur, red_knight)

    results = {
        lancelot.name: lancelot_vs_mordred[lancelot.name],
        mordred.name: lancelot_vs_mordred[mordred.name],
        arthur.name: arthur_vs_red_knight[arthur.name],
        red_knight.name: arthur_vs_red_knight[red_knight.name],
    }

    return results


if __name__ == "__main__":
    results = battle(KNIGHTS)
    print("Battle Results:")
    for knight, hp in results.items():
        print(f"{knight}: {hp} HP")
