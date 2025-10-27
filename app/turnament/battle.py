from __future__ import annotations
from app.entourage.knights import EquipedKnight
# from app.entourage.knights import Knight
# from app.entourage.knights_list import KNIGHTS


class Battle:

    @classmethod
    def knights_fight(
        cls,
        first_knight: EquipedKnight,
        second_knight: EquipedKnight
    ) -> str:
        first_knight.hp -= max(0, second_knight.power - first_knight.armour)
        second_knight.hp -= max(0, first_knight.power - second_knight.armour)

        winner = Battle.who_wins(first_knight, second_knight)

        return f"   Battle score: \n\
{first_knight.name} has {first_knight.hp} hp left\n\
{second_knight.name} has {second_knight.hp} hp left\n\
    {winner} Wins!"

    @staticmethod
    def who_wins(
        first_knight: EquipedKnight,
        second_knight: EquipedKnight
    ) -> str:
        if first_knight.hp > second_knight.hp:
            return first_knight.name
        return second_knight.name


"""
if __name__ == "__main__":
    line = "=" * 30
    print(f"Testing Code: \n{line} \n")

    knight_list = [Knight.recruit_a_knight(knight)->
      for knight in KNIGHTS.values()]

    knight1 = EquipedKnight.equip_knight(knight_list[2])
    knight2 = EquipedKnight.equip_knight(knight_list[3])

    print(f"{knight1}\n{knight2}")

    print(Battle.KnightsFight(knight1, knight2))

    print(f"\n{line}")
"""
