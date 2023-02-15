from app.data.source_data import KNIGHTS

from app.knight import Knight
from app.ammunition.armour import Armour
from app.ammunition.potion import Potion
from app.ammunition.weapon import Weapon


def create_knights(knights: dict) -> {Knight}:
    knights_dict = {}

    for params in knights.values():
        name = params["name"]
        power = params["power"]
        hp = params["hp"]

        armour = [Armour(armour["part"], armour["protection"])
                  for armour in params["armour"]]

        weapon = Weapon(params["weapon"]["name"],
                        params["weapon"]["power"])
        try:
            potion = Potion(params["potion"]["name"],
                            params["potion"]["effect"])
        except TypeError:
            potion = None

        knights_dict[name] = Knight(name, power, hp, armour, weapon, potion)

    return knights_dict


def duel(knight1: Knight, knight2: Knight) -> None:
    knight1.hit(knight2)
    knight2.hit(knight1)


def battle(knights_config: dict) -> {}:
    knights = create_knights(knights_config)
    participants = {
        knights["Lancelot"]: knights["Mordred"],
        knights["Artur"]: knights["Red Knight"]
    }
    [duel(participant1, participant2)
     for participant1, participant2 in participants.items()]

    return Knight.get_hp_all_knights()


if __name__ == "__main__":
    battle(KNIGHTS)
