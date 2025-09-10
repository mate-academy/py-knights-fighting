from json import load
from app.modules import Weapon, Armour, Knight, Potion


def battle(knights_config: dict) -> dict:
    knights = {}
    for name, config in knights_config.items():
        knights[name] = Knight(
            name=config.get("name"),
            power=config.get("power"),
            hp=config.get("hp"),
            armour=[Armour(**item) for item in config.get("armour")],
            weapon=Weapon(**config.get("weapon")),
            potion=Potion(config.get("potion")),
        )
        knights[name].before_battle()

    lancelot = knights.get("lancelot")
    mordred = knights.get("mordred")
    red_knight = knights.get("red_knight")
    arthur = knights.get("arthur")
    mordred.attack(lancelot)
    lancelot.attack(mordred)
    red_knight.attack(arthur)
    arthur.attack(red_knight)

    return {x.name: x.hp for x in knights.values()}


def main() -> None:
    with open("app/config.json", "r") as f:
        knights = load(f)
    result = battle(knights)
    print(result)


if __name__ == "__main__":
    main()
