import json
from app.battle.prep_and_fight import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    lancelot.fight(mordred)
    mordred.fight(lancelot)
    arthur.fight(red_knight)
    red_knight.fight(arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


if __name__ == "__main__":
    file_path = "knights_info.json"
    with open(file_path, "r") as file:
        data = json.load(file)
    print(data)
