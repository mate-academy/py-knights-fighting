from app.knight import Knight
from app.preparation import create_battle_list


def duel(first_fighter: Knight, second_fighter: Knight) -> None:
    first_fighter_stats = first_fighter.knights_stats()
    second_fighter_stats = second_fighter.knights_stats()
    first_fighter.hp = (first_fighter_stats["hp"]
                        - (second_fighter_stats["power"]
                        - first_fighter_stats["protection"])
                        )
    second_fighter.hp = (second_fighter_stats["hp"]
                         - (first_fighter_stats["power"]
                         - second_fighter_stats["protection"])
                         )

    if first_fighter.hp <= 0:
        first_fighter.hp = 0

    if second_fighter.hp <= 0:
        second_fighter.hp = 0


def battle(knights: dict) -> dict[str, int]:
    battle_list = create_battle_list(knights)
    duel(battle_list[0], battle_list[2])
    duel(battle_list[1], battle_list[3])
    battle_result = {
        battle_list[0].name: battle_list[0].hp,
        battle_list[1].name: battle_list[1].hp,
        battle_list[2].name: battle_list[2].hp,
        battle_list[3].name: battle_list[3].hp,
    }
    return battle_result
