from app.amunition.armour import armour_protection
from app.amunition.weapon import weapon_power
from app.amunition.potion import potion_effect


def ready_to_battle(knights: dict) -> list[tuple]:
    knights_ready = []
    for knight in knights:
        name = knights[knight]["name"]
        hp = (knights[knight]["hp"]
              + potion_effect(knights[knight]["potion"])[0])
        protection = (armour_protection(knights[knight]["armour"])
                      + potion_effect(knights[knight]["potion"])[1])
        power = (knights[knight]["power"]
                 + weapon_power(knights[knight]["weapon"])
                 + potion_effect(knights[knight]["potion"])[2])

        knights_ready.append((name, hp, protection, power))
    return knights_ready
