from app.data_base.data_base_knights import KNIGHTS
from app.knights_config.character_configuration import Character
from app.battle.battle_knights import Battle


def battle(knights_config: dict) -> dict:
    for knight in knights_config.values():
        power = knight["power"]
        hp = knight["hp"]
        protection = 0
        for armour in knight["armour"]:
            protection += armour["protection"]
        power += knight["weapon"]["power"]

        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                power += knight["potion"]["effect"]["power"]
            if "protection" in knight["potion"]["effect"]:
                protection += knight["potion"]["effect"]["protection"]
            if "hp" in knight["potion"]["effect"]:
                hp += knight["potion"]["effect"]["hp"]

        Character(
            name=knight["name"],
            power=power,
            hp=hp,
            protection=protection
        )

    Battle(
        Character.knight_list["Lancelot"],
        Character.knight_list["Mordred"]
    ).battle_knight()
    Battle(
        Character.knight_list["Artur"],
        Character.knight_list["Red Knight"]
    ).battle_knight()

    return Battle.result


print(battle(KNIGHTS))
