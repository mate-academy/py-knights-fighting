from app.components.armour import create_armour_instances
from app.components.knight import Knight
from app.components.potion import create_potion_instance
from app.components.weapon import create_weapon_instance


class Battle:
    @staticmethod
    def battle_moves(knight_1: Knight, knight_2: Knight) -> None:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection
        for knight in [knight_1, knight_2]:
            if knight.hp < 0:
                knight.hp = 0


def knight_preparing(knight_config: dict) -> Knight:
    knight = Knight(
        name=knight_config["name"],
        power=knight_config["power"],
        hp=knight_config["hp"],
    )
    if knight_config.get("armour", []):
        knight.apply_armour(create_armour_instances(knight_config["armour"]))
    knight.apply_weapon(create_weapon_instance(knight_config["weapon"]))
    if knight_config["potion"] is not None:
        knight.apply_potion(create_potion_instance(knight_config["potion"]))

    return knight


def create_knights_dict(knights: dict) -> dict[str, Knight]:
    return {
        knight_name: knight_preparing(knight_config)
        for knight_name, knight_config in knights.items()
    }
