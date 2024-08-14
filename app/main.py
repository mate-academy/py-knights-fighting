from app.warrior.equipment.armour import Armour
from app.warrior.equipment.potion import Potion
from app.warrior.equipment.weapon import Weapon
from app.warrior.knight import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = {}
    for data in knights_config.values():
        knight = Knight(data["name"],
                        data["power"],
                        data["hp"],
                        parse_armour(data["armour"]),
                        parse_weapon(data["weapon"]),
                        parse_potion(data["potion"]))
        knight.get_ready_to_battle()
        knights.update({data["name"]: knight})

    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    knights["Lancelot"].fight(knights["Mordred"])

    # 2 Arthur vs Red Knight:
    knights["Arthur"].fight(knights["Red Knight"])

    return {knight.name: knight.hp for knight in knights.values()}


def parse_armour(armour: list[dict]) -> list[Armour]:
    return [Armour(element["part"],
                   element["protection"]) for element in armour]


def parse_weapon(weapon: dict) -> Weapon:
    return Weapon(weapon["name"], weapon["power"])


def parse_potion(potion: dict) -> Potion:
    return Potion(potion["name"], potion["effect"]) if potion else None
