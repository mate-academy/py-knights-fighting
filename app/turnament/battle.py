from __future__ import annotations
from app.entourage.knights import EquippedKnight
from app.entourage.knights import Knight


class Battle:

    @classmethod
    def battle(cls, knights: dict, versus: list) -> dict:
        knights_list = [
            Knight.recruit_a_knight(knight) for knight in knights.values()
        ]
        equiped_knights = [
            EquippedKnight.equip_knight(knight) for knight in knights_list
        ]
        result = {}
        for pair in versus:
            for knight in equiped_knights:
                if pair[0] == knight.name.lower():
                    first = knight
                if pair[1] == knight.name.lower():
                    second = knight
            result.update(Battle.knights_fight(first, second))
        return result

    @classmethod
    def knights_fight(
        cls,
        first_knight: EquippedKnight,
        second_knight: EquippedKnight
    ) -> dict:

        print(f"Battle: {first_knight.name} versus {second_knight.name}\n")

        first_knight_damage = first_knight.power - second_knight.protection
        second_knight_damage = second_knight.power - first_knight.protection
        first_knight.hp = max(0, first_knight.hp - second_knight_damage)
        second_knight.hp = max(0, second_knight.hp - first_knight_damage)

        winner = Battle.who_wins(first_knight, second_knight)

        print(f"      Score: \n\
{first_knight.name} has {first_knight.hp} hp left\n\
{second_knight.name} has {second_knight.hp} hp left\n\
    {winner} Wins!\n")

        return {
            first_knight.name: first_knight.hp,
            second_knight.name: second_knight.hp
        }

    @staticmethod
    def who_wins(
        first_knight: EquippedKnight,
        second_knight: EquippedKnight
    ) -> str:
        if first_knight.hp > second_knight.hp:
            return first_knight.name
        return second_knight.name
