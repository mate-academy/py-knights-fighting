from app.Knights.knight import Knight
from app.Staff.armour import Armour
from app.Staff.potion import Potion
from app.Staff.weapon import Weapon


def knights_creation(config: dict) -> Knight:
    character = Knight(config["name"], config["power"], config["hp"])
    armours = []
    if config["armour"] is not None:
        for armour in config["armour"]:
            armours.append(Armour(
                armour.get("part"),
                armour.get("protection")
            ))
    if config["potion"] is not None:
        effect = config["potion"]["effect"]
        potion = Potion(
            config["potion"]["name"],
            effect.get("power", 0),
            effect.get("hp", 0),
            effect.get("protection", 0)
        )
    else:
        potion = Potion("Unknown")
    weapon = Weapon(config["weapon"]["name"], config["weapon"]["power"])
    character.knight_stats_completing(armours, weapon, potion)

    return character


def health_update(fighter: Knight) -> None:
    if fighter.health_points < 0:
        fighter.health_points = 0


def battle_simulation(fighter1: Knight, fighter2: Knight) -> None:
    fighter1.health_points -= fighter2.power - fighter1.protection
    fighter2.health_points -= fighter1.power - fighter2.protection
    for fighter in [fighter1, fighter2]:
        health_update(fighter)


def battle(knights: dict) -> dict:
    heroes = {
        knight: knights_creation(knights[knight])
        for knight in knights
    }

    battle_simulation(heroes["lancelot"], heroes["mordred"])
    battle_simulation(heroes["arthur"], heroes["red_knight"])

    return {
        heroes[hero].name: heroes[hero].health_points
        for hero in heroes
    }
