from app.Ammunition.armours import Armour
from app.Heroes.knights import Knight
from app.Ammunition.potions import Potion
from app.Ammunition.weapons import Weapon


def classes_creation(knights_config: dict) -> None:
    for knight in knights_config:
        Knight(knights_config[knight]["name"],
               knights_config[knight]["power"],
               knights_config[knight]["hp"])
        Weapon(knights_config[knight]["weapon"]["name"],
               knights_config[knight]["weapon"]["power"])
        if [] not in knights_config[knight]["armour"]:
            for i in range(len(knights_config[knight]["armour"])):
                Armour(knights_config[knight]["armour"][i]["part"],
                       knights_config[knight]["armour"][i]["protection"])
        if knights_config[knight]["potion"] is not None:
            _power = 0
            _health = 0
            _protection = 0
            for eff in knights_config[knight]["potion"]["effect"]:
                if eff == "power":
                    _power = knights_config[knight][
                        "potion"]["effect"]["power"]
                elif eff == "hp":
                    _health = knights_config[knight][
                        "potion"]["effect"]["hp"]
                elif eff == "protection":
                    _protection = knights_config[knight][
                        "potion"]["effect"]["protection"]
            Potion(knights_config[knight]["potion"]["name"],
                   _power, _health, _protection)


def fighters_with_completed_stats(knights_config: dict) -> None:
    for name in knights_config:
        knight_armour = []
        knight_potion = None
        knight_weapon = Weapon.weapons[
            knights_config[name]["weapon"]["name"]
        ]
        if [] not in knights_config[name]["armour"]:
            for i in range(len(knights_config[name]["armour"])):
                knight_armour.append(
                    Armour.armours[
                        knights_config[name]["armour"][i]["part"]
                        + str(knights_config[name]["armour"][i]["protection"])
                    ]
                )
        if knights_config[name]["potion"] is not None:
            knight_potion = Potion.potions[
                knights_config[name]["potion"]["name"]
            ]
        Knight.knights[knights_config[name]["name"]].geather_addition_stats(
            knight_weapon, knight_armour, knight_potion
        )


def royal_battle(first_fighter: Knight, second_fighter: Knight) -> None:
    first_fighter.health -= second_fighter.power - first_fighter.protection
    second_fighter.health -= first_fighter.power - second_fighter.protection
    if first_fighter.health < 0:
        first_fighter.health = 0
    if second_fighter.health < 0:
        second_fighter.health = 0


def battle(knights_config: dict) -> dict:
    classes_creation(knights_config)
    fighters_with_completed_stats(knights_config)

    lancelot = Knight.knights["Lancelot"]
    arthur = Knight.knights["Artur"]
    mordred = Knight.knights["Mordred"]
    red_knight = Knight.knights["Red Knight"]

    royal_battle(lancelot, mordred)
    royal_battle(arthur, red_knight)

    return {
        lancelot.name: lancelot.health,
        arthur.name: arthur.health,
        mordred.name: mordred.health,
        red_knight.name: red_knight.health
    }
