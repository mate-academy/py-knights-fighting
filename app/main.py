from app.database.participants import KNIGHTS
from app.knights.knight import Knight
from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion
from app.arena.fight import Fight


def battle(knights_config: dict) -> dict:
    participants = {
        name: Knight(knight.get("name"), knight.get("power"), knight.get("hp"))
        for name, knight in knights_config.items()
    }

    for name, knight in participants.items():
        participant = knights_config.get(name)

        participant_armour = participant.get("armour")

        if participant_armour is not None:
            knight_armour = [
                Armour(armour.get("part"), armour.get("protection"))
                for armour in participant_armour
            ]

            for armour in knight_armour:
                knight.apply_armour(armour)

        participant_weapon = participant.get("weapon")

        weapon = Weapon(
            participant_weapon.get("name"),
            participant_weapon.get("power")
        )

        knight.apply_weapon(weapon)

        participant_potion = participant.get("potion")

        if participant_potion is not None:
            potion = Potion(
                participant_potion.get("name"),
                participant_potion.get("effect")
            )

            knight.apply_potion(potion)

    Fight.fight(participants.get("lancelot"), participants.get("mordred"))
    Fight.fight(participants.get("arthur"), participants.get("red_knight"))

    return {knight.name: knight.hp for knight in participants.values()}


print(battle(KNIGHTS))
