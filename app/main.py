from app.knights_battle.knights import Knight
from app.knights_battle.weapons import Weapon
from app.knights_battle.potions import Potion


def prepare_knights(knights_config: dict) -> dict:
    knights = {}
    for key, data in knights_config.items():
        knights[key] = Knight(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data["armour"],
            weapon=Weapon(data["weapon"]["name"], data["weapon"]["power"]),
            potion=Potion(data["potion"]["name"], data["potion"]["effect"])
            if data.get("potion") else None
        )
    return knights


def battle(knights_config: dict) -> dict:
    knights = prepare_knights(knights_config)

    knights["lancelot"].apply_weapon()
    knights["lancelot"].apply_potion()
    knights["mordred"].apply_weapon()
    knights["mordred"].apply_potion()
    knights["arthur"].apply_weapon()
    knights["arthur"].apply_potion()
    knights["red_knight"].apply_weapon()
    knights["red_knight"].apply_potion()

    knights["lancelot"].take_damage(knights["mordred"].
                                    power - knights["lancelot"].protection)
    knights["mordred"].take_damage(knights["lancelot"].
                                   power - knights["mordred"].protection)
    knights["arthur"].take_damage(knights["red_knight"].
                                  power - knights["arthur"].protection)
    knights["red_knight"].take_damage(knights["arthur"].
                                      power - knights["red_knight"].protection)

    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["red_knight"].name: knights["red_knight"].hp,
    }
