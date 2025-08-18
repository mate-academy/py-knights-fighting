from json import load
if __name__ == "__main__":
    from modules import Weapon, Armour, Knight, Potion
else:
    from .modules import Weapon, Armour, Knight, Potion


def battle(knights_config: dict) -> dict:
    knights = {}
    # BATTLE PREPARATIONS:
    for name, config in knights_config.items():
        # lancelot
        # lancelot_config = knights_config.get("lancelot")
        knights[name] = Knight(
            name=config.get("name"),
            power=config.get("power"),
            hp=config.get("hp"),
            armour=[Armour(**item) for item in config.get("armour")],
            weapon=Weapon(**config.get("weapon")),
            potion=Potion(config.get("potion")),
        )
        knights[name].before_battle()

    # BATTLE:
    lancelot = knights.get("lancelot")
    mordred = knights.get("mordred")
    red_knight = knights.get("red_knight")
    arthur = knights.get("arthur")
    # 1 Lancelot vs Mordred:
    mordred.attack(lancelot)
    lancelot.attack(mordred)
    # lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    # mordred["hp"] -= lancelot["power"] - mordred["protection"]

    # check if someone fell in battle
    # if lancelot["hp"] <= 0:
    #     lancelot["hp"] = 0

    # if mordred["hp"] <= 0:
    #     mordred["hp"] = 0

    # 2 Arthur vs Red Knight:
    red_knight.attack(arthur)
    arthur.attack(red_knight)

    # arthur["hp"] -= red_knight["power"] - arthur["protection"]
    # red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    # check if someone fell in battle
    # if arthur["hp"] <= 0:
    #     arthur["hp"] = 0

    # if red_knight["hp"] <= 0:
    #     red_knight["hp"] = 0

    # Return battle results:
    return {x.name: x.hp for x in knights.values()}


def main() -> None:
    knights = load(open(
        r"C:\Users\I\PycharmProjects\py-knights-fighting\app\config.json"
    ))
    print(knights)
    # exit()
    print(battle(knights))


if __name__ == "__main__":
    main()
