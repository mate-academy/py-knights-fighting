from app.knights.armour import Armour
from app.knights.potion import Potion
from app.knights.weapon import Weapon
from app.knights.knight import Knight
from app.knights.knight_init import KNIGHTS


def config_knight(name: str, knights_in: dict) -> Knight:
    knight = Knight(knights_in[name]['name'],
                    knights_in[name]['power'],
                    knights_in[name]['hp'])
    for armour in knights_in[name]['armour']:
        armour_knt = Armour(armour['part'], armour['protection'])
        knight.equip_armour(armour_knt)
    if knights_in[name]['weapon']:
        weapon = Weapon(knights_in[name]['weapon']['name'],
                        knights_in[name]['weapon']['power'])
        knight.equip_weapon(weapon)
    if knights_in[name]['potion'] is not None:
        potion = Potion(knights_in[name]['potion']['name'],
                        knights_in[name]['potion']['effect'])
        knight.equip_potion(potion)
    return knight


def battle(knights_config) -> dict:
    lancelot = config_knight('lancelot', knights_config)
    arthur = config_knight('arthur', knights_config)
    mordred = config_knight('mordred', knights_config)
    red_knight = config_knight('red_knight', knights_config)
    result = {}
    result.update({lancelot.name: lancelot.battle(mordred)})
    result.update({mordred.name: mordred.battle(lancelot)})
    result.update({arthur.name: arthur.battle(red_knight)})
    result.update({red_knight.name: red_knight.battle(arthur)})
    return result


print(battle(KNIGHTS))
