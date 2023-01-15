from app.Ammunition.armours import Armour
from app.Heroes.knights import Knight
from app.Ammunition.potions import Potion
from app.Ammunition.weapons import Weapon


def knights_creation_config(config: dict, knight: str) -> Knight:
    name = config[knight]["name"]
    power = config[knight]["power"]
    health = config[knight]["hp"]
    weapon = Weapon(config[knight]["weapon"]["name"],
                    config[knight]["weapon"]["power"])
    armour = []
    for _armour in config[knight]["armour"]:
        armour.append(Armour(_armour["part"], _armour["protection"]))
    potion = None
    if config[knight]["potion"] is not None:
        effect = config[knight]["potion"]["effect"]
        potion = Potion(config[knight]["potion"]["name"],
                        effect["power"] if "power" in effect else 0,
                        effect["hp"] if "hp" in effect else 0,
                        effect["protection"] if "protection" in effect else 0)
    return Knight(name, power, health, weapon, armour, potion)


def health_update(knight: Knight) -> None:
    if knight.health < 0:
        knight.health = 0


def royal_battle(fighter_1: Knight, fighter_2: Knight) -> None:
    fighter_1.health -= fighter_2.power - fighter_1.protection
    fighter_2.health -= fighter_1.power - fighter_2.protection
    health_update(fighter_1)
    health_update(fighter_2)


def battle(knights_config: dict) -> dict:
    lancelot = knights_creation_config(knights_config, "lancelot")
    arthur = knights_creation_config(knights_config, "arthur")
    mordred = knights_creation_config(knights_config, "mordred")
    red_knight = knights_creation_config(knights_config, "red_knight")

    royal_battle(lancelot, mordred)
    royal_battle(arthur, red_knight)

    return {
        lancelot.name: lancelot.health,
        arthur.name: arthur.health,
        mordred.name: mordred.health,
        red_knight.name: red_knight.health
    }
