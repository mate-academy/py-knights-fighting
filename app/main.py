from typing import Dict
from app.config.knights_config import KNIGHTS
from app.entities.armour import Armour
from app.entities.weapon import Weapon
from app.entities.potion import Potion
from app.entities.knight import Knight


def create_knight(knight_config: dict) -> Knight:
    armour = [Armour(**a) for a in knight_config["armour"]]
    weapon = Weapon(**knight_config["weapon"])
    potion = Potion(**knight_config["potion"]) if (
        knight_config)["potion"] else None
    return Knight(knight_config["name"], knight_config["power"],
                  knight_config["hp"], armour, weapon, potion)


# Нова функція для обробки битви між двома лицарями
def knight_battle(knight1: Knight, knight2: Knight) -> None:
    knight2.hp -= max(0, knight1.power - knight2.protection)
    knight1.hp -= max(0, knight2.power - knight1.protection)


def battle(knightsconfig: Dict[str, dict]) -> Dict[str, dict]:
    knights = {name: create_knight(config) for name, config in
               knightsconfig.items()}

    knight_battle(knights["lancelot"], knights["mordred"])
    knight_battle(knights["arthur"], knights["red_knight"])

    return {
        knights["lancelot"].name: max(0, knights["lancelot"].hp),
        knights["arthur"].name: max(0, knights["arthur"].hp),
        knights["mordred"].name: max(0, knights["mordred"].hp),
        knights["red_knight"].name: max(0, knights["red_knight"].hp),
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
