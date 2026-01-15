from app.weapon import Weapon
from app.armour import Armour
from app.potion import Potion
from app.knights import Knight


def create_knight(knightsconfig: dict, knight_name: str) -> Knight:
    knight_data = knightsconfig.get(knight_name)
    if knight_data:
        weapon_data = knight_data["weapon"]
        potion_data = knight_data["potion"]
        knight = Knight(
            name=knight_data["name"],
            power=knight_data["power"],
            hp=knight_data["hp"],
            armour=[Armour(a["part"], a["protection"])
                    for a in knight_data["armour"]],
            weapon=Weapon(weapon_data["name"], weapon_data["power"]),
            potion=Potion(
                potion_data["name"],
                potion_data["effect"]
            ) if potion_data else None,
        )
        return knight
    else:
        raise (ValueError
               (f"Knight with name {knight_name} not in the config."))
