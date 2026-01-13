from app.config import KNIGHTS
from app.models import Knight, Armour, Weapon, Potion


def battle(knights_config: dict) -> dict:
    knights = {}

    for name, data in knights_config.items():
        armour_list = [
            Armour(part=a["part"], protection=a["protection"])
            for a in data["armour"]
        ]

        weapon = Weapon(name=data["weapon"]["name"],
                        power=data["weapon"]["power"]
                        )

        potion = None
        if data["potion"]:
            potion = Potion(name=data["potion"]["name"],
                            effect=data["potion"]["effect"])

        knights[name] = Knight(
            name=data["name"],
            base_power=data["power"],
            hp=data["hp"],
            armour=armour_list,
            weapon=weapon,
            potion=potion
        )

    fights = [("lancelot", "mordred"),
              ("arthur", "red_knight"),]

    for attaker_key, defender_key in fights:
        attacker = knights[attaker_key]
        defender = knights[defender_key]
        attacker.fight(defender)
        defender.fight(attacker)
    return {k.name: k.hp for k in knights.values()}


if __name__ == "__main__":
    print(battle(KNIGHTS))
