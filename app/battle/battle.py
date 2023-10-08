from app.participants.knight import Knight


def battle(*args: list[Knight, Knight]) -> None:
    for pair in args:
        pair[0].hp -= pair[1].power - pair[0].protection
        pair[1].hp -= pair[0].power - pair[1].protection

        for knight in pair:
            if knight.hp < 0:
                knight.hp = 0
                print(f"{knight.name} fell down in battle")
