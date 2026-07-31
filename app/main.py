from app.knight import Knight
from app.potion import Potion
from app.weapon import Weapon
from app.armor import Armor


def battle(knights_config: dict) -> dict:

    knights = {}
    for knight_name, knight_data in knights_config.items():
        armor = [
            Armor(a["part"], a["protection"])
            for a in knight_data.get("armour", [])
        ]
        weapon = Weapon(
            knight_data["weapon"]["name"],
            knight_data["weapon"]["power"]
        )
        potion = None
        if knight_data["potion"] is not None:
            potion = Potion(
                knight_data["potion"]["name"],
                knight_data["potion"]["effect"]
            )
        knights[knight_name] = Knight(
            name=knight_data["name"],
            power=knight_data["power"],
            hp=knight_data["hp"],
            armor=armor,
            weapon=weapon,
            potion=potion,
        )

    lancelot_battle_result = knights["lancelot"].battle(knights["mordred"])
    arthur_battle_result = knights["arthur"].battle(knights["red_knight"])

    return {
        **lancelot_battle_result,
        **arthur_battle_result,
    }
