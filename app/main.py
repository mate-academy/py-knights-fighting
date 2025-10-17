from app.game.knight import Knight
from app.game.armour import Armour
from app.game.weapon import Weapon
from app.game.potion import Potion
from app.game.battle import Battle
from app.game.data import KNIGHTS


def create_knights(knight_keys: dict) -> Knight:
    armour = [Armour(items["part"], items["protection"])
              for items in knight_keys["armour"]]

    weapon = knight_keys["weapon"]
    weapon = Weapon(weapon["name"], weapon["power"])

    potion = knight_keys["potion"]
    if potion:
        potion = Potion(potion["name"], potion["effect"])

    knight = Knight(name=knight_keys["name"],
                    power=knight_keys["power"],
                    hp=knight_keys["hp"],
                    armour=armour,
                    weapon=weapon,
                    potion=potion)

    return knight


def battle(knights_config: dict) -> dict:
    knights = []
    for key in knights_config:
        knight = create_knights(knights_config[key])
        knights.append(knight)

    battle_result = Battle.start_battle(knights[0], knights[2])
    battle_result.update(Battle.start_battle(knights[1], knights[3]))

    return battle_result


print(battle(KNIGHTS))
