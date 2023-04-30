from app.knights.red_knight import Red_knight_
from app.knights.lancelot import Lancelot_
from app.knights.arthur import Arthur_
from app.knights.mordred import Mordred_


def knight_stat(knight: dict) -> tuple:
    hp = 0
    power = 0
    hp += knight["hp"]
    power += knight["power"] + knight["weapon"]["power"]
    for armour in knight["armour"]:
        hp += armour["protection"]
    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            power += knight["potion"]["effect"]["power"]
        if "protection" in knight["potion"]["effect"]:
            hp += knight["potion"]["effect"]["protection"]
        if "hp" in knight["potion"]["effect"]:
            hp += knight["potion"]["effect"]["hp"]
    return (hp, power)


Red_knight_stat = knight_stat(Red_knight_)
Lancelot_stat = knight_stat(Lancelot_)
Arthur_stat = knight_stat(Arthur_)
Mordred_stat = knight_stat(Mordred_)
