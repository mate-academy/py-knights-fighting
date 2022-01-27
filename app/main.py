from app.characters.knight import Knight
from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion
from app.activities.battle import Battle


def battle(knightsConfig: dict) -> dict:
    Knight.create_the_knight(knightsConfig)
    Armour.protect_the_knight(knightsConfig)
    Weapon.arm_the_knight(knightsConfig)
    Potion.give_a_potion(knightsConfig)

    order = Battle.get_in_order(Knight.knights)

    for rivals in order:
        Battle.fighting(rivals)
        Knight.check_fell(rivals[0])
        Knight.check_fell(rivals[1])

    return {elem.name: elem.hp for elem in Knight.knights.values()}
