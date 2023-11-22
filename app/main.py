from random import sample
from knights_parameters.heroes import knights


def hp_adjustment(hp: int) -> int:
    if hp < 0:
        return 0
    return hp


def battle(knights: list) -> None:
    # Activating equipment and buffs
    for knight in knights:
        knight.parameters_in_battle()

    # We cast lots
    duelists = sample(knights, 2)
    knight_1, knight_2 = duelists

    # Let's start the fight
    remaining_hp = [
        {
            "kinght": knight_1,
            "hp": hp_adjustment(
                knight_1.battle_hp
                - (knight_2.battle_power - knight_1.battle_armor))
        },
        {
            "kinght": knight_2,
            "hp": hp_adjustment(
                knight_2.battle_hp
                - (knight_1.battle_power - knight_2.battle_armor))
        }
    ]
    # Print results table
    result_fight(remaining_hp)


def result_fight(knights: list) -> None:
    knight_1hp = knights[0]["hp"]
    knight_2hp = knights[1]["hp"]

    if knight_1hp > knight_2hp == 0:
        print(
            f"Winner : {knights[0]['kinght'].name}\n"
            f"damage caused: {knights[0]['kinght'].battle_power}\n"
            f"remaining hp: {knight_1hp}\n\n"
            f"Loser: {knights[1]['kinght'].name}\n"
            f"damage caused: {knights[1]['kinght'].battle_power}\n"
            f"remaining hp: {knight_2hp}"
        )

    if knight_2hp > knight_1hp == 0:
        print(
            f"Winner : {knights[1]['kinght'].name}\n"
            f"damage caused: {knights[1]['kinght'].battle_power}\n"
            f"remaining hp: {knight_2hp}\n\n"
            f"Loser: {knights[0]['kinght'].name}\n"
            f"damage caused: {knights[0]['kinght'].battle_power}\n"
            f"remaining hp: {knight_1hp}"
        )
    if knight_2hp > 0 and knight_1hp > 0:
        print(
            "Draw\n"
            f"{knights[0]['kinght'].name}\n"
            f"damage caused: {knights[0]['kinght'].battle_power}\n"
            f"remaining hp: {knight_1hp}\n\n"
            f"{knights[1]['kinght'].name}\n"
            f"damage caused: {knights[1]['kinght'].battle_power}\n"
            f"remaining hp: {knight_2hp}"
        )


battle(knights)
