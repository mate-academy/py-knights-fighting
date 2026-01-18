from app.build_instance.knights import Knight


def check_hp(hp: int) -> int:
    return hp if hp > 0 else 0


def pairs_fight(fighter_1: Knight, fighter_2: Knight) -> None:
    fighter_1.hp -= fighter_2.power - fighter_1.protection
    fighter_2.hp -= fighter_1.power - fighter_2.protection

    fighter_1.hp = check_hp(fighter_1.hp)
    fighter_2.hp = check_hp(fighter_2.hp)


def all_battles(knights_pairs: dict, knights: dict) -> None:
    for fighter_1, fighter_2 in knights_pairs.items():
        pairs_fight(knights[fighter_1], knights[fighter_2])


def battle_final_result(knights_: dict) -> dict:
    return {
        knights_[knight].name: knights_[knight].hp
        for knight in knights_}
