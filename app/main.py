from app.items import weapon
from app.knights import knight


def config_pars(knightsConfig):
    for value in knightsConfig.values():
        knight.Knight(
            name=value["name"],
            power=value["power"] + weapon.Weapon(
                name=value["weapon"]
            )
        )


def battle():
    pass
