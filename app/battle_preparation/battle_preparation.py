from app.items.armour import Armour
from app.items.potion import Potion
from app.items.weapon import Weapon
from app.participants.knight import Knight


class BattlePreparation:
    @staticmethod
    def prepare_participants(
            participants: dict[str, dict]) -> dict[str, Knight]:
        participants_objects = {}

        for participant_name, participant in participants.items():
            knight = Knight(
                name=participant["name"],
                power=participant["power"],
                hp=participant["hp"]
            )

            for armour_data in participant.get("armour") or []:
                armour = Armour(
                    armour_data["part"],
                    armour_data["protection"]
                )
                knight.wear_armour(armour)

            weapon_data = participant["weapon"]
            weapon = Weapon(
                weapon_data["name"],
                weapon_data["power"]
            )
            knight.get_armed(weapon)

            if participant["potion"] is not None:
                potion_data = participant["potion"]
                potion = Potion(
                    potion_data["name"],
                    potion_data["effect"]
                )
                knight.drink_potion(potion)

            participants_objects[knight.name] = knight

        return participants_objects
