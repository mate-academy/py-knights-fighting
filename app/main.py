from models.knight import Knight
from models.equipment import Weapon, Armour, Potion
from battle.arena import fight
from battle.knights_config import KNIGHTS_CONFIG


def battle(knights_config: dict) -> dict:
    knights = []

    for config in knights_config.values():
        knight = Knight(name=config["name"],
                        base_power=config["power"],
                        base_hp=config["hp"])

        if "potion" in config and config["potion"] is not None:
            potion_data = config["potion"]
            knight.apply_potion(Potion(potion_data["name"],
                                       potion_data["effect"]))

        if "weapon" in config:
            weapon_data = config["weapon"]
            knight.set_weapon(Weapon(weapon_data["name"],
                                     weapon_data["power"]))

        if "armour" in config:
            armour_list = [Armour(part["part"], part["protection"])
                           for part in config["armour"]]
            knight.set_armor(armour_list)

        knights.append(knight)

    fight(knights)

    return {knight.name: max(knight.hp, 0)
            for knight in knights}


if __name__ == "__main__":

    results = battle(KNIGHTS_CONFIG)
    for name, hp in results.items():
        print(f"{name}: {hp} HP")
