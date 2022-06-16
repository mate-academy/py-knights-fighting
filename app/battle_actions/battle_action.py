from app.character.knight import Knight
from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon


def create_knight(knight_values: dict):
    armour = []
    for item in knight_values.get("armour"):
        armour.append(Armour(item.get("part"), item.get("protection")))

    weapon_info = knight_values.get("weapon")
    weapon = Weapon(weapon_info["name"], weapon_info["power"])

    potion_info = knight_values.get("potion")
    potion = None
    if potion_info is not None:
        potion = Potion(potion_info["name"], potion_info["effect"])

    return Knight(knight_values.get("name"),
                  knight_values.get("power"),
                  knight_values.get("hp"),
                  armour,
                  weapon,
                  potion)


def put_armour_on(knight):
    for item in knight.armour:
        knight.protection += item.protection


def draw_weapon(knight):
    knight.power += knight.weapon.power


def drink_potion(knight):
    knight_potion = knight.potion
    if knight_potion is not None:
        if "power" in knight_potion.effect:
            knight.power += knight_potion.effect["power"]
        if "protection" in knight_potion.effect:
            knight.protection += knight_potion.effect["protection"]
        if "hp" in knight_potion.effect:
            knight.hp += knight_potion.effect["hp"]


def apply_equipment(knight: Knight):
    put_armour_on(knight)
    draw_weapon(knight)
    drink_potion(knight)


def check_hp(knight_one, knight_two):
    if knight_one.hp <= 0:
        knight_one.hp = 0

    if knight_two.hp <= 0:
        knight_two.hp = 0


def fight(knight_one: Knight, knight_two: Knight):
    knight_one.hp -= knight_two.power - knight_one.protection
    knight_two.hp -= knight_one.power - knight_two.protection
    check_hp(knight_one, knight_two)
