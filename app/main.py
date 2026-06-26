from app.data.characters import KNIGHTS
from app.services.character_services import get_characters_as_class


def battle(knights_config: dict) -> dict:
    knights = get_characters_as_class(knights_config)

    for knight in knights:
        knight.increase_protection().increase_power().apply_potion()

    lancelot, arthur, mordred, red_knight = knights

    lancelot -= mordred
    mordred -= lancelot
    red_knight -= arthur
    arthur -= red_knight

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
