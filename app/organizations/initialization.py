from app.preparations.participant import Participant
from app.preparations.extras import Weapon, Armor, Potion


def initialization(knights_config: dict) -> None:
    for knight in knights_config.values():
        Participant(knight["name"], knight["power"], knight["hp"])
        tmp_knight_obj = Participant.find_knights(knight["name"])
        for armor in knight["armour"]:
            tmp_knight_obj.extras.append(
                Armor(armor.get("part"), armor.get("protection"))
            )
        tmp_knight_obj.extras.append(
            Weapon(knight["weapon"].get("name"),
                   knight["weapon"].get("power"))
        )
        if knight["potion"] is not None:
            tmp_knight_obj.extras.append(
                Potion(knight["potion"].get("name"),
                       knight["potion"].get("effect"))
            )
