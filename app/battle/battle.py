from app.knights.knight import Knight
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon
from app.equipment.armour import Armour


battle_net = {
    "battle1": ["Lancelot", "Mordred"],
    "battle2": ["Artur", "Red Knight"]
}


def fight(knight1: Knight, knight2: Knight) -> None:
    knight1.get_ready_for_fight()
    knight2.get_ready_for_fight()

    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    if knight1.hp < 0:
        knight1.hp = 0
    if knight2.hp < 0:
        knight2.hp = 0


def return_results() -> dict:
    return {
        Knight.knights_arr[participant].name:
            Knight.knights_arr[participant].hp
        for participant in Knight.knights_arr
    }


def clear_data() -> None:
    Knight.knights_arr.clear()
    Potion.potions_arr.clear()
    Weapon.weapons_arr.clear()
    Armour.armours_arr.clear()
