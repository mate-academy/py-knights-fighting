from app.characters.knight import Knight


def check_hp(knight: Knight) -> None:
    if knight.hp < 0:
        knight.hp = 0


def duel(duel_participants: list[Knight]) -> None:
    first_knight = duel_participants[0]
    second_knight = duel_participants[1]

    first_knight.attack(second_knight)
    second_knight.attack(first_knight)

    [check_hp(knight) for knight in duel_participants]
