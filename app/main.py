from app.characters.knight import Knight
from app.items.equipment import Armour, Weapon, Potion
from app.events.battle import Battle
from app.config import KNIGHTS


def battle(knights_data: dict) -> dict:

    knights = [create_knight(knights_data[knight]) for knight in knights_data]
    lancelot, arthur, mordred, red_knight = knights
    for knight in knights:
        equipment = get_equipment(knights_data, knight)
        get_ready_to_battle(equipment, knight)

    battles = [Battle(lancelot, mordred), Battle(arthur, red_knight)]
    for one_battle in battles:
        one_battle.fight()

    battles_result = Battle.get_result()
    return battles_result


def create_knight(knight_info: dict) -> Knight:
    knight_name = knight_info["name"]
    knight_hp = knight_info["hp"]
    knight_power = knight_info["power"]
    return Knight(name=knight_name, hp=knight_hp, power=knight_power)


def get_equipment(knights_data: dict, warrior: Knight) -> dict:
    knight_name = warrior.name.lower().replace(" ", "_")
    if knight_name == "artur":
        knight_name = "arthur"
    warrior_weapon = knights_data[knight_name]["weapon"]
    warrior_potion = knights_data[knight_name]["potion"]
    warrior_armour = knights_data[knight_name]["armour"]
    return {
        "weapon": warrior_weapon,
        "potion": warrior_potion,
        "armour": warrior_armour
    }


def get_ready_to_battle(warrior_equipment: dict, warrior: Knight) -> None:
    get_weapon(warrior_equipment["weapon"], warrior)
    if warrior_equipment.get("potion"):
        get_potion(warrior_equipment["potion"], warrior)
    get_armour(warrior_equipment["armour"], warrior)


def get_weapon(weapon: dict, warrior: Knight) -> None:
    warrior.add_weapon(Weapon(name=weapon["name"], power=weapon["power"]))


def get_potion(potion: dict, warrior: Knight) -> None:
    warrior.add_potion(Potion(name=potion["name"], effect=potion["effect"]))


def get_armour(armour: list[dict], warrior: Knight) -> None:
    armour = [Armour(element["part"], element["protection"])
              for element in armour]
    for element in armour:
        warrior.add_armour(element)


print(battle(KNIGHTS))
