from app.preparations.participant import Participant


def prepare_knight(knight_name: str) -> None:
    knight = Participant.find_knights(knight_name)
    for adds in knight.extras:
        knight.apply_extras(adds)


def fight(first_name: str, second_name: str) -> None:
    knight_first = Participant.find_knights(first_name)
    knight_second = Participant.find_knights(second_name)
    knight_first.hp -= knight_second.power - knight_first.protection
    knight_second.hp -= knight_first.power - knight_second.protection

    for everybody in (knight_first, knight_second):
        if everybody.hp < 0:
            everybody.hp = 0
        Participant.fighters.append(everybody)
